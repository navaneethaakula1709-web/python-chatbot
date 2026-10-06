import os

import re

import json



from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity



from nlp_processor import preprocess





# ============================================================

# PROJECT PATHS

# ============================================================



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



DATA_FILE = os.path.join(

    BASE_DIR,

    "data",

    "python_questions.json"

)





# ============================================================

# PYTHON KNOWLEDGE BASE

# ============================================================



TOPICS = {



    # --------------------------------------------------------

    # PYTHON BASICS

    # --------------------------------------------------------



    "python": {

        "category": "Python Basics",

        "definition": "Python is a high-level, interpreted and general-purpose programming language known for its simple and readable syntax.",

        "example": 'print("Hello, Python!")',

        "syntax": 'print("message")'

    },



    "variable": {

        "category": "Python Basics",

        "definition": "A variable is a name used to store a value in a program.",

        "example": 'name = "Navaneetha"\nage = 20\nprint(name)\nprint(age)',

        "syntax": "variable = value"

    },



    "constant": {

        "category": "Python Basics",

        "definition": "A constant is a value that is intended to remain unchanged during program execution.",

        "example": "PI = 3.14159",

        "syntax": "CONSTANT_NAME = value"

    },



    "data type": {

        "category": "Python Basics",

        "definition": "A data type specifies what kind of value a variable contains, such as integer, float, string, boolean or list.",

        "example": 'age = 20\nprice = 99.5\nname = "Python"\npassed = True',

        "syntax": "variable = value"

    },



    "integer": {

        "category": "Python Basics",

        "definition": "An integer is a whole number without a decimal point.",

        "example": "age = 20",

        "syntax": "variable = integer"

    },



    "float": {

        "category": "Python Basics",

        "definition": "A float represents a number containing a decimal point.",

        "example": "price = 99.50",

        "syntax": "variable = decimal_value"

    },



    "string": {

        "category": "Python Basics",

        "definition": "A string is a sequence of characters enclosed in quotes.",

        "example": 'name = "Python"\nprint(name)',

        "syntax": 'variable = "text"'

    },



    "boolean": {

        "category": "Python Basics",

        "definition": "A boolean represents one of two values: True or False.",

        "example": "is_student = True",

        "syntax": "variable = True or False"

    },



    "type casting": {

        "category": "Python Basics",

        "definition": "Type casting means converting a value from one data type to another.",

        "example": 'age = "20"\nnumber = int(age)\nprint(number)',

        "syntax": "new_type(value)"

    },



    "input": {

        "category": "Python Basics",

        "definition": "The input() function is used to receive data from the user.",

        "example": 'name = input("Enter your name: ")\nprint(name)',

        "syntax": "input(prompt)"

    },



    "output": {

        "category": "Python Basics",

        "definition": "The print() function is used to display output on the screen.",

        "example": 'print("Hello World")',

        "syntax": "print(value)"

    },



    "operator": {

        "category": "Python Basics",

        "definition": "An operator is a symbol used to perform operations on values.",

        "example": "a = 10\nb = 5\nprint(a + b)",

        "syntax": "operand operator operand"

    },



    "arithmetic operator": {

        "category": "Python Basics",

        "definition": "Arithmetic operators perform mathematical operations such as addition, subtraction, multiplication and division.",

        "example": "a = 10\nb = 3\nprint(a + b)\nprint(a - b)\nprint(a * b)\nprint(a / b)",

        "syntax": "+  -  *  /  %  //  **"

    },



    "comparison operator": {

        "category": "Python Basics",

        "definition": "Comparison operators compare two values and return True or False.",

        "example": "a = 10\nb = 5\nprint(a > b)",

        "syntax": "==  !=  >  <  >=  <="

    },



    "logical operator": {

        "category": "Python Basics",

        "definition": "Logical operators combine or modify conditions.",

        "example": "age = 20\nprint(age > 18 and age < 30)",

        "syntax": "and, or, not"

    },



    "membership operator": {

        "category": "Python Basics",

        "definition": "Membership operators check whether a value exists in a sequence.",

        "example": 'numbers = [1, 2, 3]\nprint(2 in numbers)',

        "syntax": "in, not in"

    },



    "identity operator": {

        "category": "Python Basics",

        "definition": "Identity operators check whether two variables refer to the same object.",

        "example": "a = [1, 2]\nb = a\nprint(a is b)",

        "syntax": "is, is not"

    },





    # --------------------------------------------------------

    # CONTROL STATEMENTS

    # --------------------------------------------------------



    "if statement": {

        "category": "Control Statements",

        "definition": "An if statement executes a block of code when a condition is True.",

        "example": 'age = 20\nif age >= 18:\n    print("Adult")',

        "syntax": "if condition:"

    },



    "if else": {

        "category": "Control Statements",

        "definition": "The if-else statement chooses between two blocks of code based on a condition.",

        "example": 'age = 16\nif age >= 18:\n    print("Adult")\nelse:\n    print("Minor")',

        "syntax": "if condition:\n    statement\nelse:\n    statement"

    },



    "if elif else": {

        "category": "Control Statements",

        "definition": "if-elif-else is used when multiple conditions need to be checked.",

        "example": 'mark = 85\nif mark >= 90:\n    print("A+")\nelif mark >= 75:\n    print("A")\nelse:\n    print("B")',

        "syntax": "if condition:\nelif condition:\nelse:"

    },



    "for loop": {

        "category": "Control Statements",

        "definition": "A for loop is used to repeat a block of code for each item in a sequence or iterable.",

        "example": 'for i in range(5):\n    print(i)',

        "syntax": "for variable in sequence:"

    },



    "while loop": {

        "category": "Control Statements",

        "definition": "A while loop repeatedly executes a block of code while a condition remains True.",

        "example": 'i = 1\nwhile i <= 5:\n    print(i)\n    i += 1',

        "syntax": "while condition:"

    },



    "nested loop": {

        "category": "Control Statements",

        "definition": "A nested loop is a loop placed inside another loop.",

        "example": 'for i in range(3):\n    for j in range(2):\n        print(i, j)',

        "syntax": "loop inside another loop"

    },



    "break": {

        "category": "Control Statements",

        "definition": "The break statement immediately terminates the current loop.",

        "example": 'for i in range(10):\n    if i == 5:\n        break\n    print(i)',

        "syntax": "break"

    },



    "continue": {

        "category": "Control Statements",

        "definition": "The continue statement skips the current iteration and moves to the next iteration.",

        "example": 'for i in range(5):\n    if i == 2:\n        continue\n    print(i)',

        "syntax": "continue"

    },



    "pass": {

        "category": "Control Statements",

        "definition": "The pass statement does nothing and is used as a placeholder.",

        "example": 'if True:\n    pass',

        "syntax": "pass"

    },



    "range": {

        "category": "Control Statements",

        "definition": "The range() function generates a sequence of numbers commonly used with loops.",

        "example": "for i in range(1, 6):\n    print(i)",

        "syntax": "range(start, stop, step)"

    },





    # --------------------------------------------------------

    # DATA STRUCTURES

    # --------------------------------------------------------



    "list": {

        "category": "Data Structures",

        "definition": "A list is an ordered and mutable collection that can store multiple values.",

        "example": 'numbers = [10, 20, 30]\nnumbers.append(40)\nprint(numbers)',

        "syntax": "list_name = [item1, item2]"

    },



    "tuple": {

        "category": "Data Structures",

        "definition": "A tuple is an ordered and immutable collection of values.",

        "example": "numbers = (10, 20, 30)\nprint(numbers)",

        "syntax": "tuple_name = (item1, item2)"

    },



    "set": {

        "category": "Data Structures",

        "definition": "A set is an unordered collection of unique elements.",

        "example": "numbers = {1, 2, 3, 3}\nprint(numbers)",

        "syntax": "set_name = {items}"

    },



    "dictionary": {

        "category": "Data Structures",

        "definition": "A dictionary stores data as key-value pairs.",

        "example": 'student = {"name": "Navaneetha", "age": 20}\nprint(student["name"])',

        "syntax": "dictionary = {key: value}"

    },



    "list comprehension": {

        "category": "Data Structures",

        "definition": "List comprehension provides a compact way to create lists using an expression and loop.",

        "example": "squares = [x * x for x in range(5)]\nprint(squares)",

        "syntax": "[expression for item in iterable]"

    },



    "dictionary comprehension": {

        "category": "Data Structures",

        "definition": "Dictionary comprehension provides a concise way to create dictionaries.",

        "example": "squares = {x: x*x for x in range(5)}\nprint(squares)",

        "syntax": "{key: value for item in iterable}"

    },



    "indexing": {

        "category": "Data Structures",

        "definition": "Indexing is used to access an individual element from a sequence using its position.",

        "example": 'numbers = [10, 20, 30]\nprint(numbers[0])',

        "syntax": "sequence[index]"

    },



    "slicing": {

        "category": "Data Structures",

        "definition": "Slicing extracts a portion of a sequence.",

        "example": "numbers = [1, 2, 3, 4, 5]\nprint(numbers[1:4])",

        "syntax": "sequence[start:stop:step]"

    },



    "stack": {

        "category": "Data Structures",

        "definition": "A stack is a LIFO data structure where the last inserted element is removed first.",

        "example": "stack = []\nstack.append(10)\nstack.append(20)\nprint(stack.pop())",

        "syntax": "append() and pop()"

    },



    "queue": {

        "category": "Data Structures",

        "definition": "A queue is a FIFO data structure where the first inserted element is removed first.",

        "example": "from collections import deque\nq = deque([1, 2])\nq.append(3)\nprint(q.popleft())",

        "syntax": "append() and popleft()"

    },





    # --------------------------------------------------------

    # FUNCTIONS

    # --------------------------------------------------------



    "function": {

        "category": "Functions",

        "definition": "A function is a reusable block of code designed to perform a specific task.",

        "example": 'def greet():\n    print("Hello")\n\ngreet()',

        "syntax": "def function_name():"

    },



    "parameter": {

        "category": "Functions",

        "definition": "A parameter is a variable defined in a function that receives a value.",

        "example": 'def greet(name):\n    print("Hello", name)\n\ngreet("Python")',

        "syntax": "def function(parameter):"

    },



    "argument": {

        "category": "Functions",

        "definition": "An argument is the actual value passed to a function when it is called.",

        "example": 'def greet(name):\n    print(name)\n\ngreet("Python")',

        "syntax": "function(value)"

    },



    "return statement": {

        "category": "Functions",

        "definition": "The return statement sends a value back from a function.",

        "example": 'def add(a, b):\n    return a + b\n\nprint(add(2, 3))',

        "syntax": "return value"

    },



    "lambda": {

        "category": "Functions",

        "definition": "A lambda is a small anonymous function written using the lambda keyword.",

        "example": "square = lambda x: x * x\nprint(square(5))",

        "syntax": "lambda arguments: expression"

    },



    "recursion": {

        "category": "Functions",

        "definition": "Recursion is a technique where a function calls itself to solve a problem.",

        "example": 'def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n - 1)\n\nprint(factorial(5))',

        "syntax": "function calls itself"

    },

    "factorial": {

    "category": "Functions",

    "definition": "Factorial of a positive integer n is the product of all positive integers from 1 to n. It is represented as n!.",

    "example": 'def factorial(n):\n    if n == 0 or n == 1:\n        return 1\n    return n * factorial(n - 1)\n\nnumber = 5\nprint("Factorial:", factorial(number))',

    "syntax": "factorial(n)"

    },



    "map": {

        "category": "Functions",

        "definition": "map() applies a function to every item in an iterable.",

        "example": "numbers = [1, 2, 3]\nresult = list(map(lambda x: x * 2, numbers))\nprint(result)",

        "syntax": "map(function, iterable)"

    },



    "filter": {

        "category": "Functions",

        "definition": "filter() selects elements from an iterable that satisfy a condition.",

        "example": "numbers = [1, 2, 3, 4]\nresult = list(filter(lambda x: x % 2 == 0, numbers))\nprint(result)",

        "syntax": "filter(function, iterable)"

    },



    "reduce": {

        "category": "Functions",

        "definition": "reduce() repeatedly applies a function to combine elements into a single result.",

        "example": "from functools import reduce\nnumbers = [1, 2, 3, 4]\nresult = reduce(lambda a, b: a + b, numbers)\nprint(result)",

        "syntax": "reduce(function, iterable)"

    },





    # --------------------------------------------------------

    # OOP

    # --------------------------------------------------------



    "class": {

        "category": "Object-Oriented Programming",

        "definition": "A class is a blueprint used to create objects.",

        "example": 'class Student:\n    pass\n\nstudent = Student()',

        "syntax": "class ClassName:"

    },



    "object": {

        "category": "Object-Oriented Programming",

        "definition": "An object is an instance of a class containing data and behavior.",

        "example": 'class Student:\n    pass\n\nstudent = Student()',

        "syntax": "object = ClassName()"

    },



    "constructor": {

        "category": "Object-Oriented Programming",

        "definition": "The __init__() method is commonly used as a constructor to initialize object attributes.",

        "example": 'class Student:\n    def __init__(self, name):\n        self.name = name\n\ns = Student("Navaneetha")',

        "syntax": "def __init__(self):"

    },



    "self": {

        "category": "Object-Oriented Programming",

        "definition": "self refers to the current object inside a class method.",

        "example": 'class Student:\n    def __init__(self, name):\n        self.name = name',

        "syntax": "self.attribute"

    },



    "inheritance": {

        "category": "Object-Oriented Programming",

        "definition": "Inheritance allows one class to acquire properties and methods from another class.",

        "example": 'class Animal:\n    def speak(self):\n        print("Animal sound")\n\nclass Dog(Animal):\n    pass\n\nDog().speak()',

        "syntax": "class Child(Parent):"

    },



    "polymorphism": {

        "category": "Object-Oriented Programming",

        "definition": "Polymorphism allows the same method or interface to behave differently for different objects.",

        "example": 'class Dog:\n    def sound(self):\n        print("Bark")\n\nclass Cat:\n    def sound(self):\n        print("Meow")\n\nfor animal in [Dog(), Cat()]:\n    animal.sound()',

        "syntax": "same method name with different behavior"

    },



    "encapsulation": {

        "category": "Object-Oriented Programming",

        "definition": "Encapsulation combines data and methods inside a class and can restrict direct access to internal data.",

        "example": 'class Student:\n    def __init__(self):\n        self.__marks = 90',

        "syntax": "self.__private_variable"

    },



    "abstraction": {

        "category": "Object-Oriented Programming",

        "definition": "Abstraction hides implementation details and exposes only the necessary functionality.",

        "example": 'from abc import ABC, abstractmethod\n\nclass Animal(ABC):\n    @abstractmethod\n    def sound(self):\n        pass',

        "syntax": "ABC and abstractmethod"

    },



    "method overriding": {

        "category": "Object-Oriented Programming",

        "definition": "Method overriding occurs when a child class provides its own implementation of a parent class method.",

        "example": 'class Animal:\n    def sound(self):\n        print("Sound")\n\nclass Dog(Animal):\n    def sound(self):\n        print("Bark")',

        "syntax": "same method in child class"

    },





    # --------------------------------------------------------

    # EXCEPTION HANDLING

    # --------------------------------------------------------



    "exception": {

        "category": "Exception Handling",

        "definition": "An exception is an error or unexpected event that occurs during program execution.",

        "example": 'try:\n    print(10 / 0)\nexcept ZeroDivisionError:\n    print("Cannot divide by zero")',

        "syntax": "try / except"

    },



    "try except": {

        "category": "Exception Handling",

        "definition": "try-except is used to handle runtime errors without stopping the entire program.",

        "example": 'try:\n    number = int(input("Enter number: "))\nexcept ValueError:\n    print("Invalid input")',

        "syntax": "try:\n    code\nexcept Exception:"

    },



    "finally": {

        "category": "Exception Handling",

        "definition": "The finally block executes whether an exception occurs or not.",

        "example": 'try:\n    print("Work")\nfinally:\n    print("Always executes")',

        "syntax": "finally:"

    },



    "raise": {

        "category": "Exception Handling",

        "definition": "The raise statement is used to manually generate an exception.",

        "example": 'age = -1\nif age < 0:\n    raise ValueError("Age cannot be negative")',

        "syntax": "raise ExceptionType()"

    },





    # --------------------------------------------------------

    # FILES / MODULES

    # --------------------------------------------------------



    "file handling": {

        "category": "File Handling",

        "definition": "File handling allows Python programs to read, write and manage files.",

        "example": 'with open("data.txt", "w") as file:\n    file.write("Hello Python")',

        "syntax": 'open("file", "mode")'

    },



    "read file": {

        "category": "File Handling",

        "definition": "A file can be opened in read mode to retrieve stored data.",

        "example": 'with open("data.txt", "r") as file:\n    data = file.read()\n    print(data)',

        "syntax": 'open("file.txt", "r")'

    },



    "write file": {

        "category": "File Handling",

        "definition": "A file can be opened in write mode to create or replace its contents.",

        "example": 'with open("data.txt", "w") as file:\n    file.write("Hello")',

        "syntax": 'open("file.txt", "w")'

    },



    "module": {

        "category": "Modules and Packages",

        "definition": "A module is a Python file containing reusable code such as functions, classes or variables.",

        "example": "import math\nprint(math.sqrt(25))",

        "syntax": "import module_name"

    },



    "package": {

        "category": "Modules and Packages",

        "definition": "A package is a directory containing Python modules and related files.",

        "example": "from math import sqrt\nprint(sqrt(16))",

        "syntax": "from package import module"

    },



    "pip": {

        "category": "Modules and Packages",

        "definition": "pip is Python's package installer used to install external Python packages.",

        "example": "pip install pandas",

        "syntax": "pip install package_name"

    },



    "virtual environment": {

        "category": "Python Environment",

        "definition": "A virtual environment creates an isolated Python environment for a project.",

        "example": "python -m venv venv",

        "syntax": "python -m venv environment_name"

    },



    "requirements": {

        "category": "Python Environment",

        "definition": "A requirements file lists the packages needed by a Python project.",

        "example": "pip freeze > requirements.txt",

        "syntax": "pip install -r requirements.txt"

    },





    # --------------------------------------------------------

    # ADVANCED PYTHON

    # --------------------------------------------------------



    "iterator": {

        "category": "Advanced Python",

        "definition": "An iterator is an object that returns elements one at a time using the iterator protocol.",

        "example": "numbers = iter([1, 2, 3])\nprint(next(numbers))\nprint(next(numbers))",

        "syntax": "iter() and next()"

    },



    "generator": {

        "category": "Advanced Python",

        "definition": "A generator is a special type of iterator that produces values lazily using yield.",

        "example": 'def numbers():\n    yield 1\n    yield 2\n\nfor n in numbers():\n    print(n)',

        "syntax": "yield"

    },



    "decorator": {

        "category": "Advanced Python",

        "definition": "A decorator modifies or extends the behavior of a function without changing its original code.",

        "example": 'def decorator(func):\n    def wrapper():\n        print("Before")\n        func()\n    return wrapper\n\n@decorator\ndef greet():\n    print("Hello")\n\ngreet()',

        "syntax": "@decorator"

    },



    "regular expression": {

        "category": "Advanced Python",

        "definition": "A regular expression is a pattern used to search, match or manipulate text.",

        "example": 'import re\ntext = "Python 123"\nresult = re.findall(r"\\d+", text)\nprint(result)',

        "syntax": "re.findall(pattern, text)"

    },



    "json": {

        "category": "Advanced Python",

        "definition": "JSON is a lightweight format commonly used to exchange structured data between applications.",

        "example": 'import json\ndata = {"name": "Python"}\ntext = json.dumps(data)\nprint(text)',

        "syntax": "json.dumps() / json.loads()"

    },



    "multithreading": {

        "category": "Advanced Python",

        "definition": "Multithreading allows multiple threads to execute tasks concurrently within a process.",

        "example": 'import threading\n\ndef task():\n    print("Running task")\n\nthread = threading.Thread(target=task)\nthread.start()',

        "syntax": "threading.Thread()"

    },



    "multiprocessing": {

        "category": "Advanced Python",

        "definition": "Multiprocessing uses separate processes to execute tasks concurrently.",

        "example": 'from multiprocessing import Process\n\ndef task():\n    print("Running")\n\np = Process(target=task)\np.start()',

        "syntax": "Process(target=function)"

    },





    # --------------------------------------------------------

    # PYTHON LIBRARIES

    # --------------------------------------------------------



    "numpy": {

        "category": "Python Libraries",

        "definition": "NumPy is a Python library used for numerical computing and multidimensional arrays.",

        "example": 'import numpy as np\narr = np.array([1, 2, 3])\nprint(arr)',

        "syntax": "import numpy as np"

    },



    "pandas": {

        "category": "Python Libraries",

        "definition": "Pandas is a Python library used for data manipulation and analysis using structures such as Series and DataFrame.",

        "example": 'import pandas as pd\ndata = {"Name": ["A", "B"], "Age": [20, 21]}\ndf = pd.DataFrame(data)\nprint(df)',

        "syntax": "pd.DataFrame(data)"

    },



    "matplotlib": {

        "category": "Python Libraries",

        "definition": "Matplotlib is a Python library used to create graphs and visualizations.",

        "example": 'import matplotlib.pyplot as plt\nplt.plot([1, 2, 3], [2, 4, 6])\nplt.show()',

        "syntax": "plt.plot(x, y)"

    },



    "seaborn": {

        "category": "Python Libraries",

        "definition": "Seaborn is a Python visualization library built on top of Matplotlib.",

        "example": 'import seaborn as sns\nsns.set_theme()\nsns.lineplot(x=[1, 2, 3], y=[2, 4, 6])',

        "syntax": "sns.plot_function()"

    },



    "scikit learn": {

        "category": "Machine Learning",

        "definition": "Scikit-learn is a Python library that provides tools for machine learning, preprocessing, model training and evaluation.",

        "example": 'from sklearn.linear_model import LinearRegression\nmodel = LinearRegression()',

        "syntax": "from sklearn import ..."

    },



    "opencv": {

        "category": "Computer Vision",

        "definition": "OpenCV is a computer vision library used for image and video processing.",

        "example": 'import cv2\nimage = cv2.imread("image.jpg")\nprint(image.shape)',

        "syntax": "cv2.imread()"

    },



    "mediapipe": {

        "category": "Computer Vision",

        "definition": "MediaPipe is a framework that provides solutions for tasks such as hand, face and pose tracking.",

        "example": "import mediapipe as mp\nprint(mp)",

        "syntax": "import mediapipe as mp"

    },





    # --------------------------------------------------------

    # DATA SCIENCE

    # --------------------------------------------------------



    "data science": {

        "category": "Data Science",

        "definition": "Data Science combines statistics, programming, data analysis and machine learning to extract useful insights from data.",

        "example": "Collect data → Clean data → Analyze data → Visualize data → Build model",

        "syntax": "Data → Cleaning → Analysis → Modeling"

    },



    "data analysis": {

        "category": "Data Science",

        "definition": "Data analysis is the process of inspecting, cleaning and interpreting data to discover useful information.",

        "example": "Use Pandas to load a CSV file and calculate the average of a column.",

        "syntax": "load → clean → analyze → visualize"

    },



    "mean": {

        "category": "Statistics",

        "definition": "Mean is the average value of a set of numbers.",

        "example": "For 1, 2, 3, 4: mean = (1+2+3+4)/4 = 2.5",

        "syntax": "Mean = Sum of values / Number of values"

    },



    "median": {

        "category": "Statistics",

        "definition": "Median is the middle value when data is arranged in ascending or descending order.",

        "example": "For 1, 2, 3, 4, 5, the median is 3.",

        "syntax": "Middle value"

    },



    "mode": {

        "category": "Statistics",

        "definition": "Mode is the value that occurs most frequently in a dataset.",

        "example": "For 1, 2, 2, 3, the mode is 2.",

        "syntax": "Most frequent value"

    },



    "variance": {

        "category": "Statistics",

        "definition": "Variance measures how far data values are spread from their mean.",

        "example": "For a dataset, calculate the difference from the mean, square the differences and find their average.",

        "syntax": "Variance = average squared deviation from mean"

    },



    "standard deviation": {

        "category": "Statistics",

        "definition": "Standard deviation measures the amount of variation or dispersion in a dataset.",

        "example": "Standard deviation is the square root of variance.",

        "syntax": "SD = √Variance"

    },



    "correlation": {

        "category": "Statistics",

        "definition": "Correlation measures the strength and direction of the relationship between two variables.",

        "example": "Study hours and exam marks may have a positive correlation.",

        "syntax": "-1 <= correlation <= 1"

    },





    # --------------------------------------------------------

    # MACHINE LEARNING

    # --------------------------------------------------------



    "machine learning": {

        "category": "Machine Learning",

        "definition": "Machine Learning is a branch of AI where computers learn patterns from data and use them to make predictions or decisions.",

        "example": "Train a model using student study hours and marks to predict marks for a new student.",

        "syntax": "Data → Training → Model → Prediction"

    },



    "supervised learning": {

        "category": "Machine Learning",

        "definition": "Supervised learning trains a model using labeled data containing input values and known outputs.",

        "example": "Predict house prices using previous house data with known prices.",

        "syntax": "Input + Label → Model → Prediction"

    },



    "unsupervised learning": {

        "category": "Machine Learning",

        "definition": "Unsupervised learning finds patterns or structures in data without labeled output values.",

        "example": "Group customers into different segments using clustering.",

        "syntax": "Input data → Pattern discovery"

    },



    "reinforcement learning": {

        "category": "Machine Learning",

        "definition": "Reinforcement learning trains an agent through actions, rewards and penalties.",

        "example": "A game-playing agent learns which actions produce higher rewards.",

        "syntax": "State → Action → Reward → Learning"

    },



    "classification": {

        "category": "Machine Learning",

        "definition": "Classification is a supervised learning task that predicts a category or class.",

        "example": "Classify an email as spam or not spam.",

        "syntax": "Input → Class"

    },



    "regression": {

        "category": "Machine Learning",

        "definition": "Regression predicts a continuous numerical value.",

        "example": "Predict a house price from its size and location.",

        "syntax": "Input → Numerical output"

    },



    "linear regression": {

        "category": "Machine Learning",

        "definition": "Linear regression models the relationship between variables using a linear equation.",

        "example": "Predict salary based on years of experience.",

        "syntax": "y = mx + c"

    },



    "logistic regression": {

        "category": "Machine Learning",

        "definition": "Logistic regression is commonly used for classification problems and estimates class probabilities.",

        "example": "Predict whether a student passes or fails.",

        "syntax": "Probability → Class"

    },



    "decision tree": {

        "category": "Machine Learning",

        "definition": "A decision tree makes predictions using a tree-like sequence of decision rules.",

        "example": "A model can decide whether a person qualifies for a loan based on income and credit information.",

        "syntax": "Features → Decision nodes → Prediction"

    },



    "random forest": {

        "category": "Machine Learning",

        "definition": "Random Forest is an ensemble learning algorithm that combines predictions from multiple decision trees.",

        "example": "A Random Forest can classify whether an email is spam using multiple decision trees.",

        "syntax": "Many Decision Trees → Combined Prediction"

    },



    "knn": {

        "category": "Machine Learning",

        "definition": "K-Nearest Neighbors predicts a value or class using the closest data points.",

        "example": "Classify a new student based on students with similar features.",

        "syntax": "Find nearest neighbors → Vote"

    },



    "support vector machine": {

        "category": "Machine Learning",

        "definition": "Support Vector Machine finds a decision boundary that separates classes effectively.",

        "example": "Classify two groups of data points using a separating hyperplane.",

        "syntax": "Features → Decision boundary → Class"

    },



    "k means": {

        "category": "Machine Learning",

        "definition": "K-Means is an unsupervised clustering algorithm that divides data into K groups.",

        "example": "Divide customers into three groups based on purchasing behavior.",

        "syntax": "Data → K clusters"

    },



    "overfitting": {

        "category": "Machine Learning",

        "definition": "Overfitting occurs when a model learns the training data too closely and performs poorly on unseen data.",

        "example": "A model gets very high training accuracy but much lower test accuracy.",

        "syntax": "Training performance high + Test performance low"

    },



    "underfitting": {

        "category": "Machine Learning",

        "definition": "Underfitting occurs when a model is too simple to learn important patterns in the data.",

        "example": "A simple model performs poorly on both training and test data.",

        "syntax": "Training performance low + Test performance low"

    },



    "train test split": {

        "category": "Machine Learning",

        "definition": "Train-test split divides a dataset into training data and testing data.",

        "example": 'from sklearn.model_selection import train_test_split\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)',

        "syntax": "train_test_split(X, y)"

    },



    "accuracy": {

        "category": "Machine Learning",

        "definition": "Accuracy is the proportion of correct predictions among all predictions.",

        "example": "If 90 out of 100 predictions are correct, accuracy is 90%.",

        "syntax": "Accuracy = Correct predictions / Total predictions"

    },



    "precision": {

        "category": "Machine Learning",

        "definition": "Precision measures how many predicted positive cases were actually positive.",

        "example": "Precision is important when false positive predictions are costly.",

        "syntax": "Precision = TP / (TP + FP)"

    },



    "recall": {

        "category": "Machine Learning",

        "definition": "Recall measures how many actual positive cases were correctly identified.",

        "example": "Recall is important when missing positive cases is costly.",

        "syntax": "Recall = TP / (TP + FN)"

    },



    "f1 score": {

        "category": "Machine Learning",

        "definition": "F1 score is the harmonic mean of precision and recall.",

        "example": "F1 score is useful when both precision and recall are important.",

        "syntax": "F1 = 2 × Precision × Recall / (Precision + Recall)"

    },



    "confusion matrix": {

        "category": "Machine Learning",

        "definition": "A confusion matrix summarizes classification predictions using true positives, true negatives, false positives and false negatives.",

        "example": "It can be used to evaluate a spam classification model.",

        "syntax": "TP, TN, FP, FN"

    },



    "mse": {

        "category": "Machine Learning",

        "definition": "Mean Squared Error measures the average squared difference between actual and predicted values.",

        "example": "MSE = average of (actual - predicted)^2.",

        "syntax": "MSE = Σ(actual - predicted)² / n"

    },



    "model training": {

        "category": "Machine Learning",

        "definition": "Model training is the process of learning patterns from training data.",

        "example": "model.fit(X_train, y_train)",

        "syntax": "model.fit(X_train, y_train)"

    },



    "prediction": {

        "category": "Machine Learning",

        "definition": "Prediction is the process of using a trained model to estimate an output for new data.",

        "example": "prediction = model.predict(X_test)",

        "syntax": "model.predict(new_data)"

    },





    # --------------------------------------------------------

    # NLP

    # --------------------------------------------------------



    "nlp": {

        "category": "Natural Language Processing",

        "definition": "Natural Language Processing enables computers to process, understand and work with human language.",

        "example": "A chatbot that understands user questions is an NLP application.",

        "syntax": "Text → NLP processing → Meaning"

    },



    "tokenization": {

        "category": "Natural Language Processing",

        "definition": "Tokenization splits text into smaller units such as words or sentences.",

        "example": 'text = "I love Python"\nwords = text.split()\nprint(words)',

        "syntax": "Text → Tokens"

    },



    "stop words": {

        "category": "Natural Language Processing",

        "definition": "Stop words are common words that are often removed during NLP preprocessing because they may contribute less useful information.",

        "example": "Words such as 'the', 'is' and 'a' may be treated as stop words depending on the task.",

        "syntax": "Text → Remove selected common words"

    },



    "stemming": {

        "category": "Natural Language Processing",

        "definition": "Stemming reduces words to a simpler root-like form by removing prefixes or suffixes.",

        "example": "Words such as 'playing' and 'played' may be reduced to a common stem.",

        "syntax": "Word → Stem"

    },



    "lemmatization": {

        "category": "Natural Language Processing",

        "definition": "Lemmatization converts words into their meaningful base or dictionary form.",

        "example": "The words 'running' and 'ran' can be related to the lemma 'run' depending on linguistic analysis.",

        "syntax": "Word → Dictionary form"

    },



    "text classification": {

        "category": "Natural Language Processing",

        "definition": "Text classification assigns text to predefined categories.",

        "example": "Classify customer messages as complaint, feedback or query.",

        "syntax": "Text → Features → Class"

    },



    "chatbot": {

        "category": "Natural Language Processing",

        "definition": "A chatbot is a software system that communicates with users through natural language.",

        "example": "A Python chatbot can classify a question and return an appropriate answer.",

        "syntax": "User input → Processing → Response"

    },



    "sentiment analysis": {

        "category": "Natural Language Processing",

        "definition": "Sentiment analysis identifies the emotional or opinion-related polarity of text.",

        "example": 'The sentence "This product is excellent" can be classified as positive sentiment.',

        "syntax": "Text → Positive/Negative/Neutral"

    },





    # --------------------------------------------------------

    # DATABASE / WEB

    # --------------------------------------------------------



    "sql": {

        "category": "Database",

        "definition": "SQL is a language used to create, retrieve, update and manage data in relational databases.",

        "example": "SELECT * FROM students;",

        "syntax": "SELECT column FROM table;"

    },



    "sqlite": {

        "category": "Database",

        "definition": "SQLite is a lightweight relational database engine that can be used directly from Python.",

        "example": 'import sqlite3\nconnection = sqlite3.connect("students.db")',

        "syntax": "sqlite3.connect()"

    },



    "api": {

        "category": "Web Development",

        "definition": "An API allows different software applications to communicate with each other.",

        "example": "A weather application can request weather data from a weather API.",

        "syntax": "Client → API → Server → Response"

    },



    "flask": {

        "category": "Web Development",

        "definition": "Flask is a lightweight Python web framework used to build web applications and APIs.",

        "example": 'from flask import Flask\napp = Flask(__name__)\n\n@app.route("/")\ndef home():\n    return "Hello"',

        "syntax": "Flask(__name__)"

    },



    "django": {

        "category": "Web Development",

        "definition": "Django is a high-level Python web framework designed for building web applications.",

        "example": "Django can be used to create database-driven websites.",

        "syntax": "django-admin startproject project"

    },





    # --------------------------------------------------------

    "cloud computing": {
        "category": "Technology",
        "definition": "Cloud computing is the delivery of computing services such as servers, storage, databases and software over the internet.",
        "example": "Examples include online file storage, cloud databases and applications running on cloud servers.",
        "syntax": "User → Internet → Cloud Service"
    },


    # PROJECTS

    # --------------------------------------------------------



    "project": {

        "category": "Projects",

        "definition": "A Python project combines programming concepts to solve a practical problem.",

        "example": "Student Management System, chatbot, calculator and expense tracker are common Python projects.",

        "syntax": "Problem → Design → Code → Test → Deploy"

    },



    "student management system": {

        "category": "Projects",

        "definition": "A Student Management System is a project used to store and manage student information.",

        "example": "It can contain features for adding, updating, searching and deleting student records.",

        "syntax": "Student → Add → Search → Update → Delete"

    },



    "resume screening": {

        "category": "Projects",

        "definition": "An AI resume screening system analyzes resumes and compares candidate information with job requirements.",

        "example": "A system can extract skills from resumes and calculate a similarity score with a job description.",

        "syntax": "Resume → NLP → Skills → Matching → Result"

    },



    "sign language": {

        "category": "Projects",

        "definition": "A sign language recognition system uses computer vision and machine learning to recognize hand gestures and convert them into meaningful output.",

        "example": "A camera can capture a hand gesture and a trained model can classify it as a predefined sign.",

        "syntax": "Camera → Hand Detection → ML Model → Text/Speech"

    },





    # --------------------------------------------------------

    # INTERVIEW

    # --------------------------------------------------------



    "python interview": {

        "category": "Interview",

        "definition": "Python interviews commonly test programming fundamentals, data structures, functions, OOP, exceptions and practical problem solving.",

        "example": "Common questions include: What is Python? What is a list? What is inheritance?",

        "syntax": "Concept → Explanation → Example"

    },



    "coding interview": {

        "category": "Interview",

        "definition": "A coding interview evaluates programming logic, problem-solving ability and implementation skills.",

        "example": "A common beginner problem is finding whether a number is even or odd.",

        "syntax": "Understand → Plan → Code → Test"

    }

}





