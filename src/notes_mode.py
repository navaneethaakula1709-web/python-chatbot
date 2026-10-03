NOTES = {
    "python": {
        "title": "Python Programming",
        "definition": "Python is a high-level, interpreted, general-purpose programming language.",
        "concepts": [
            "Variables and data types",
            "Operators",
            "Conditional statements",
            "Loops",
            "Functions",
            "Data structures",
            "Object-Oriented Programming",
            "Exception handling",
            "File handling",
            "Modules and packages"
        ],
        "example": '''name = "Python"
age = 20

print("Name:", name)
print("Age:", age)''',
        "applications": [
            "Web development",
            "Data Science",
            "Machine Learning",
            "Artificial Intelligence",
            "Automation",
            "Scripting"
        ],
        "key_points": [
            "Python uses simple and readable syntax.",
            "Python is dynamically typed.",
            "Python supports Object-Oriented Programming.",
            "Python has a large standard library and ecosystem."
        ]
    },

    "oop": {
        "title": "Object-Oriented Programming",
        "definition": "OOP is a programming approach that organizes programs using classes and objects.",
        "concepts": [
            "Class",
            "Object",
            "Constructor",
            "Inheritance",
            "Polymorphism",
            "Encapsulation",
            "Abstraction"
        ],
        "example": '''class Student:

    def __init__(self, name):
        self.name = name

student = Student("Alex")

print(student.name)''',
        "applications": [
            "Large software applications",
            "Banking systems",
            "Management systems",
            "Game development",
            "Enterprise applications"
        ],
        "key_points": [
            "A class is a blueprint.",
            "An object is an instance of a class.",
            "Inheritance allows code reuse.",
            "Encapsulation protects data and behavior."
        ]
    },

    "machine learning": {
        "title": "Machine Learning",
        "definition": "Machine Learning is a branch of AI that enables computers to learn patterns from data and make predictions or decisions.",
        "concepts": [
            "Supervised Learning",
            "Unsupervised Learning",
            "Reinforcement Learning",
            "Classification",
            "Regression",
            "Clustering",
            "Training data",
            "Testing data",
            "Model evaluation"
        ],
        "example": '''from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

model = LinearRegression()
model.fit(X_train, y_train)

prediction = model.predict(X_test)''',
        "applications": [
            "Recommendation systems",
            "Fraud detection",
            "Spam detection",
            "Image classification",
            "Prediction systems"
        ],
        "key_points": [
            "Machine Learning learns patterns from data.",
            "Data quality affects model performance.",
            "Models must be evaluated using suitable metrics.",
            "Overfitting can reduce performance on unseen data."
        ]
    },

    "nlp": {
        "title": "Natural Language Processing",
        "definition": "NLP is a field of AI that enables computers to process and understand human language.",
        "concepts": [
            "Tokenization",
            "Stop-word removal",
            "Stemming",
            "Lemmatization",
            "Text classification",
            "Sentiment analysis",
            "Named Entity Recognition",
            "Chatbots"
        ],
        "example": '''from nltk.tokenize import word_tokenize

text = "Python is easy to learn."

tokens = word_tokenize(text)

print(tokens)''',
        "applications": [
            "Chatbots",
            "Voice assistants",
            "Sentiment analysis",
            "Machine translation",
            "Text classification",
            "Search systems"
        ],
        "key_points": [
            "NLP works with human language data.",
            "Text preprocessing is an important step.",
            "Tokenization divides text into smaller units.",
            "Lemmatization converts words to meaningful base forms."
        ]
    },

    "data science": {
        "title": "Data Science",
        "definition": "Data Science combines programming, statistics and analytical techniques to extract useful insights from data.",
        "concepts": [
            "Data collection",
            "Data cleaning",
            "Exploratory Data Analysis",
            "Statistics",
            "Data visualization",
            "Feature engineering",
            "Machine Learning"
        ],
        "example": '''import pandas as pd

data = pd.read_csv("data.csv")

print(data.head())
print(data.describe())''',
        "applications": [
            "Business analytics",
            "Healthcare analytics",
            "Financial analysis",
            "Marketing analytics",
            "Recommendation systems"
        ],
        "key_points": [
            "Data cleaning improves data quality.",
            "EDA helps understand patterns in data.",
            "Visualization makes insights easier to understand.",
            "Machine Learning can be used as part of Data Science."
        ]
    }
}


def show_notes(notes):
    print()
    print("=" * 70)
    print(f"NOTES: {notes['title']}")
    print("=" * 70)

    print()
    print("1. Definition")
    print(notes["definition"])

    print()
    print("2. Important Concepts")
    for concept in notes["concepts"]:
        print(f"• {concept}")

    print()
    print("3. Example")
    print("```python")
    print(notes["example"])
    print("```")

    print()
    print("4. Applications")
    for application in notes["applications"]:
        print(f"• {application}")

    print()
    print("5. Key Points")
    for point in notes["key_points"]:
        print(f"• {point}")

    print()
    print("=" * 70)


def find_notes(question):
    question = question.lower()

    if "oop" in question or "object oriented" in question:
        return NOTES["oop"]

    if "machine learning" in question or "ml" in question:
        return NOTES["machine learning"]

    if "nlp" in question or "natural language" in question:
        return NOTES["nlp"]

    if "data science" in question:
        return NOTES["data science"]

    if "python" in question:
        return NOTES["python"]

    return None


def start_notes_mode():
    print()
    print("=" * 70)
    print("                     NOTES MODE")
    print("=" * 70)

    print()
    print("You can ask:")
    print("• Give me notes on Python")
    print("• Explain Python OOP in detail")
    print("• Give me notes on Machine Learning")
    print("• Give me interview notes on NLP")
    print("• Explain Data Science")
    print()
    print("Type 'back' to return to the main chatbot.")

    while True:
        question = input("\nNotes Mode > ").strip()

        if question.lower() in ["back", "exit", "quit"]:
            print("Returning to main chatbot...")
            break

        notes = find_notes(question)

        if notes:
            show_notes(notes)
        else:
            print()
            print("Available topics:")
            print("1. Python")
            print("2. OOP")
            print("3. Machine Learning")
            print("4. NLP")
            print("5. Data Science")


if __name__ == "__main__":
    start_notes_mode()