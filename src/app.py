import random
import streamlit as st

from chatbot_engine import get_answer, get_context_answer
from study_planner import find_plan
from practice_mode import QUESTIONS, check_answer


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Python AI Learning Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #f5f7ff 0%, #eef2ff 100%);
    }

    /* Main title */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
        color: #1f2937;
    }

    .subtitle {
        text-align: center;
        font-size: 17px;
        color: #6b7280;
        margin-bottom: 30px;
    }

    /* Feature cards */
    .feature-card {
        background: white;
        padding: 22px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        min-height: 150px;
    }

    .feature-card h3 {
        margin-bottom: 8px;
        color: #111827;
    }

    .feature-card p {
        color: #6b7280;
        font-size: 14px;
    }

    /* Section headings */
    .section-title {
        font-size: 28px;
        font-weight: 700;
        color: #1f2937;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    /* Question box */
    .question-box {
        background: white;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-top: 15px;
        margin-bottom: 20px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: white;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_question" not in st.session_state:
    st.session_state.last_question = None

if "mode" not in st.session_state:
    st.session_state.mode = "chat"

if "practice_question" not in st.session_state:
    st.session_state.practice_question = None

if "practice_topic" not in st.session_state:
    st.session_state.practice_topic = None

if "practice_score" not in st.session_state:
    st.session_state.practice_score = None

if "show_concepts" not in st.session_state:
    st.session_state.show_concepts = False


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## ⚙️ Menu")

    st.markdown("---")

    # Chatbot
    if st.button(
        "💬 Chatbot",
        use_container_width=True
    ):
        st.session_state.mode = "chat"

    # Study Planner
    if st.button(
        "📚 Study Planner",
        use_container_width=True
    ):
        st.session_state.mode = "study"

    # Practice Mode
    if st.button(
        "🎯 Practice Mode",
        use_container_width=True
    ):
        st.session_state.mode = "practice"

        st.session_state.practice_question = None
        st.session_state.practice_score = None
        st.session_state.show_concepts = False

    st.markdown("---")

    # Clear Chat
    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.session_state.last_question = None
        st.rerun()

    st.markdown("---")

    st.markdown("### 💡 Example Questions")

    st.write("• What is Python?")
    st.write("• What is a variable?")
    st.write("• What is a tuple?")
    st.write("• List vs tuple")
    st.write("• What is machine learning?")
    st.write("• Explain decorators")

    st.markdown("---")

    st.caption("🤖 Python AI Learning Assistant")
    st.caption("Learn • Practice • Improve")


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🤖 Python AI Learning Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Learn Python, Machine Learning, NLP and more with your personal AI assistant.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# HOME / CHAT MODE
# =========================================================

if st.session_state.mode == "chat":

    # Feature cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <h3>💬 Ask Questions</h3>
                <p>
                Ask Python and technical questions
                in natural language.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <h3>📚 Study Planner</h3>
                <p>
                Generate structured 30-day
                learning plans.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="feature-card">
                <h3>🎯 Practice Mode</h3>
                <p>
                Practice programming and
                technical concepts.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.markdown(
        '<div class="section-title">💬 Chat with your AI Assistant</div>',
        unsafe_allow_html=True
    )

    # Display old messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(
                message["content"]
            )

    # Chat input
    question = st.chat_input(
        "Ask your Python question..."
    )

    if question:

        # Save user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):

            st.markdown(question)

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

        # Display answer
        with st.chat_message("assistant"):

            st.markdown(answer)

        # Save assistant response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        # Remember question
        st.session_state.last_question = question


# =========================================================
# STUDY PLANNER
# =========================================================

elif st.session_state.mode == "study":

    st.markdown(
        '<div class="section-title">📚 Study Planner</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Create a structured 30-day learning plan."
    )

    st.markdown("---")

    subject = st.selectbox(
        "🎓 Select your subject",
        [
            "Python",
            "Machine Learning",
            "Data Analyst",
            "AI"
        ]
    )

    if st.button(
        "🚀 Generate Study Plan",
        use_container_width=True
    ):

        plan = find_plan(
            f"Create a {subject} study plan"
        )

        if plan:

            st.success(
                f"✅ {plan['title']}"
            )

            st.markdown("### 🎯 Goal")

            st.info(
                plan["goal"]
            )

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("### ⏰ Study Time")

                st.write(
                    plan["daily"]
                )

            with col2:

                st.markdown("### 🚀 Project")

                st.write(
                    plan["project"]
                )

            st.markdown("---")

            st.markdown("### 📖 Topics to Learn")

            for number, topic in enumerate(
                plan["topics"],
                start=1
            ):

                st.write(
                    f"**{number}.** {topic}"
                )

            st.markdown("---")

            st.markdown(
                "### ✍️ Practice Activities"
            )

            for activity in plan["practice"]:

                st.write(
                    f"✅ {activity}"
                )


# =========================================================
# PRACTICE MODE
# =========================================================

elif st.session_state.mode == "practice":

    st.markdown(
        '<div class="section-title">🎯 Practice Mode</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Test your knowledge and improve your technical skills."
    )

    st.markdown("---")

    # Topic selection
    topic = st.selectbox(
        "📚 Choose a topic",
        [
            "Python",
            "OOP",
            "SQL",
            "Machine Learning",
            "NLP"
        ]
    )

    topic_key = topic.lower()

    # Create first question
    if (
        st.session_state.practice_question is None
        or st.session_state.practice_topic != topic_key
    ):

        st.session_state.practice_topic = topic_key

        st.session_state.practice_question = random.choice(
            QUESTIONS[topic_key]
        )

        st.session_state.practice_score = None
        st.session_state.show_concepts = False

    question_data = st.session_state.practice_question

    # Question box
    st.markdown(
        '<div class="question-box">',
        unsafe_allow_html=True
    )

    st.markdown("### ❓ Practice Question")

    st.info(
        question_data["question"]
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    # Answer
    answer = st.text_area(
        "✍️ Write your answer",
        height=180,
        placeholder="Type your answer here..."
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    # -----------------------------------------------------
    # CHECK ANSWER
    # -----------------------------------------------------

    with col1:

        if st.button(
            "✅ Check Answer",
            use_container_width=True
        ):

            if answer.strip() == "":

                st.warning(
                    "⚠️ Please write your answer first."
                )

            else:

                score = check_answer(
                    answer,
                    question_data["keywords"]
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

    # -----------------------------------------------------
    # SKIP
    # -----------------------------------------------------

    with col2:

        if st.button(
            "⏭️ Skip Question",
            use_container_width=True
        ):

            available_questions = QUESTIONS[topic_key]

            current_question = (
                st.session_state.practice_question
            )

            # Make sure next question is different
            if len(available_questions) > 1:

                other_questions = [
                    q for q in available_questions
                    if q != current_question
                ]

                st.session_state.practice_question = random.choice(
                    other_questions
                )

            else:

                st.session_state.practice_question = (
                    current_question
                )

            st.session_state.practice_score = None
            st.session_state.show_concepts = False

            st.rerun()

    # -----------------------------------------------------
    # SHOW CONCEPTS
    # -----------------------------------------------------

    with col3:

        if st.button(
            "💡 Show Concepts",
            use_container_width=True
        ):

            st.session_state.show_concepts = True

    # Show concepts
    if st.session_state.show_concepts:

        st.markdown("---")

        st.markdown(
            "### 💡 Expected Concepts"
        )

        for keyword in question_data["keywords"]:

            st.write(
                f"🔹 {keyword}"
            )

    # Previous score
    if st.session_state.practice_score is not None:

        st.markdown("---")

        st.markdown("### 📊 Your Result")

        score = st.session_state.practice_score

        st.progress(
            int(score)
        )

        st.write(
            f"**Concept Coverage: {score:.0f}%**"
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#6b7280; padding:15px;">
        🤖 <b>Python AI Learning Assistant</b><br>
        Learn • Practice • Build • Improve
    </div>
    """,
    unsafe_allow_html=True
)