# ============================================================

# ============================================================
# DEEP PYTHON INTERNALS
# ============================================================

DEEP_TOPICS = {
    "garbage collection": {"category": "Deep Python Internals", "definition": "In CPython, memory is primarily reclaimed through reference counting. A cyclic garbage collector also detects unreachable groups of objects that reference each other.", "example": "import gc\na = []\na.append(a)\ndel a\ngc.collect()", "syntax": "import gc; gc.collect()"},
    "memory management": {"category": "Deep Python Internals", "definition": "Python manages memory automatically. In CPython, objects live in a private heap managed by Python's memory allocator, with reference counting and cyclic garbage collection used for reclamation.", "example": "a = [1, 2, 3]\nb = a\ndel b", "syntax": "object creation -> references -> reclamation"},
    "reference counting": {"category": "Deep Python Internals", "definition": "Reference counting tracks how many references point to an object. In CPython, when the count reaches zero, the object can usually be deallocated immediately.", "example": "a = []\nb = a\ndel b\ndel a", "syntax": "reference_count -> 0 -> deallocation"},
    "circular reference": {"category": "Deep Python Internals", "definition": "A circular reference occurs when objects reference each other directly or indirectly. Reference counting alone cannot reclaim such cycles, so the cyclic garbage collector can detect unreachable cycles.", "example": "a = []\nb = []\na.append(b)\nb.append(a)\ndel a\ndel b", "syntax": "A -> B -> A"},
    "string immutability": {"category": "Deep Python Internals", "definition": "Python strings are immutable: an existing string object cannot be changed in place. Operations that appear to modify a string create or return another string. This also supports safe hashing and dictionary keys.", "example": 's = "Python"\ns = s + " 3"\nprint(s)', "syntax": "new_string = old_string + text"},
    "shallow copy": {"category": "Deep Python Internals", "definition": "A shallow copy creates a new outer object but keeps references to the same nested objects.", "example": "import copy\na = [[1, 2], [3, 4]]\nb = copy.copy(a)", "syntax": "copy.copy(object)"},
    "deep copy": {"category": "Deep Python Internals", "definition": "A deep copy recursively copies nested objects, so changes to nested mutable objects in the copy normally do not affect the original.", "example": "import copy\na = [[1, 2], [3, 4]]\nb = copy.deepcopy(a)", "syntax": "copy.deepcopy(object)"},
    "dictionary internals": {"category": "Deep Python Internals", "definition": "Python dictionaries are hash tables. A key's hash helps locate a slot, while equality checks distinguish keys when needed. Modern CPython dictionaries preserve insertion order.", "example": 'student = {"name": "Python", "age": 30}\nprint(student["name"])', "syntax": "dictionary[key] -> hash -> lookup"},
    "hashing": {"category": "Deep Python Internals", "definition": "Hashing converts a hashable object into an integer hash value used by dictionaries and sets. Keys need a stable hash/equality relationship.", "example": 'print(hash("Python"))\nd = {"Python": 1}', "syntax": "hash(object)"},
    "generator memory": {"category": "Deep Python Internals", "definition": "Generators produce values lazily and preserve execution state between yield points, so large sequences do not have to be stored completely in memory.", "example": "def numbers():\n    for i in range(1000000):\n        yield i", "syntax": "yield value"},
    "decorator internals": {"category": "Deep Python Internals", "definition": "A decorator receives a function or class and returns a replacement or wrapped object. The @decorator syntax applies it when the decorated definition is created.", "example": "def log(func):\n    def wrapper(*args, **kwargs):\n        return func(*args, **kwargs)\n    return wrapper\n\n@log\ndef add(a, b):\n    return a + b", "syntax": "decorated = decorator(original)"},
    "method resolution order": {"category": "Deep Python Internals", "definition": "Method Resolution Order (MRO) is the order Python follows when searching for methods and attributes in a class hierarchy. Python uses C3 linearization.", "example": "class A: pass\nclass B(A): pass\nprint(B.mro())", "syntax": "ClassName.mro()"},
    "new vs init": {"category": "Deep Python Internals", "definition": "__new__ creates or returns an instance, while __init__ initializes an already-created instance. __new__ is especially important for immutable types and custom instance creation.", "example": "class A:\n    def __new__(cls):\n        return super().__new__(cls)\n    def __init__(self):\n        self.value = 10", "syntax": "__new__ -> instance -> __init__"},
    "context manager": {"category": "Deep Python Internals", "definition": "A context manager controls setup and cleanup around a block of code. A class-based context manager uses __enter__ and __exit__ with the with statement.", "example": "with open(\"data.txt\") as file:\n    data = file.read()", "syntax": "with expression as target:"},
    "bytecode": {"category": "Deep Python Internals", "definition": "Python source code is compiled to bytecode instructions executed by the Python virtual machine. The dis module can inspect bytecode.", "example": "import dis\ndef add(a, b):\n    return a + b\ndis.dis(add)", "syntax": "dis.dis(function)"},
    "gil": {"category": "Deep Python Internals", "definition": "The Global Interpreter Lock (GIL) in traditional CPython builds allows only one thread at a time to execute Python bytecode within a process. Threads can still be useful for I/O-bound work.", "example": "import threading\n# Threads are commonly useful for I/O-bound tasks.", "syntax": "threading.Thread(target=function)"},
    "async event loop": {"category": "Deep Python Internals", "definition": "Python's asyncio event loop schedules asynchronous tasks. Coroutines can suspend at await points, allowing other ready tasks to run while waiting for I/O.", "example": "import asyncio\nasync def main():\n    await asyncio.sleep(1)\nasyncio.run(main())", "syntax": "async def -> await -> event loop"},
    "string interning": {"category": "Deep Python Internals", "definition": "String interning allows some identical strings to share an object. It can reduce memory use, but code should use == for value comparison rather than relying on object identity.", "example": 'a = "python"\nb = "python"\nprint(a == b)', "syntax": "value equality: =="},
    "list internals": {"category": "Deep Python Internals", "definition": "A Python list is a dynamic array of object references. Extra capacity can make repeated append operations efficient on average.", "example": "numbers = []\nfor i in range(5):\n    numbers.append(i)", "syntax": "list.append(value)"},
    "slots": {"category": "Deep Python Internals", "definition": "__slots__ can declare a fixed set of instance attributes and may reduce per-instance memory usage by avoiding a normal instance __dict__ in suitable classes.", "example": "class Student:\n    __slots__ = (\"name\", \"age\")", "syntax": "__slots__ = (\"attribute\", ...)"},
    "descriptor": {"category": "Deep Python Internals", "definition": "A descriptor implements methods such as __get__, __set__, or __delete__. Descriptors power features such as properties and methods.", "example": "class A:\n    @property\n    def value(self):\n        return 10", "syntax": "__get__ / __set__ / __delete__"},
    "property": {"category": "Deep Python Internals", "definition": "property() creates a managed attribute interface, allowing getter, setter, or deleter logic while keeping attribute-style syntax.", "example": "class Student:\n    @property\n    def age(self):\n        return self._age", "syntax": "@property"},
    "metaclass": {"category": "Deep Python Internals", "definition": "A metaclass is the class of a class. Python normally uses type as the metaclass, and custom metaclasses can control class creation.", "example": "class MyMeta(type):\n    pass", "syntax": "class MyMeta(type):"},
}

