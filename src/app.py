import random
import streamlit as st

from chatbot_engine import get_answer, get_context_answer
from study_planner import find_plan
from practice_mode import QUESTIONS, check_answer


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Python AI Learning Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7ff 0%, #eef2ff 100%);
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        color: #1f2937;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 17px;
        color: #6b7280;
        margin-bottom: 30px;
    }

    .feature-card {
        background: white;
        padding: 22px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        min-height: 150px;
    }

    .feature-card h3 {
        color: #111827;
        margin-bottom: 8px;
    }

    .feature-card p {
        color: #6b7280;
        font-size: 14px;
    }

    .section-title {
        font-size: 28px;
        font-weight: 700;
        color: #1f2937;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    .question-box {
        background: white;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        margin-top: 15px;
        margin-bottom: 20px;
    }

    section[data-testid="stSidebar"] {
        background: white;
    }

    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "messages": [],
    "mode": "chat",
    "practice_question": None,
    "practice_topic": None,
    "practice_score": None,
    "show_concepts": False,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def extract_answer(result):
    """
    chatbot_engine may return either a string or a dictionary.
    Always convert it into the clean answer text for the UI.
    """
    if isinstance(result, dict):
        answer = result.get("answer")

        if answer is None:
            answer = result.get("definition")

        if answer is None:
            answer = result.get("response")

        if answer is None:
            answer = str(result)

        return str(answer)

    if result is None:
        return "Sorry, I could not find an answer for that question."

    return str(result)


def get_chatbot_answer(question):
    """
    Get a clean answer from chatbot_engine.

    New questions use get_answer().
    Simple follow-up questions can use get_context_answer().
    """
    question = str(question).strip()

    if not question:
        return "Please enter a Python-related question."

    try:
        # First try the normal engine.
        result = get_answer(question)
        answer = extract_answer(result)

        if answer and answer != "None":
            return answer

    except Exception:
        pass

    # Fallback to context engine.
    try:
        result = get_context_answer(question, None)
        answer = extract_answer(result)

        if answer and answer != "None":
            return answer

    except Exception as error:
        return (
            "Sorry, I could not generate an answer right now.\n\n"
            f"Error: {error}"
        )

    return "Sorry, I could not find an answer for that question."


def reset_practice():
    st.session_state.practice_question = None
    st.session_state.practice_score = None
    st.session_state.show_concepts = False


def choose_practice_question(topic_key):
    questions = QUESTIONS.get(topic_key, [])

    if not questions:
        return None

    if len(questions) == 1:
        return questions[0]

    current = st.session_state.practice_question

    choices = [q for q in questions if q != current]

    return random.choice(choices or questions)


def get_question_text(question_data):
    if isinstance(question_data, dict):
        return str(question_data.get("question", "Practice question"))

    return str(question_data)


def get_keywords(question_data):
    if isinstance(question_data, dict):
        return question_data.get("keywords", [])

    return []


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown("## ⚙️ Menu")
    st.markdown("---")

    if st.button("💬 Chatbot", use_container_width=True):
        st.session_state.mode = "chat"

    if st.button("📚 Study Planner", use_container_width=True):
        st.session_state.mode = "study"

    if st.button("🎯 Practice Mode", use_container_width=True):
        st.session_state.mode = "practice"
        reset_practice()

    st.markdown("---")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.markdown("### 💡 Example Questions")

    examples = [
        "What is Python?",
        "What is a variable?",
        "What is a tuple?",
        "List vs tuple",
        "What is inheritance?",
        "What is a generator?",
        "Explain decorators",
        "How does garbage collection work in Python?",
        "How is memory managed in Python?",
        "What is the GIL?",
        "How does dictionary lookup work internally?",
        "Why are strings immutable in Python?",
    ]

    for example in examples:
        st.caption("• " + example)

    st.markdown("---")
    st.caption("🤖 Python AI Learning Assistant")
    st.caption("Python + NLP + Machine Learning")


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    '<div class="main-title">💬 Python Question-Answering Chatbot</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    "Learn Python, practice concepts, and explore Python internals with AI."
    "</div>",
    unsafe_allow_html=True,
)


# ============================================================
# CHATBOT MODE
# ============================================================

if st.session_state.mode == "chat":

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <h3>💬 Ask Questions</h3>
                <p>Ask beginner to advanced Python questions.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <h3>🧠 Learn Internals</h3>
                <p>Explore memory, garbage collection, GIL and more.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="feature-card">
                <h3>🚀 Practice</h3>
                <p>Use Practice Mode and Study Planner to improve.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### 💡 Ask your Python question")

    st.info(
        "Ask any Python-related question. "
        "You can ask beginner, intermediate, advanced, "
        "or deep Python internals questions."
    )

    # Previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Ask your Python question...")

    if question:
        clean_question = question.strip()

        # Show user message immediately.
        st.session_state.messages.append(
            {
                "role": "user",
                "content": clean_question,
            }
        )

        answer = get_chatbot_answer(clean_question)

        # Store only clean text, never the complete dictionary.
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        st.rerun()


# ============================================================
# STUDY PLANNER
# ============================================================

