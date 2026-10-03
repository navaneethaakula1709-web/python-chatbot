import random
import streamlit as st

from chatbot_engine import get_answer, get_context_answer
from study_planner import find_plan
from practice_mode import QUESTIONS, check_answer


# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="Python QA Chatbot",
    page_icon="🤖",
    layout="centered"
)


# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title("🤖 Python QA Chatbot")
st.write("Ask questions about Python, Machine Learning, NLP and more.")


# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_question" not in st.session_state:
    st.session_state.last_question = None

if "study_planner" not in st.session_state:
    st.session_state.study_planner = False

if "practice_mode" not in st.session_state:
    st.session_state.practice_mode = False

if "practice_question" not in st.session_state:
    st.session_state.practice_question = None

if "practice_topic" not in st.session_state:
    st.session_state.practice_topic = None

if "practice_score" not in st.session_state:
    st.session_state.practice_score = None


# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:

    st.header("⚙️ Options")

    # Study Planner
    if st.button("📚 Study Planner"):

        st.session_state.study_planner = True
        st.session_state.practice_mode = False


    # Practice Mode
    if st.button("🎯 Practice Mode"):

        st.session_state.practice_mode = True
        st.session_state.study_planner = False

        # Reset question when entering Practice Mode
        st.session_state.practice_question = None
        st.session_state.practice_score = None


    # Clear Chat
    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []
        st.session_state.last_question = None
        st.session_state.study_planner = False
        st.session_state.practice_mode = False
        st.session_state.practice_question = None
        st.session_state.practice_score = None

        st.rerun()


    st.markdown("---")

    st.subheader("💡 Example Questions")

    st.write("• What is Python?")
    st.write("• What is a tuple?")
    st.write("• List vs tuple")
    st.write("• Who invented Python?")
    st.write("• What is machine learning?")
    st.write("• Explain decorators")


# -------------------------------------------------
# DISPLAY PREVIOUS CHAT
# -------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# =================================================
# STUDY PLANNER
# =================================================

if st.session_state.study_planner:

    st.subheader("📚 Study Planner")

    st.write(
        "Choose a subject to generate a 30-day study plan."
    )

    subject = st.selectbox(
        "Select your subject:",
        [
            "Python",
            "Machine Learning",
            "Data Analyst",
            "AI"
        ]
    )

    if st.button("🚀 Generate Study Plan"):

        plan = find_plan(
            f"Create a {subject} study plan"
        )

        if plan:

            st.success(plan["title"])

            st.write("### 🎯 Goal")
            st.write(plan["goal"])

            st.write("### ⏰ Recommended Study Time")
            st.write(plan["daily"])

            st.write("### 📖 Topics to Learn")

            for number, topic in enumerate(
                plan["topics"],
                start=1
            ):
                st.write(
                    f"{number}. {topic}"
                )

            st.write("### ✍️ Practice Activities")

            for activity in plan["practice"]:

                st.write(
                    f"• {activity}"
                )

            st.write("### 🚀 Recommended Project")

            st.write(plan["project"])


# =================================================
# PRACTICE MODE
# =================================================

if st.session_state.practice_mode:

    st.subheader("🎯 Practice Mode")

    st.write(
        "Practice programming and technical concepts."
    )

    # Topic selection
    topic = st.selectbox(
        "Choose a practice topic:",
        [
            "Python",
            "OOP",
            "SQL",
            "Machine Learning",
            "NLP"
        ]
    )

    topic_key = topic.lower()

    # Generate first question
    if st.session_state.practice_question is None:

        st.session_state.practice_question = random.choice(
            QUESTIONS[topic_key]
        )

        st.session_state.practice_topic = topic_key


    # If topic changes
    if st.session_state.practice_topic != topic_key:

        st.session_state.practice_topic = topic_key

        st.session_state.practice_question = random.choice(
            QUESTIONS[topic_key]
        )

        st.session_state.practice_score = None


    question_data = st.session_state.practice_question


    st.markdown("---")

    st.write("### ❓ Practice Question")

    st.info(
        question_data["question"]
    )


    # Answer box
    answer = st.text_area(
        "✍️ Write your answer:",
        height=180,
        placeholder="Type your answer here..."
    )


    col1, col2, col3 = st.columns(3)


    # -------------------------------------------------
    # CHECK ANSWER
    # -------------------------------------------------

    with col1:

        if st.button("✅ Check Answer"):

            if answer.strip() == "":

                st.warning(
                    "Please write your answer first."
                )

            else:

                score = check_answer(
                    answer,
                    question_data["keywords"]
                )

                st.session_state.practice_score = score

                if score >= 70:

                    st.success(
                        f"Good attempt! ✅ "
                        f"Concept coverage: {score:.0f}%"
                    )

                elif score >= 40:

                    st.warning(
                        f"You are on the right track! 👍 "
                        f"Concept coverage: {score:.0f}%"
                    )

                else:

                    st.error(
                        f"Keep practicing! 💪 "
                        f"Concept coverage: {score:.0f}%"
                    )


    # -------------------------------------------------
    # SKIP QUESTION
    # -------------------------------------------------

    with col2:

        if st.button("⏭️ Skip"):

            st.session_state.practice_question = random.choice(
                QUESTIONS[topic_key]
            )

            st.session_state.practice_score = None

            st.rerun()


    # -------------------------------------------------
    # SHOW EXPECTED CONCEPTS
    # -------------------------------------------------

    with col3:

        if st.button("💡 Show Concepts"):

            st.session_state.show_concepts = True


    # Show expected concepts
    if st.session_state.get("show_concepts", False):

        st.write("### 💡 Expected Concepts")

        for keyword in question_data["keywords"]:

            st.write(
                f"• {keyword}"
            )


# =================================================
# NORMAL CHATBOT
# =================================================

st.markdown("---")

st.subheader("💬 Chat with your Python Assistant")


question = st.chat_input(
    "Ask your question..."
)


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


    # Follow-up question
    if st.session_state.last_question:

        answer_data = get_context_answer(
            question,
            st.session_state.last_question,
            None
        )


    # Normal question
    if answer_data is None:

        answer_data = get_answer(
            question
        )


    answer = answer_data.get(
        "answer",
        "Sorry, I could not find an answer."
    )


    # Display chatbot answer
    with st.chat_message("assistant"):

        st.markdown(answer)


    # Save answer
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })


    # Remember question
    st.session_state.last_question = question