TOPICS.update(DEEP_TOPICS)

# ALIASES

# ============================================================



ALIASES = {


    "how does garbage collection work in python": "garbage collection",
    "python garbage collection": "garbage collection",
    "garbage collector": "garbage collection",
    "how is memory managed in python": "memory management",
    "python memory management": "memory management",
    "how does reference counting work": "reference counting",
    "circular references": "circular reference",
    "why are strings immutable": "string immutability",
    "why are strings immutable in python": "string immutability",
    "string immutable": "string immutability",
    "shallow copy vs deep copy": "shallow copy",
    "how does dictionary lookup work internally": "dictionary internals",
    "how does hashing work": "hashing",
    "how does a decorator work internally": "decorator internals",
    "mro": "method resolution order",
    "new vs init": "new vs init",
    "__new__ vs __init__": "new vs init",
    "context managers": "context manager",
    "python bytecode": "bytecode",
    "global interpreter lock": "gil",
    "event loop": "async event loop",
    "asyncio event loop": "async event loop",
    "string interning": "string interning",
    "list internals": "list internals",
    "__slots__": "slots",
    "descriptors": "descriptor",
    "metaclasses": "metaclass",






    "what is python language": "python",

    "python programming": "python",

    "python basics": "python",



    "variables": "variable",

    "data types": "data type",

    "datatype": "data type",



    "ints": "integer",

    "integer datatype": "integer",



    "strings": "string",

    "bool": "boolean",



    "type conversion": "type casting",

    "casting": "type casting",



    "operators": "operator",

    "arithmetic operators": "arithmetic operator",

    "comparison operators": "comparison operator",

    "logical operators": "logical operator",



    "conditions": "if statement",

    "if condition": "if statement",

    "if else statement": "if else",

    "elif": "if elif else",

    "else if": "if elif else",



    "loops": "for loop",

    "loop": "for loop",

    "for loops": "for loop",

    "while loops": "while loop",



    "lists": "list",

    "tuples": "tuple",

    "sets": "set",

    "dictionaries": "dictionary",

    "dict": "dictionary",



    "functions": "function",

    "parameters": "parameter",

    "arguments": "argument",

    "return": "return statement",

    "anonymous function": "lambda",



    "oops": "object-oriented programming",

    "oop": "object-oriented programming",

    "classes": "class",

    "objects": "object",



    "inherit": "inheritance",

    "polymorphism concept": "polymorphism",

    "encapsulation concept": "encapsulation",



    "errors": "exception",

    "error handling": "exception",

    "exception handling": "try except",



    "files": "file handling",

    "file handling in python": "file handling",



    "libraries": "numpy",

    "numpy library": "numpy",

    "pandas library": "pandas",



    "machine learning": "machine learning",

    "ml": "machine learning",

    "supervised": "supervised learning",

    "unsupervised": "unsupervised learning",

    "random forest algorithm": "random forest",

    "decision trees": "decision tree",



    "natural language processing": "nlp",

    "nlp concept": "nlp",

    "word tokenization": "tokenization",

    "tokens": "tokenization",



    "data analysis": "data analysis",

    "data analytics": "data analysis",



    "standard deviation": "standard deviation",

    "sd": "standard deviation",



    "regular expressions": "regular expression",

    "regex": "regular expression",



    "api development": "api",



    "web framework flask": "flask",



    "recursive function": "recursion",
"projects": "project",
    "cloud": "cloud computing",
    "cloud computing service": "cloud computing",
    "cloud computing services": "cloud computing"

}





