# ============================================
# PROGRAMMING PROBLEM SOLVER
# Python QA Chatbot
# ============================================


PROGRAMS = {

    "factorial": {
        "keywords": ["factorial", "factorial program"],
        "title": "Factorial Program",
        "code": '''def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial:", factorial(number))
'''
    },

    "fibonacci": {
        "keywords": ["fibonacci", "fibonacci series", "fibonacci program"],
        "title": "Fibonacci Series",
        "code": '''n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
'''
    },

    "prime": {
        "keywords": ["prime", "prime number", "prime program"],
        "title": "Prime Number Program",
        "code": '''number = int(input("Enter a number: "))

if number <= 1:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
'''
    },

    "palindrome": {
        "keywords": ["palindrome", "palindrome program"],
        "title": "Palindrome Program",
        "code": '''text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
'''
    },

    "reverse string": {
        "keywords": [
            "reverse string",
            "reverse a string",
            "reverse program",
            "string reverse"
        ],
        "title": "Reverse String Program",
        "code": '''text = input("Enter a string: ")

reversed_text = text[::-1]

print("Reversed string:", reversed_text)
'''
    },

    "even odd": {
        "keywords": [
            "even or odd",
            "even odd",
            "check even",
            "check odd",
            "even number",
            "odd number"
        ],
        "title": "Even or Odd Program",
        "code": '''number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
'''
    },

    "armstrong": {
        "keywords": [
            "armstrong",
            "armstrong number",
            "armstrong program"
        ],
        "title": "Armstrong Number Program",
        "code": '''number = int(input("Enter a number: "))

original = number
digits = len(str(number))
total = 0

while number > 0:
    digit = number % 10
    total += digit ** digits
    number //= 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
'''
    },

    "sum digits": {
        "keywords": [
            "sum of digits",
            "sum digits",
            "digits sum"
        ],
        "title": "Sum of Digits Program",
        "code": '''number = int(input("Enter a number: "))

total = 0

while number > 0:
    digit = number % 10
    total += digit
    number //= 10

print("Sum of digits:", total)
'''
    },

    "largest": {
        "keywords": [
            "largest number",
            "largest among",
            "find largest",
            "maximum number"
        ],
        "title": "Largest Number Program",
        "code": '''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = max(a, b, c)

print("Largest number:", largest)
'''
    },

    "leap year": {
        "keywords": [
            "leap year",
            "check leap year",
            "leap year program"
        ],
        "title": "Leap Year Program",
        "code": '''year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
'''
    },

    "swap": {
        "keywords": [
            "swap numbers",
            "swap two numbers",
            "swapping program"
        ],
        "title": "Swap Two Numbers",
        "code": '''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
'''
    },

    "count vowels": {
        "keywords": [
            "count vowels",
            "number of vowels",
            "vowels in string"
        ],
        "title": "Count Vowels Program",
        "code": '''text = input("Enter a string: ")

count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print("Number of vowels:", count)
'''
    },

    "multiplication table": {
        "keywords": [
            "multiplication table",
            "table program",
            "multiplication program"
        ],
        "title": "Multiplication Table",
        "code": '''number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
'''
    },

    "gcd": {
        "keywords": [
            "gcd",
            "greatest common divisor",
            "hcf",
            "highest common factor"
        ],
        "title": "GCD / HCF Program",
        "code": '''import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = math.gcd(a, b)

print("GCD:", result)
'''
    },

    "lcm": {
        "keywords": [
            "lcm",
            "least common multiple"
        ],
        "title": "LCM Program",
        "code": '''import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = math.lcm(a, b)

print("LCM:", result)
'''
    },

    "calculator": {
        "keywords": [
            "calculator program",
            "simple calculator",
            "calculator"
        ],
        "title": "Simple Calculator",
        "code": '''a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if operator == "+":
    print("Result:", a + b)

elif operator == "-":
    print("Result:", a - b)

elif operator == "*":
    print("Result:", a * b)

elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")
'''
    }
}


def get_program(question):
    """
    Detects a programming problem from the user's question
    and returns the corresponding Python program.
    """

    question_lower = question.lower().strip()

    # Check whether the user is actually asking for a program
    request_words = [
        "code",
        "program",
        "write",
        "implement",
        "python code",
        "give code",
        "give program",
        "how to code"
    ]

    is_program_request = any(
        word in question_lower
        for word in request_words
    )

    if not is_program_request:
        return None

    # Find matching programming problem
    for problem_name, problem_data in PROGRAMS.items():

        for keyword in problem_data["keywords"]:

            if keyword in question_lower:

                answer = (
                    f"Here is the Python program for "
                    f"{problem_data['title']}:\n\n"
                    f"```python\n"
                    f"{problem_data['code']}"
                    f"```\n\n"
                    f"You can copy this program and run it in VS Code."
                )

                return {
                    "answer": answer,
                    "category": "Programming Problems",
                    "confidence": 1.0,
                    "matched_question": problem_data["title"]
                }

    return None


if __name__ == "__main__":

    print("=" * 60)
    print("          PROGRAMMING PROBLEM SOLVER")
    print("=" * 60)

    while True:

        question = input("\nYou: ").strip()

        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        result = get_program(question)

        if result:
            print("\nBot:")
            print(result["answer"])
        else:
            print("\nBot: I don't have a program for that yet.")