STUDY_PLANS = {
    "python": {
        "title": "Python 30-Day Study Plan",
        "goal": "Build strong Python programming fundamentals.",
        "topics": [
            "Python basics and syntax",
            "Variables and data types",
            "Operators",
            "if, elif and else",
            "for and while loops",
            "Lists, tuples, sets and dictionaries",
            "Functions",
            "Recursion",
            "OOP concepts",
            "File handling",
            "Exception handling",
            "Modules and packages",
            "Practice programming problems",
            "Build a Python project"
        ],
        "daily": "1–2 hours per day",
        "practice": [
            "Solve 2–3 programming problems",
            "Write code without copying",
            "Debug your own errors",
            "Review previous topics"
        ],
        "project": "Student Management System or Expense Tracker"
    },

    "machine learning": {
        "title": "Machine Learning 30-Day Study Plan",
        "goal": "Learn ML fundamentals and build beginner-level ML projects.",
        "topics": [
            "Python for ML",
            "NumPy",
            "Pandas",
            "Data visualization",
            "Statistics basics",
            "Data preprocessing",
            "Train-test split",
            "Linear Regression",
            "Logistic Regression",
            "Decision Tree",
            "Random Forest",
            "KNN",
            "SVM",
            "K-Means",
            "Model evaluation",
            "Overfitting and underfitting",
            "Feature engineering",
            "ML project development"
        ],
        "daily": "1–2 hours per day",
        "practice": [
            "Practice with small datasets",
            "Implement algorithms using Scikit-learn",
            "Compare model performance",
            "Explain each model in your own words"
        ],
        "project": "Student Performance Prediction or Customer Churn Prediction"
    },

    "data analyst": {
        "title": "Data Analyst 30-Day Study Plan",
        "goal": "Build the core skills required for beginner data analysis.",
        "topics": [
            "Excel basics",
            "Python basics",
            "NumPy",
            "Pandas",
            "Data cleaning",
            "Missing values",
            "Data filtering",
            "Data aggregation",
            "SQL basics",
            "SQL queries",
            "Statistics",
            "Matplotlib",
            "Seaborn",
            "Power BI basics",
            "Dashboard creation",
            "Data analysis project"
        ],
        "daily": "1–2 hours per day",
        "practice": [
            "Analyze CSV datasets",
            "Write SQL queries",
            "Create charts",
            "Find useful patterns in data",
            "Explain your findings"
        ],
        "project": "Sales Data Analysis Dashboard"
    },

    "ai": {
        "title": "AI 30-Day Study Plan",
        "goal": "Build a foundation in Artificial Intelligence and related technologies.",
        "topics": [
            "Python",
            "NumPy and Pandas",
            "Statistics basics",
            "Machine Learning",
            "Deep Learning basics",
            "Neural Networks",
            "NLP basics",
            "Computer Vision basics",
            "Chatbots",
            "Generative AI basics",
            "AI project architecture",
            "Model evaluation",
            "AI project development"
        ],
        "daily": "1–2 hours per day",
        "practice": [
            "Study one concept daily",
            "Implement small examples",
            "Read model outputs",
            "Build mini projects"
        ],
        "project": "AI Question Answering Chatbot"
    }
}


def show_plan(plan):
    print()
    print("=" * 70)
    print(plan["title"])
    print("=" * 70)

    print()
    print("Goal:")
    print(plan["goal"])

    print()
    print("Recommended Study Time:")
    print(plan["daily"])

    print()
    print("Topics to Learn:")

    for number, topic in enumerate(plan["topics"], start=1):
        print(f"{number}. {topic}")

    print()
    print("Practice Activities:")

    for activity in plan["practice"]:
        print(f"• {activity}")

    print()
    print("Recommended Project:")
    print(plan["project"])

    print()
    print("=" * 70)


def find_plan(question):
    question = question.lower()

    if "python" in question:
        return STUDY_PLANS["python"]

    if "machine learning" in question or "ml" in question:
        return STUDY_PLANS["machine learning"]

    if "data analyst" in question or "data analysis" in question:
        return STUDY_PLANS["data analyst"]

    if "ai" in question or "artificial intelligence" in question:
        return STUDY_PLANS["ai"]

    return None


def start_study_planner():
    print()
    print("=" * 70)
    print("                    STUDY PLANNER MODE")
    print("=" * 70)

    print()
    print("You can ask:")
    print("• Create a Python study plan")
    print("• Give me a 30 day ML roadmap")
    print("• Create a Data Analyst learning plan")
    print("• Give me an AI study plan")
    print()
    print("Type 'back' to return to the main chatbot.")

    while True:
        question = input("\nStudy Planner > ").strip()

        if question.lower() in ["back", "exit", "quit"]:
            print("Returning to main chatbot...")
            break

        plan = find_plan(question)

        if plan:
            show_plan(plan)
        else:
            print()
            print("Available study plans:")
            print("1. Python")
            print("2. Machine Learning")
            print("3. Data Analyst")
            print("4. AI")


if __name__ == "__main__":
    start_study_planner()
    