# ============================================================

# NORMALIZE TEXT

# ============================================================



def normalize(text):

    text = text.lower().strip()

    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text





# ============================================================

# FIND TOPIC

# ============================================================



def find_topic(question):



    normalized = normalize(question)



    # First check aliases.

    for alias in sorted(ALIASES, key=len, reverse=True):

        if alias in normalized:

            return ALIASES[alias]



    # Then check actual topic names.

    for topic in sorted(TOPICS, key=len, reverse=True):

        if topic in normalized:

            return topic



    return None





# ============================================================

# LOAD DATASET

# ============================================================



def load_dataset():



    if not os.path.exists(DATA_FILE):

        return []



    try:

        with open(DATA_FILE, "r", encoding="utf-8") as file:

            data = json.load(file)



        if isinstance(data, list):

            return data



        return []



    except Exception:

        return []





DATASET = load_dataset()





# ============================================================

# PREPARE DATASET FOR ML SEARCH

# ============================================================



dataset_questions = []

dataset_answers = []

dataset_categories = []





for item in DATASET:



    if not isinstance(item, dict):

        continue



    question = item.get("question", "")

    answer = item.get("answer", "")

    category = item.get("category", "General")



    if question and answer:

        dataset_questions.append(question)

        dataset_answers.append(answer)

        dataset_categories.append(category)





