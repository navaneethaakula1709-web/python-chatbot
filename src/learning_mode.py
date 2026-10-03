# ============================================
# PYTHON LEARNING MODE
# Python QA Chatbot
# ============================================


TOPICS = [

    {
        "name": "Python Basics",
        "lesson": """
Python is a high-level, interpreted programming language.

Important basics:
• Variables store values.
• Data types define the type of value.
• input() gets information from the user.
• print() displays output.
• Comments are written using #.

Example:

name = input("Enter your name: ")
print("Hello", name)
"""
    },

    {
        "name": "Variables and Data Types",
        "lesson": """
A variable is a name used to store a value.

Common Python data types:

int      → Whole numbers
float    → Decimal numbers
str      → Text
bool     → True or False
list     → Ordered collection
tuple    → Ordered immutable collection
set      → Unordered unique collection
dict     → Key-value pairs

Example:

name = "Python"
age = 20
height = 5.8
student = True
"""
    },

    {
        "name": "Operators",
        "lesson": """
Operators are symbols used to perform operations.

Arithmetic:
+   Addition
-   Subtraction
*   Multiplication
/   Division
%   Modulus
//  Floor division
**  Power

Comparison:
>   <   >=   <=   ==   !=

Logical:
and
or
not

Example:

a = 10
b = 5

print(a + b)
print(a > b)
"""
    },

    {
        "name": "Conditional Statements",
        "lesson": """
Conditional statements allow Python to make decisions.

Main statements:

if
elif
else

Example:

age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Not an adult")
"""
    },

    {
        "name": "Loops",
        "lesson": """
Loops are used to repeat a block of code.

Python has:

1. for loop
2. while loop

Example:

for i in range(1, 6):
    print(i)

This prints numbers from 1 to 5.
"""
    },

    {
        "name": "Functions",
        "lesson": """
A function is a reusable block of code.

A function is created using def.

Example:

def greet(name):
    print("Hello", name)

greet("Python")

Functions can accept parameters and return values.
"""
    },

    {
        "name": "Data Structures",
        "lesson": """
Python provides several important data structures.

List:
numbers = [1, 2, 3]

Tuple:
numbers = (1, 2, 3)

Set:
numbers = {1, 2, 3}

Dictionary:
student = {
    "name": "Alex",
    "age": 20
}

Each structure is useful for different types of data.
"""
    },

    {
        "name": "Object-Oriented Programming",
        "lesson": """
Object-Oriented Programming uses classes and objects.

Important OOP concepts:

• Class
• Object
• Constructor
• Inheritance
• Polymorphism
• Encapsulation
• Abstraction

Example:

class Student:

    def __init__(self, name):
        self.name = name

student = Student("Alex")

print(student.name)
"""
    },

    {
        "name": "File Handling",
        "lesson": """
File handling allows Python to work with files.

Common modes:

r → Read
w → Write
a → Append

Example:

with open("data.txt", "r") as file:
    content = file.read()

print(content)
"""
    },

    {
        "name": "Python Libraries",
        "lesson": """
Libraries provide ready-made functionality.

Important libraries:

NumPy
→ Numerical computing

Pandas
→ Data analysis

Matplotlib
→ Data visualization

OpenCV
→ Computer vision

Scikit-learn
→ Machine learning

MediaPipe
→ Computer vision and gesture-related tasks
"""
    },

    {
        "name": "Data Science",
        "lesson": """
Data Science involves collecting, processing, analyzing and interpreting data.

Important concepts:

• Data collection
• Data cleaning
• Data analysis
• Data visualization
• Statistics
• Machine learning

Popular Python libraries:
NumPy
Pandas
Matplotlib
Seaborn
"""
    },

    {
        "name": "Machine Learning",
        "lesson": """
Machine Learning allows computers to learn patterns from data.

Main types:

1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning

Examples of algorithms:

• Linear Regression
• Logistic Regression
• Decision Tree
• Random Forest
• KNN
• SVM
• K-Means
"""
    },

    {
        "name": "NLP",
        "lesson": """
NLP stands for Natural Language Processing.

It allows computers to process human language.

Common NLP tasks:

• Tokenization
• Stop-word removal
• Stemming
• Lemmatization
• Text classification
• Sentiment analysis
• Chatbots

Your chatbot itself uses NLP concepts.
"""
    },

    {
        "name": "Python Projects",
        "lesson": """
Projects help you apply programming concepts.

Examples:

• Student Management System
• Resume Screening System
• Sign Language Recognition
• Python QA Chatbot
• Data Analysis Dashboard
• Machine Learning Prediction System

A good project usually contains:

Problem
→ Data
→ Processing
→ Model/Logic
→ Output
→ User interaction
"""
    }
]


