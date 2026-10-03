import random
import streamlit as st


QUESTIONS = {
    "python": [
        {
            "question": "Write a Python program to check whether a number is even or odd.",
            "keywords": ["%", "if", "else"]
        },
        {
            "question": "Write a Python program to find the largest of three numbers.",
            "keywords": ["if", "elif", "else"]
        },
        {
            "question": "Write a Python program to calculate the factorial of a number.",
            "keywords": ["factorial", "for"]
        },
        {
            "question": "Write a Python program to reverse a string.",
            "keywords": ["[::-1]"]
        },
        {
            "question": "Write a Python program to check whether a number is prime.",
            "keywords": ["for", "if", "%"]
        }
    ],

    "oop": [
        {
            "question": "Create a Python class named Student with name and age attributes.",
            "keywords": ["class", "__init__", "self"]
        },
        {
            "question": "Write a Python example demonstrating inheritance.",
            "keywords": ["class", "inherit"]
        }
    ],

    "sql": [
        {
            "question": "Write an SQL query to display all records from a Students table.",
            "keywords": ["select", "from", "students"]
        },
        {
            "question": "Write an SQL query to find students whose age is greater than 18.",
            "keywords": ["select", "where", "age"]
        }
    ],

    "machine learning": [
        {
            "question": "What is the difference between supervised and unsupervised learning?",
            "keywords": ["supervised", "unsupervised"]
        },
        {
            "question": "What is overfitting in Machine Learning?",
            "keywords": ["training", "unseen", "data"]
        }
    ],

    "nlp": [
        {
            "question": "What is tokenization in NLP?",
            "keywords": ["text", "tokens", "words"]
        },
        {
            "question": "What is the purpose of removing stop words?",
            "keywords": ["common", "words", "text"]
        }
    ]
}


def check_answer(answer, keywords):

    answer_lower = answer.lower()

    matched = 0

    for keyword in keywords:
        if keyword.lower() in answer_lower:
            matched += 1

    percentage = (matched / len(keywords)) * 100

    return percentage


def practice_mode():

    st.title("📝 Practice Mode")

    st.write(
        "Practice programming and technical concepts."
    )

    # Topic selection
    topic = st.selectbox(
        "Choose a topic",
        [
            "Python",
            "OOP",
            "SQL",
            "Machine Learning",
            "NLP"
        ]
    )

    topic_key = topic.lower()

    # Generate question
    if "practice_question" not in st.session_state:
        st.session_state.practice_question = random.choice(
            QUESTIONS[topic_key]
        )

    # Change question when topic changes
    if st.session_state.get("practice_topic") != topic_key:

        st.session_state.practice_topic = topic_key

        st.session_state.practice_question = random.choice(
            QUESTIONS[topic_key]
        )

    question_data = st.session_state.practice_question

    st.markdown("---")

    st.subheader("💡 Practice Question")

    st.write(question_data["question"])

    st.markdown("---")

    # Answer box
    answer = st.text_area(
        "✍️ Your Answer",
        height=180,
        placeholder="Type your answer here..."
    )

    # Buttons
    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("✅ Check Answer"):

            if answer.strip() == "":
                st.warning("Please enter your answer first.")

            else:

                score = check_answer(
                    answer,
                    question_data["keywords"]
                )

                st.session_state.practice_score = score

    with col2:

        if st.button("⏭️ Skip Question"):

            st.session_state.practice_question = random.choice(
                QUESTIONS[topic_key]
            )

            st.session_state.practice_score = None

            st.rerun()

    with col3:

        if st.button("🔄 New Question"):

            st.session_state.practice_question = random.choice(
                QUESTIONS[topic_key]
            )

            st.session_state.practice_score = None

            st.rerun()

    # Show result
    if "practice_score" in st.session_state:

        score = st.session_state.practice_score

        if score is not None:

            st.markdown("---")

            st.subheader("📊 Result")

            st.write(
                f"Basic concept coverage: **{score:.0f}%**"
            )

            if score >= 70:

                st.success(
                    "Good attempt! ✅"
                )

            elif score >= 40:

                st.warning(
                    "You are on the right track. 👍"
                )

            else:

                st.error(
                    "Keep practicing! 💪"
                )

    # Expected concepts
    if st.button("💡 Show Expected Concepts"):

        st.markdown("### Expected Concepts")

        for keyword in question_data["keywords"]:

            st.write(f"• {keyword}")