if dataset_questions:



    vectorizer = TfidfVectorizer(

        lowercase=True,

        stop_words="english"

    )



    question_vectors = vectorizer.fit_transform(

        dataset_questions

    )



else:



    vectorizer = None

    question_vectors = None





# ============================================================

# GET TOPIC CATEGORY

# ============================================================



def get_category(topic):



    if topic in TOPICS:

        return TOPICS[topic]["category"]



    return "General"





# ============================================================

# CODE REQUEST DETECTION

# ============================================================



def is_code_request(question):



    patterns = [

        "give code",

        "give me code",

        "write code",

        "write a program",

        "program for",

        "python code",

        "code for",

        "how to code",

        "show code",

        "coding example"

    ]



    normalized = normalize(question)



    return any(pattern in normalized for pattern in patterns)





# ============================================================

# COMPARISON DETECTION

# ============================================================



def find_comparison(question):



    normalized = normalize(question)



    if " vs " in normalized:



        parts = normalized.split(" vs ")



        if len(parts) == 2:

            left = parts[0].strip()

            right = parts[1].strip()



            left_topic = find_topic(left)

            right_topic = find_topic(right)



            if left_topic and right_topic:

                return left_topic, right_topic



    if "difference between" in normalized:



        text = normalized.replace(

            "difference between",

            ""

        )



        parts = text.split(" and ")



        if len(parts) == 2:



            left_topic = find_topic(parts[0])

            right_topic = find_topic(parts[1])



            if left_topic and right_topic:

                return left_topic, right_topic



    return None





