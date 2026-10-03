CAREERS = {
    "data analyst": {
        "title": "Data Analyst Career Path",
        "skills": [
            "Python basics",
            "SQL",
            "Excel",
            "Pandas and NumPy",
            "Data cleaning",
            "Statistics",
            "Data visualization",
            "Power BI or Tableau",
            "Basic machine learning"
        ],
        "roadmap": [
            "Learn Python fundamentals",
            "Learn SQL",
            "Learn Excel",
            "Learn Pandas and NumPy",
            "Learn statistics",
            "Practice data cleaning",
            "Learn visualization",
            "Build data analysis projects",
            "Create a portfolio",
            "Prepare for interviews"
        ],
        "projects": [
            "Sales Data Analysis",
            "Student Performance Analysis",
            "Customer Churn Analysis",
            "COVID-19 Data Analysis"
        ],
        "interview": [
            "Python basics",
            "SQL queries",
            "Excel functions",
            "Statistics",
            "Data cleaning",
            "Data visualization",
            "Project explanation"
        ]
    },

    "machine learning": {
        "title": "Machine Learning Engineer Career Path",
        "skills": [
            "Python",
            "NumPy and Pandas",
            "Statistics",
            "Linear Algebra basics",
            "Machine Learning algorithms",
            "Scikit-learn",
            "Data preprocessing",
            "Model evaluation",
            "Git and GitHub",
            "Basic deployment"
        ],
        "roadmap": [
            "Learn Python",
            "Learn NumPy and Pandas",
            "Learn statistics",
            "Learn machine learning fundamentals",
            "Study supervised learning",
            "Study unsupervised learning",
            "Learn model evaluation",
            "Build ML projects",
            "Learn deployment basics",
            "Prepare for ML interviews"
        ],
        "projects": [
            "House Price Prediction",
            "Customer Churn Prediction",
            "Spam Detection",
            "Resume Screening",
            "Student Performance Prediction"
        ],
        "interview": [
            "Supervised vs unsupervised learning",
            "Classification vs regression",
            "Overfitting and underfitting",
            "Model evaluation metrics",
            "Feature engineering",
            "Random Forest",
            "Project explanation"
        ]
    },

    "python": {
        "title": "Python Developer Career Path",
        "skills": [
            "Python fundamentals",
            "OOP",
            "Data structures",
            "Exception handling",
            "File handling",
            "Modules and packages",
            "Git and GitHub",
            "APIs",
            "Database basics",
            "Backend development"
        ],
        "roadmap": [
            "Learn Python basics",
            "Practice problem solving",
            "Learn OOP",
            "Learn data structures",
            "Learn file handling",
            "Learn SQL",
            "Learn APIs",
            "Learn Flask or Django",
            "Build projects",
            "Prepare for interviews"
        ],
        "projects": [
            "Student Management System",
            "Expense Tracker",
            "Movie Ticket Booking System",
            "REST API",
            "Library Management System"
        ],
        "interview": [
            "Python data types",
            "Functions",
            "OOP concepts",
            "Exception handling",
            "List vs tuple",
            "Dictionary and set",
            "Generators",
            "Decorators",
            "Project explanation"
        ]
    },

    "ai": {
        "title": "AI Engineer Career Path",
        "skills": [
            "Python",
            "Machine Learning",
            "Deep Learning basics",
            "NLP",
            "Computer Vision",
            "NumPy",
            "Pandas",
            "Scikit-learn",
            "PyTorch or TensorFlow",
            "Model deployment"
        ],
        "roadmap": [
            "Learn Python",
            "Learn mathematics basics",
            "Learn data science fundamentals",
            "Learn machine learning",
            "Learn deep learning",
            "Learn NLP and computer vision",
            "Build AI projects",
            "Learn model deployment",
            "Create a portfolio",
            "Prepare for AI interviews"
        ],
        "projects": [
            "AI Chatbot",
            "Image Classification",
            "Sign Language Recognition",
            "Sentiment Analysis",
            "Resume Screening System"
        ],
        "interview": [
            "AI vs ML vs Deep Learning",
            "Supervised learning",
            "Neural networks",
            "NLP basics",
            "Computer vision",
            "Model evaluation",
            "AI project architecture"
        ]
    }
}


def show_career(career):
    print()
    print("=" * 70)
    print(career["title"])
    print("=" * 70)

    print()
    print("1. Important Skills")
    for skill in career["skills"]:
        print(f"• {skill}")

    print()
    print("2. Learning Roadmap")
    for number, step in enumerate(career["roadmap"], start=1):
        print(f"{number}. {step}")

    print()
    print("3. Recommended Projects")
    for project in career["projects"]:
        print(f"• {project}")

    print()
    print("4. Interview Preparation")
    for topic in career["interview"]:
        print(f"• {topic}")

    print()
    print("=" * 70)


def find_career(question):
    question = question.lower()

    if "data analyst" in question or "data analysis" in question:
        return CAREERS["data analyst"]

    if "machine learning" in question or "ml engineer" in question:
        return CAREERS["machine learning"]

    if "python developer" in question or "python career" in question:
        return CAREERS["python"]

    if "ai engineer" in question or "artificial intelligence" in question:
        return CAREERS["ai"]

    return None


def start_career_mode():
    print()
    print("=" * 70)
    print("                      CAREER MODE")
    print("=" * 70)

    print()
    print("You can ask:")
    print("• What skills do I need for Data Analyst?")
    print("• Give me a Machine Learning roadmap")
    print("• How can I become a Python Developer?")
    print("• What should I learn for an AI Engineer career?")
    print()
    print("Type 'back' to return to the main chatbot.")

    while True:
        question = input("\nCareer Mode > ").strip()

        if question.lower() in ["back", "exit", "quit"]:
            print("Returning to main chatbot...")
            break

        career = find_career(question)

        if career:
            show_career(career)
        else:
            print()
            print("Available career paths:")
            print("1. Data Analyst")
            print("2. Machine Learning Engineer")
            print("3. Python Developer")
            print("4. AI Engineer")


if __name__ == "__main__":
    start_career_mode()