elif st.session_state.mode == "study":

    st.markdown(
        '<div class="section-title">📚 30-Day Study Planner</div>',
        unsafe_allow_html=True,
    )

    st.write(
        "Choose a learning path and get a structured study plan."
    )

    topic = st.selectbox(
        "Choose your learning path",
        [
            "Python",
            "Machine Learning",
            "Data Analyst",
            "AI",
        ],
    )

    if st.button(
        "🚀 Generate Study Plan",
        use_container_width=True,
    ):
        try:
            plan = find_plan(topic.lower())

            if not plan:
                st.warning("No study plan was found for this topic.")
            else:
                st.success(
                    f"Study plan generated for {topic}!"
                )

                if isinstance(plan, dict):

                    # Common dictionary format.
                    if "days" in plan:
                        st.markdown("### 📅 Study Schedule")

                        days = plan["days"]

                        if isinstance(days, dict):
                            for day, content in days.items():
                                st.markdown(f"**{day}**")
                                st.write(content)

                        elif isinstance(days, list):
                            for index, content in enumerate(days, 1):
                                st.markdown(f"**Day {index}**")
                                st.write(content)

                    # Display any other useful plan fields.
                    for key, value in plan.items():
                        if key == "days":
                            continue

                        title = str(key).replace("_", " ").title()
                        st.markdown(f"### {title}")

                        if isinstance(value, (dict, list)):
                            st.write(value)
                        else:
                            st.write(value)

                elif isinstance(plan, list):
                    for index, content in enumerate(plan, 1):
                        st.markdown(f"**Day {index}**")
                        st.write(content)

                else:
                    st.write(plan)

        except Exception as error:
            st.error(
                "Unable to generate the study plan."
            )
            st.code(str(error))


# ============================================================
# PRACTICE MODE
# ============================================================

elif st.session_state.mode == "practice":

    st.markdown(
        '<div class="section-title">🎯 Python Practice Mode</div>',
        unsafe_allow_html=True,
    )

    st.write(
        "Choose a topic, answer the question, and check your concept coverage."
    )

    topic_keys = list(QUESTIONS.keys())

    if not topic_keys:
        st.error("No practice questions are available.")
    else:

        topic_key = st.selectbox(
            "Choose a topic",
            topic_keys,
            format_func=lambda x: str(x).replace("_", " ").title(),
        )

        # If topic changed, reset the question.
        if st.session_state.practice_topic != topic_key:
            st.session_state.practice_topic = topic_key
            st.session_state.practice_question = choose_practice_question(
                topic_key
            )
            st.session_state.practice_score = None
            st.session_state.show_concepts = False

        if st.button(
            "🎲 New Question",
            use_container_width=True,
        ):
            st.session_state.practice_question = choose_practice_question(
                topic_key
            )
            st.session_state.practice_score = None
            st.session_state.show_concepts = False
            st.rerun()

        question_data = st.session_state.practice_question

        if question_data is None:
            question_data = choose_practice_question(topic_key)
            st.session_state.practice_question = question_data

        if question_data is not None:

            question_text = get_question_text(question_data)
            keywords = get_keywords(question_data)

            st.markdown(
                '<div class="question-box">',
                unsafe_allow_html=True,
            )

            st.markdown("### ❓ Practice Question")
            st.info(question_text)

            st.markdown(
                "</div>",
                unsafe_allow_html=True,
            )

            answer = st.text_area(
                "✍️ Write your answer",
                height=180,
                placeholder="Type your answer here...",
                key="practice_answer",
            )

            col1, col2, col3 = st.columns(3)

            # ------------------------------------------------
            # CHECK ANSWER
            # ------------------------------------------------

            with col1:
                if st.button(
                    "✅ Check Answer",
                    use_container_width=True,
                ):
                    if not answer.strip():
                        st.warning(
                            "⚠️ Please write your answer first."
                        )
                    else:
                        try:
                            score = check_answer(
                                answer,
                                keywords,
                            )

                            st.session_state.practice_score = score

                            if score >= 70:
                                st.success(
                                    f"🎉 Good attempt!\n\n"
                                    f"Concept coverage: {score:.0f}%"
                                )
                            elif score >= 40:
                                st.warning(
                                    f"👍 You are on the right track!\n\n"
                                    f"Concept coverage: {score:.0f}%"
                                )
                            else:
                                st.error(
                                    f"💪 Keep practicing!\n\n"
                                    f"Concept coverage: {score:.0f}%"
                                )

                        except Exception as error:
                            st.error(
                                "Could not check the answer."
                            )
                            st.code(str(error))

            # ------------------------------------------------
            # SKIP QUESTION
            # ------------------------------------------------

            with col2:
                if st.button(
                    "⏭️ Skip Question",
                    use_container_width=True,
                ):
                    st.session_state.practice_question = choose_practice_question(
                        topic_key
                    )
                    st.session_state.practice_score = None
                    st.session_state.show_concepts = False
                    st.rerun()

            # ------------------------------------------------
            # SHOW CONCEPTS
            # ------------------------------------------------

            with col3:
                if st.button(
                    "💡 Show Concepts",
                    use_container_width=True,
                ):
                    st.session_state.show_concepts = True

            if st.session_state.show_concepts:
                st.markdown("### 💡 Key Concepts")

                if keywords:
                    st.write(", ".join(str(k) for k in keywords))
                else:
                    st.info(
                        "No keyword list is available for this question."
                    )

            if st.session_state.practice_score is not None:
                st.markdown("---")
                st.metric(
                    "Last Concept Coverage",
                    f"{st.session_state.practice_score:.0f}%",
                )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "🐍 Python AI Learning Assistant | Python + NLP + Machine Learning"
)