# ============================================================

# COMPARISON ANSWER

# ============================================================



def comparison_answer(topic1, topic2):



    first = TOPICS[topic1]

    second = TOPICS[topic2]



    answer = (

        f"{topic1.title()} vs {topic2.title()}\n\n"

        f"{topic1.title()}:\n"

        f"{first['definition']}\n\n"

        f"{topic2.title()}:\n"

        f"{second['definition']}\n\n"

        "Main difference:\n"

        f"{topic1.title()} and {topic2.title()} are different "

        "Python concepts with different purposes."

    )



    return {

        "answer": answer,

        "category": "Comparison",

        "confidence": 1.0,

        "matched_question": f"{topic1} vs {topic2}"

    }





# ============================================================

# SIMPLE EXPLANATION

# ============================================================



def is_simple_request(question):



    normalized = normalize(question)



    patterns = [

        "explain simply",

        "explain in simple words",

        "simple explanation",

        "explain easy",

        "easy explanation",

        "explain for beginner"

    ]



    return any(pattern in normalized for pattern in patterns)





# ============================================================

# EXAMPLE REQUEST

# ============================================================



def is_example_request(question):



    normalized = normalize(question)



    patterns = [

        "example",

        "give example",

        "give me example",

        "show example",

        "code example",

        "program example"

    ]



    return any(pattern in normalized for pattern in patterns)





