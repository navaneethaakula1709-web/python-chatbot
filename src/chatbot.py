from chatbot_engine import get_answer, get_context_answer, find_topic
from conversation_manager import ConversationManager
from problem_solver import get_program
from code_explainer import explain_code
from learning_mode import start_learning_mode
from project_mode import start_project_mode
from career_mode import start_career_mode
from study_planner import start_study_planner
from notes_mode import start_notes_mode
from practice_mode import start_practice_mode


def show_doodle():
    print()
    print("             🐍")
    print("        .-----------.")
    print("       /   PYTHON    \\")
    print("      /    CHATBOT    \\")
    print("     '-----------------'")
    print("          |  |  |")
    print("       Python + NLP + ML")
    print()


def show_welcome():
    print("=" * 65)
    print("                 PYTHON QA CHATBOT")
    print("=" * 65)
    print()
    print("Ask me questions about:")
    print()
    print("1. Python Basics")
    print("2. Control Statements")
    print("3. Data Structures")
    print("4. Functions")
    print("5. OOP")
    print("6. Exceptions")
    print("7. Files and Modules")
    print("8. Advanced Python")
    print("9. Python Libraries")
    print("10. Data Science")
    print("11. Machine Learning")
    print("12. NLP")
    print("13. Projects")
    print()
    print("Special commands:")
    print("  help       → Show commands")
    print("  categories → Show categories")
    print("  history    → Show conversation history")
    print("  clear      → Clear conversation memory")
    print("  interview  → Start Python interview mode")
    print("  quiz       → Start Python quiz")
    print("  exit       → Exit chatbot")
    print()
    print("=" * 65)


INTERVIEW_QUESTIONS = [
    (
        "What is Python?",
        "Python is a high-level, interpreted, general-purpose programming language."
    ),
    (
        "What are variables in Python?",
        "Variables are names used to store values in memory."
    ),
    (
        "What is a list?",
        "A list is an ordered and mutable collection of elements."
    ),
    (
        "What is a tuple?",
        "A tuple is an ordered and immutable collection of elements."
    ),
    (
        "What is a dictionary?",
        "A dictionary stores data in key-value pairs."
    ),
    (
        "What is a function?",
        "A function is a reusable block of code designed to perform a specific task."
    ),
    (
        "What is OOP?",
        "Object-Oriented Programming is a programming approach based on classes and objects."
    ),
    (
        "What is inheritance?",
        "Inheritance allows one class to acquire properties and methods from another class."
    ),
    (
        "What is polymorphism?",
        "Polymorphism means the same interface or method name can behave differently in different contexts."
    ),
    (
        "What is encapsulation?",
        "Encapsulation combines data and methods inside a class and controls access to the data."
    ),
    (
        "What is exception handling?",
        "Exception handling manages runtime errors using mechanisms such as try and except."
    ),
    (
        "What is NumPy?",
        "NumPy is a Python library mainly used for numerical computing and arrays."
    ),
    (
        "What is Pandas?",
        "Pandas is a Python library used for data manipulation and analysis."
    ),
    (
        "What is machine learning?",
        "Machine learning is a field where systems learn patterns from data to make predictions or decisions."
    ),
    (
        "What is NLP?",
        "Natural Language Processing allows computers to process and understand human language."
    )
]


QUIZ_QUESTIONS = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. define", "D. fun"],
        "answer": "B"
    },
    {
        "question": "Which data type is mutable?",
        "options": ["A. Tuple", "B. String", "C. List", "D. Integer"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. --"],
        "answer": "C"
    },
    {
        "question": "Which library is mainly used for numerical computing?",
        "options": ["A. NumPy", "B. Flask", "C. Django", "D. Tkinter"],
        "answer": "A"
    },
    {
        "question": "Which collection stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "D"
    },
    {
        "question": "Which keyword is used to handle exceptions?",
        "options": ["A. error", "B. try", "C. catch", "D. handle"],
        "answer": "B"
    },
    {
        "question": "Which library is commonly used for data analysis?",
        "options": ["A. Pandas", "B. Turtle", "C. Pygame", "D. OS"],
        "answer": "A"
    },
    {
        "question": "What does NLP stand for?",
        "options": [
            "A. Natural Language Processing",
            "B. Neural Learning Program",
            "C. Natural Logic Programming",
            "D. Network Language Protocol"
        ],
        "answer": "A"
    },
    {
        "question": "Which algorithm can be used for classification?",
        "options": [
            "A. Decision Tree",
            "B. Linear Search",
            "C. Bubble Sort",
            "D. Binary Search"
        ],
        "answer": "A"
    },
    {
        "question": "Which method is used to add an item to a list?",
        "options": ["A. add()", "B. insert()", "C. append()", "D. push()"],
        "answer": "C"
    }
]


