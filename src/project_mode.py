PROJECTS = {
    "python": {
        "title": "Python Student Management System",
        "problem": "Students, marks and attendance information ni manage cheyyadaniki system.",
        "technologies": "Python, JSON, OOP",
        "dataset": "Dataset required kaadu. User-entered student data use cheyyachu.",
        "steps": [
            "Define the problem",
            "Create Student class",
            "Add student details",
            "Store data using JSON",
            "Add search and update features",
            "Display student records",
            "Test the system"
        ],
        "output": "A console-based Student Management System."
    },

    "ml": {
        "title": "Machine Learning Prediction System",
        "problem": "Historical data ni use chesi future result/prediction cheyyadam.",
        "technologies": "Python, Pandas, NumPy, Scikit-learn, Matplotlib",
        "dataset": "CSV dataset containing relevant input features and target values.",
        "steps": [
            "Collect dataset",
            "Load dataset using Pandas",
            "Clean missing or incorrect data",
            "Perform data analysis",
            "Split features and target",
            "Train-test split",
            "Train ML model",
            "Evaluate the model",
            "Make predictions",
            "Display results"
        ],
        "output": "A trained machine learning model that predicts the target value."
    },

    "resume": {
        "title": "AI Resume Screening System",
        "problem": "Large number of resumes ni automatically analyze chesi job requirements tho compare cheyyadam.",
        "technologies": "Python, NLP, Machine Learning, Pandas, Scikit-learn",
        "dataset": "Resume documents and job-description data.",
        "steps": [
            "Collect resume data",
            "Extract resume text",
            "Clean the text",
            "Tokenize and preprocess text",
            "Extract important features",
            "Process job description",
            "Calculate similarity",
            "Rank resumes",
            "Display matching results",
            "Test the system"
        ],
        "output": "Resumes ranked according to their similarity with the job requirements."
    },

    "chatbot": {
        "title": "Python Question Answering Chatbot",
        "problem": "Students ki Python and technical topics gurinchi questions ki automated answers provide cheyyadam.",
        "technologies": "Python, NLP, NLTK, Scikit-learn, TF-IDF",
        "dataset": "Question-answer pairs stored in JSON.",
        "steps": [
            "Collect question-answer data",
            "Clean the text",
            "Tokenize and lemmatize",
            "Convert text into TF-IDF vectors",
            "Train the matching model",
            "Find the most relevant topic",
            "Generate the answer",
            "Store conversation history",
            "Add learning and quiz modes",
            "Test the chatbot"
        ],
        "output": "A console-based intelligent Python learning chatbot."
    },

    "data": {
        "title": "Data Analysis Dashboard",
        "problem": "Large datasets ni analyze chesi useful patterns and insights identify cheyyadam.",
        "technologies": "Python, Pandas, NumPy, Matplotlib",
        "dataset": "CSV or Excel dataset.",
        "steps": [
            "Collect dataset",
            "Load data",
            "Check missing values",
            "Clean the data",
            "Perform statistical analysis",
            "Find important patterns",
            "Create visualizations",
            "Interpret results",
            "Generate final report"
        ],
        "output": "Data insights and visualizations that help understand the dataset."
    }
}


def show_project(project):
    print()
    print("=" * 70)
    print(f"PROJECT: {project['title']}")
    print("=" * 70)

    print()
    print("1. Problem Statement")
    print(project["problem"])

    print()
    print("2. Technologies")
    print(project["technologies"])

    print()
    print("3. Dataset")
    print(project["dataset"])

    print()
    print("4. Development Steps")

    for number, step in enumerate(project["steps"], start=1):
        print(f"{number}. {step}")

    print()
    print("5. Expected Output")
    print(project["output"])

    print()
    print("=" * 70)


def find_project(question):
    question = question.lower()

    if "resume" in question:
        return PROJECTS["resume"]

    if "chatbot" in question:
        return PROJECTS["chatbot"]

    if "machine learning" in question or "ml project" in question:
        return PROJECTS["ml"]

    if "data analysis" in question or "data science project" in question:
        return PROJECTS["data"]

    if "python project" in question or "student management" in question:
        return PROJECTS["python"]

    return None


def start_project_mode():
    print()
    print("=" * 70)
    print("                    PROJECT MODE")
    print("=" * 70)

    print()
    print("You can ask things like:")
    print("• suggest a python project")
    print("• suggest an ML project")
    print("• how to build resume screening project")
    print("• suggest a data analysis project")
    print("• how to build a chatbot")
    print()
    print("Type 'back' to return to the main chatbot.")

    while True:
        question = input("\nProject Mode > ").strip()

        if question.lower() in ["back", "exit", "quit"]:
            print("Returning to main chatbot...")
            break

        project = find_project(question)

        if project:
            show_project(project)
        else:
            print()
            print("Available project areas:")
            print("1. Python")
            print("2. Machine Learning")
            print("3. Resume Screening")
            print("4. Data Analysis")
            print("5. Chatbot")


if __name__ == "__main__":
    start_project_mode()