# ============================================================

# GET ANSWER

# ============================================================



def get_answer(question):



    # --------------------------------------------------------

    # SPECIAL PYTHON HISTORY QUESTIONS

    # --------------------------------------------------------



    normalized_question = normalize(question)



    if "who invented python" in normalized_question:

        return {

            "answer": (

                "Python was created by Guido van Rossum. "

                "He started developing Python in the late 1980s, "

                "and the first public release was made in 1991."

            ),

            "category": "Python History",

            "confidence": 1.0,

            "matched_question": "who invented python"

        }



    if "who created python" in normalized_question:

        return {

            "answer": "Python was created by Guido van Rossum.",

            "category": "Python History",

            "confidence": 1.0,

            "matched_question": "who created python"

        }



    if "when was python created" in normalized_question:

        return {

            "answer": (

                "Python was started by Guido van Rossum "

                "in the late 1980s, and its first public release "

                "was in 1991."

            ),

            "category": "Python History",

            "confidence": 1.0,

            "matched_question": "when was python created"

        }





    # --------------------------------------------------------

    # SPECIAL RECURSION QUESTIONS
    # --------------------------------------------------------

    if (
        "what is recursion" in normalized_question
        or "explain recursion" in normalized_question
        or normalized_question.strip() == "recursion"
    ):
        data = TOPICS["recursion"]

        return {
            "answer": data["definition"],
            "category": data["category"],
            "confidence": 1.0,
            "matched_question": "recursion"
        }


    # --------------------------------------------------------

    # COMPARISON

    # --------------------------------------------------------



    comparison = find_comparison(question)



    if comparison:



        return comparison_answer(

            comparison[0],

            comparison[1]

        )





    # --------------------------------------------------------

    # TOPIC MATCH

    # --------------------------------------------------------



    topic = find_topic(question)



    if topic:



        data = TOPICS[topic]



        # Code request

        if is_code_request(question):



            return {

                "answer": data["example"],

                "category": data["category"],

                "confidence": 1.0,

                "matched_question": topic

            }



        # Simple explanation

        if is_simple_request(question):



            answer = (

                f"Simple explanation:\n"

                f"{data['definition']}\n\n"

                f"Example:\n"

                f"{data['example']}"

            )



            return {

                "answer": answer,

                "category": data["category"],

                "confidence": 1.0,

                "matched_question": topic

            }



        # Example request

        if is_example_request(question):



            return {

                "answer": data["example"],

                "category": data["category"],

                "confidence": 1.0,

                "matched_question": topic

            }



        # Normal definition

        return {

            "answer": data["definition"],

            "category": data["category"],

            "confidence": 1.0,

            "matched_question": topic

        }





    # --------------------------------------------------------

    # ML / TF-IDF FALLBACK

    # --------------------------------------------------------



    if vectorizer is not None:



        try:



            processed = preprocess(question)



            query_text = processed["processed"]



            query_vector = vectorizer.transform(

                [query_text]

            )



            similarities = cosine_similarity(

                query_vector,

                question_vectors

            )[0]



            best_index = similarities.argmax()

            best_score = similarities[best_index]



            if best_score >= 0.25:



                return {

                    "answer": dataset_answers[best_index],

                    "category": dataset_categories[best_index],

                    "confidence": float(best_score),

                    "matched_question": dataset_questions[best_index]

                }



        except Exception:

            pass





    # --------------------------------------------------------

    # UNKNOWN QUESTION

    # --------------------------------------------------------



    return {

        "answer": (

            "I'm not fully sure about that question yet. "

            "Try asking about Python, loops, lists, functions, "

            "OOP, Pandas, NumPy, Machine Learning, NLP, "

            "projects or interview questions."

        ),

        "category": "Unknown",

        "confidence": 0.0

    }



    # --------------------------------------------------------