def start_interview():

    print()
    print("=" * 65)
    print("                 PYTHON INTERVIEW MODE")
    print("=" * 65)
    print()
    print("Type 'answer' if you want to see the expected answer.")
    print("Type 'exit' to leave interview mode.")
    print()

    score = 0

    for index, item in enumerate(INTERVIEW_QUESTIONS, start=1):

        print(f"Question {index}: {item[0]}")

        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == "exit":
            print("Exiting interview mode...")
            return

        if user_answer.lower() == "answer":
            print()
            print("Expected answer:")
            print(item[1])
            print()
            continue

        if len(user_answer) >= 10:
            score += 1
            print("Answer recorded.")
        else:
            print("Try to give a more detailed answer.")

        print()

    print("=" * 65)
    print("Interview completed!")
    print(f"Detailed answers given: {score}/{len(INTERVIEW_QUESTIONS)}")
    print("=" * 65)


def start_quiz():

    print()
    print("=" * 65)
    print("                    PYTHON QUIZ")
    print("=" * 65)
    print()

    score = 0

    for index, item in enumerate(QUIZ_QUESTIONS, start=1):

        print(f"Question {index}: {item['question']}")

        for option in item["options"]:
            print(option)

        answer = input("Your answer: ").strip().upper()

        if answer == "EXIT":
            print("Exiting quiz...")
            return

        if answer == item["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. Correct answer: {item['answer']}")

        print()

    percentage = (score / len(QUIZ_QUESTIONS)) * 100

    print("=" * 65)
    print("Quiz completed!")
    print(f"Score: {score}/{len(QUIZ_QUESTIONS)}")
    print(f"Percentage: {percentage:.1f}%")
    print("=" * 65)


def show_categories():

    print()
    print("=" * 50)
    print("                 CATEGORIES")
    print("=" * 50)

    categories = [
        "Python Basics",
        "Control Statements",
        "Data Structures",
        "Functions",
        "OOP",
        "Exceptions",
        "Files and Modules",
        "Advanced Python",
        "Python Libraries",
        "Data Science",
        "Machine Learning",
        "NLP",
        "Database and Web",
        "Projects",
        "Programming Problems"
    ]

    for number, category in enumerate(categories, start=1):
        print(f"{number}. {category}")

    print("=" * 50)


def show_help():
    print()
    print("=" * 70)
    print("                         HELP MENU")
    print("=" * 70)

    print()
    print("NORMAL QUESTIONS")
    print("• What is Python?")
    print("• Explain OOP")
    print("• What is Machine Learning?")
    print("• What is NLP?")
    print("• Explain Random Forest")

    print()
    print("PROGRAMMING")
    print("• Give me code for factorial")
    print("• Write a prime number program")
    print("• Give me code for palindrome")
    print("• Give me code for Fibonacci")

    print()
    print("LEARNING MODES")
    print("• learn     → Python Learning Mode")
    print("• quiz      → Python Quiz Mode")
    print("• interview → Interview Preparation")

    print()
    print("PROJECT & CAREER")
    print("• project   → Project Recommendation & Guidance")
    print("• career    → Career Guidance & Roadmaps")
    print("• study     → Study Planner")

    print()
    print("STUDY & PRACTICE")
    print("• notes     → Technical Notes & Documentation")
    print("• practice  → Coding & Technical Practice")

    print()
    print("OTHER COMMANDS")
    print("• categories → Show available categories")
    print("• history    → Show conversation history")
    print("• clear      → Clear conversation history")
    print("• help       → Show this help menu")
    print("• exit       → Close chatbot")

    print()
    print("=" * 70)


