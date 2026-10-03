import random


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


def choose_topic():
    print()
    print("=" * 65)
    print("                  PRACTICE TOPICS")
    print("=" * 65)
    print("1. Python")
    print("2. OOP")
    print("3. SQL")
    print("4. Machine Learning")
    print("5. NLP")
    print("=" * 65)


def get_topic(choice):
    topics = {
        "1": "python",
        "2": "oop",
        "3": "sql",
        "4": "machine learning",
        "5": "nlp"
    }

    return topics.get(choice)


def check_answer(answer, keywords):
    answer_lower = answer.lower()

    matched = 0

    for keyword in keywords:
        if keyword.lower() in answer_lower:
            matched += 1

    percentage = (matched / len(keywords)) * 100

    return percentage


def practice_topic(topic):
    question_data = random.choice(QUESTIONS[topic])

    print()
    print("=" * 65)
    print("                     PRACTICE QUESTION")
    print("=" * 65)

    print()
    print(question_data["question"])

    print()
    print("Type your answer below.")
    print("Type 'skip' to see the expected concepts.")
    print("Type 'back' to return.")

    answer = input("\nYour Answer:\n").strip()

    if answer.lower() == "back":
        return False

    if answer.lower() == "skip":
        print()
        print("Expected concepts:")
        for keyword in question_data["keywords"]:
            print(f"• {keyword}")
        return True

    score = check_answer(
        answer,
        question_data["keywords"]
    )

    print()
    print("=" * 65)

    if score >= 70:
        print("Good attempt! ✅")
        print(f"Basic concept coverage: {score:.0f}%")

    elif score >= 40:
        print("You are on the right track. 👍")
        print(f"Basic concept coverage: {score:.0f}%")
        print("Try improving your answer.")

    else:
        print("Keep practicing! 💪")
        print(f"Basic concept coverage: {score:.0f}%")
        print("Review the topic and try again.")

    print("=" * 65)

    return True


def start_practice_mode():
    print()
    print("=" * 65)
    print("                    PRACTICE MODE")
    print("=" * 65)

    print()
    print("Practice programming and technical concepts.")
    print()
    print("Commands:")
    print("1 → Python")
    print("2 → OOP")
    print("3 → SQL")
    print("4 → Machine Learning")
    print("5 → NLP")
    print("back → Return to main chatbot")

    while True:

        choose_topic()

        choice = input("\nChoose a topic: ").strip().lower()

        if choice in ["back", "exit", "quit"]:
            print("Returning to main chatbot...")
            break

        topic = get_topic(choice)

        if topic is None:
            print()
            print("Please choose a valid option from 1 to 5.")
            continue

        practice_topic(topic)


if __name__ == "__main__":
    start_practice_mode()