# CONTEXT / FOLLOW-UP ANSWER

# ============================================================



def get_context_answer(

    question,

    last_question=None,

    last_category=None

):



    normalized = normalize(question)



    follow_up_patterns = [

        "example",

        "give example",

        "give me example",

        "show example",

        "real world example",



        "code",

        "give code",

        "show code",

        "write code",

        "program",



        "syntax",

        "how to write",



        "explain it",

        "explain this",

        "how does it work",

        "why is it useful",

        "why is it important",

        "advantages"

    ]



    is_follow_up = any(

        pattern in normalized

        for pattern in follow_up_patterns

    )



    if not is_follow_up:

        return get_answer(question)



    if not last_question:

        return get_answer(question)



    previous_topic = find_topic(last_question)



    if not previous_topic:

        return get_answer(question)



    data = TOPICS[previous_topic]



    # Syntax / how to write

    if (

        "syntax" in normalized

        or "how to write" in normalized

    ):

        return {

            "answer": data["syntax"],

            "category": data["category"],

            "confidence": 1.0,

            "matched_question": previous_topic

        }



    # Code / program request

    if (

        "code" in normalized

        or "program" in normalized

        or "write code" in normalized

        or "show code" in normalized

    ):

        return {

            "answer": data["example"],

            "category": data["category"],

            "confidence": 1.0,

            "matched_question": previous_topic

        }



    # Explanation / why / how

    if (

        "explain" in normalized

        or "how does it work" in normalized

        or "why is it useful" in normalized

        or "why is it important" in normalized

        or "advantages" in normalized

    ):

        answer = (

            f"{data['definition']}\n\n"

            f"Example:\n"

            f"{data['example']}"

        )



        return {

            "answer": answer,

            "category": data["category"],

            "confidence": 1.0,

            "matched_question": previous_topic

        }



    # Example request

    return {

        "answer": data["example"],

        "category": data["category"],

        "confidence": 1.0,

        "matched_question": previous_topic

    }





# ============================================================

# TEST

# ============================================================



if __name__ == "__main__":



    test_questions = [

        "what is python",

        "what is list",

        "what is inheritance",

        "what is pandas",

        "what is random forest",

        "what is tokenization",

        "list vs tuple"

    ]



    print("=" * 60)

    print("          CHATBOT ENGINE TEST")

    print("=" * 60)



    for question in test_questions:



        result = get_answer(question)



        print()

        print("Question:", question)

        print("Answer:", result["answer"])

        print("Category:", result["category"])

        print("Confidence:", result["confidence"])



    print()

    print("=" * 60)