def show_learning_topics():

    print()
    print("=" * 65)
    print("                 PYTHON LEARNING PATH")
    print("=" * 65)

    for index, topic in enumerate(TOPICS, start=1):
        print(f"{index}. {topic['name']}")

    print("=" * 65)


def show_topic(index):

    if index < 0 or index >= len(TOPICS):
        return

    topic = TOPICS[index]

    print()
    print("=" * 65)
    print(f"TOPIC {index + 1}: {topic['name']}")
    print("=" * 65)

    print(topic["lesson"])

    print("=" * 65)


def topic_quiz(index):

    quizzes = {

        0: [
            (
                "Which function is used to display output?",
                ["A. input()", "B. print()", "C. output()", "D. display()"],
                "B"
            ),
            (
                "Which symbol is used for comments?",
                ["A. //", "B. #", "C. --", "D. /*"],
                "B"
            )
        ],

        1: [
            (
                "Which data type stores True or False?",
                ["A. int", "B. str", "C. bool", "D. float"],
                "C"
            ),
            (
                "Which data type stores key-value pairs?",
                ["A. list", "B. tuple", "C. set", "D. dict"],
                "D"
            )
        ],

        2: [
            (
                "Which operator gives the remainder?",
                ["A. /", "B. //", "C. %", "D. **"],
                "C"
            ),
            (
                "Which operator is used for power?",
                ["A. ^", "B. **", "C. //", "D. %%"],
                "B"
            )
        ],

        3: [
            (
                "Which keyword is used for a condition?",
                ["A. if", "B. check", "C. condition", "D. when"],
                "A"
            ),
            (
                "Which keyword checks another condition?",
                ["A. otherwise", "B. elif", "C. elseif", "D. next"],
                "B"
            )
        ],

        4: [
            (
                "Which loop is commonly used with range()?",
                ["A. for", "B. if", "C. class", "D. try"],
                "A"
            ),
            (
                "Which loop runs while a condition is true?",
                ["A. for", "B. while", "C. repeat", "D. loop"],
                "B"
            )
        ]
    }

    questions = quizzes.get(index)

    if not questions:
        print()
        print("Quiz for this topic will be added soon.")
        return

    score = 0

    print()
    print("=" * 65)
    print(f"QUIZ: {TOPICS[index]['name']}")
    print("=" * 65)

    for number, question in enumerate(questions, start=1):

        print()
        print(f"{number}. {question[0]}")

        for option in question[1]:
            print(option)

        answer = input("Your answer: ").strip().upper()

        if answer == question[2]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. Correct answer: {question[2]}")

    print()
    print(f"Your score: {score}/{len(questions)}")


def start_learning_mode():

    current_topic = 0

    print()
    print("=" * 65)
    print("                    LEARNING MODE")
    print("=" * 65)

    print()
    print("Welcome to Python Learning Mode!")
    print()
    print("Commands:")
    print("  topics  → Show all topics")
    print("  start   → Start learning")
    print("  next    → Go to next topic")
    print("  quiz    → Take a quiz")
    print("  back    → Return to main chatbot")
    print()

    show_learning_topics()

    while True:

        command = input("\nLearning Mode > ").strip().lower()

        if command == "back":
            print("Returning to main chatbot...")
            break

        elif command == "topics":
            show_learning_topics()

        elif command == "start":
            current_topic = 0
            show_topic(current_topic)

        elif command == "next":

            if current_topic < len(TOPICS) - 1:
                current_topic += 1
                show_topic(current_topic)
            else:
                print("You have completed all learning topics!")

        elif command == "quiz":
            topic_quiz(current_topic)

        elif command.isdigit():

            number = int(command)

            if 1 <= number <= len(TOPICS):
                current_topic = number - 1
                show_topic(current_topic)
            else:
                print("Invalid topic number.")

        else:
            print()
            print("Available commands:")
            print("topics")
            print("start")
            print("next")
            print("quiz")
            print("back")


if __name__ == "__main__":
    start_learning_mode()