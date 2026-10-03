import streamlit as st

from chatbot_engine import get_answer, get_context_answer


st.set_page_config(
    page_title="Python QA Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Python QA Chatbot")
st.write("Ask questions about Python, Machine Learning, NLP and more.")


# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_question" not in st.session_state:
    st.session_state.last_question = None


# Sidebar
with st.sidebar:
    st.header("⚙️ Options")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.last_question = None
        st.rerun()

    st.markdown("---")

    st.subheader("💡 Example Questions")
    st.write("• What is Python?")
    st.write("• What is a tuple?")
    st.write("• List vs tuple")
    st.write("• Who invented Python?")
    st.write("• What is machine learning?")
    st.write("• Explain decorators")


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
question = st.chat_input("Ask your question...")


if question:

    # Display user question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)


    # Get answer
    answer_data = None

    # Check follow-up question
    if st.session_state.last_question:

        answer_data = get_context_answer(
            question,
            st.session_state.last_question,
            None
        )


    # Normal question
    if answer_data is None:
        answer_data = get_answer(question)


    answer = answer_data.get(
        "answer",
        "Sorry, I could not find an answer."
    )


    # Display chatbot answer
    with st.chat_message("assistant"):
        st.markdown(answer)


    # Save chatbot answer
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })


    # Remember current question
    st.session_state.last_question = question