def start_chatbot():

    manager = ConversationManager()

    show_doodle()
    show_welcome()

    while True:

        try:
            user_question = input("\nYou: ").strip()

        except KeyboardInterrupt:
            print("\n\nChatbot closed.")
            break

        if not user_question:
            print("Bot: Please enter a question.")
            continue

        command = user_question.lower()

        # ------------------------------------------
        # BASIC COMMANDS
        # ------------------------------------------

        if command in ["exit", "quit", "bye"]:
            print()
            print("Bot: Goodbye! Keep learning Python! 🐍")
            break

        if command == "help":
            show_help()
            continue

        if command == "categories":
            show_categories()
            continue

        if command == "history":
            history = manager.get_history()

            if not history:
                print()
                print("Bot: No conversation history yet.")
            else:
                print()
                print("=" * 60)
                print("CONVERSATION HISTORY")
                print("=" * 60)

                for index, item in enumerate(history, start=1):
                    print()
                    print(f"{index}.")
                    print(f"You: {item['question']}")
                    print(f"Category: {item['category']}")
                    print(f"Bot: {item['answer']}")

                print()
                print("=" * 60)

            continue

        if command == "clear":
            manager.clear_history()
            print()
            print("Bot: Conversation memory cleared.")
            continue

        # ------------------------------------------
        # MODES
        # ------------------------------------------

        if command in ["practice", "practice mode"]:
            start_practice_mode()
            continue

        if command in ["notes", "notes mode", "documentation"]:
            start_notes_mode()
            continue

        if command in ["study", "study planner", "study mode"]:
            start_study_planner()
            continue

        if command in ["career", "careers", "career mode"]:
            start_career_mode()
            continue

        if command in ["project", "projects", "project mode"]:
            start_project_mode()
            continue

        if command == "interview":
            start_interview()
            continue

        if command == "quiz":
            start_quiz()
            continue

        if command in ["learn", "learning", "learning mode"]:
            start_learning_mode()
            continue

        # ------------------------------------------
        # FIND THE LAST REAL TOPIC
        # ------------------------------------------
        # Follow-up questions are also stored in history.
        # Search backwards until we find a question that
        # contains a known chatbot topic.

        history = manager.get_history()
        context_question = None

        for item in reversed(history):

            previous_question = item.get("question", "")

            if find_topic(previous_question) is not None:
                context_question = previous_question
                break

        # ------------------------------------------
        # FOLLOW-UP REQUEST TYPES
        # ------------------------------------------

        context_words = [
            "syntax",
            "how to write",
            "give example",
            "give me example",
            "show example",
            "show me an example",
            "real world example",
            "code",
            "give code",
            "give me code",
            "show code",
            "show me code",
            "write code",
            "program",
            "explain it",
            "explain this",
            "how does it work",
            "why is it useful",
            "why is it important",
            "advantages"
        ]

        is_context_request = any(
            word in command
            for word in context_words
        )

        # ------------------------------------------
        # CONTEXT / FOLLOW-UP HANDLING
        # ------------------------------------------
        # Important:
        # Even if the current question contains a topic
        # such as "what is list syntax?", it can still be
        # a follow-up because it asks for syntax.
        #
        # But a normal new question such as:
        # "what is dictionary?"
        # is NOT treated as a follow-up.

        if context_question and is_context_request:

            context_result = get_context_answer(
                user_question,
                context_question
            )

            if context_result:

                answer = context_result["answer"]

                print()
                print("Bot:")
                print(answer)

                manager.add_conversation(
                    user_question,
                    context_result.get("category", "General"),
                    answer
                )

                continue

                # ------------------------------------------
        # CODE EXPLANATION
        # ------------------------------------------

        explanation_words = [
            "explain this code",
            "explain the code",
            "explain code"
        ]

        if any(word in command for word in explanation_words):

            history = manager.get_history()

            if history:

                last_item = history[-1]

                code_to_explain = last_item.get("answer", "")

                explanation_result = explain_code(code_to_explain)

                if explanation_result:

                    answer = explanation_result["answer"]

                    print()
                    print("Bot:")
                    print(answer)

                    manager.add_conversation(
                        user_question,
                        explanation_result.get("category", "General"),
                        answer
                    )

                    continue

        # ------------------------------------------
        # PROGRAMMING PROBLEM SOLVER
        # ------------------------------------------

        program_result = get_program(user_question)

        if program_result:

            answer = program_result["answer"]

            print()
            print("Bot:")
            print(answer)

            manager.add_conversation(
                user_question,
                program_result.get("category", "Programming Problems"),
                answer
            )

            continue

        # ------------------------------------------
        # NORMAL CHATBOT
        # ------------------------------------------

        result = get_answer(user_question)

        answer = result["answer"]

        print()
        print("Bot:")
        print(answer)

        manager.add_conversation(
            user_question,
            result.get("category", "General"),
            answer
        )


if __name__ == "__main__":
    start_chatbot()
