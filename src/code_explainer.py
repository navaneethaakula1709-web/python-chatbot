# ============================================
# CODE EXPLAINER
# Python QA Chatbot
# ============================================


EXPLANATIONS = {

    "factorial": {
        "title": "Factorial Program",
        "explanation": """
1. def factorial(n):
   → Creates a function named factorial that accepts n.

2. if n == 0 or n == 1:
   → Checks the base condition.

3. return 1
   → Factorial of 0 and 1 is 1.

4. return n * factorial(n - 1)
   → The function calls itself with n - 1.
   → This is called recursion.

5. number = int(input(...))
   → Gets a number from the user.

6. factorial(number)
   → Calls the factorial function.

7. print(...)
   → Displays the final factorial.
"""
    },

    "fibonacci": {
        "title": "Fibonacci Program",
        "explanation": """
1. n = int(input(...))
   → Gets the number of terms from the user.

2. a = 0
   → Stores the first Fibonacci number.

3. b = 1
   → Stores the second Fibonacci number.

4. for i in range(n):
   → Repeats the process n times.

5. print(a)
   → Prints the current Fibonacci number.

6. a, b = b, a + b
   → Updates the two numbers to generate the next term.
"""
    },

    "prime": {
        "title": "Prime Number Program",
        "explanation": """
1. number = int(input(...))
   → Gets a number from the user.

2. if number <= 1:
   → Numbers less than or equal to 1 are not prime.

3. is_prime = True
   → Initially assumes the number is prime.

4. for i in range(2, number):
   → Checks possible divisors.

5. if number % i == 0:
   → Checks whether the number is exactly divisible by i.

6. is_prime = False
   → If divisible, the number is not prime.

7. break
   → Stops the loop once a divisor is found.

8. print(...)
   → Displays whether the number is prime.
"""
    },

    "palindrome": {
        "title": "Palindrome Program",
        "explanation": """
1. text = input(...)
   → Gets a string from the user.

2. text[::-1]
   → Reverses the string using slicing.

3. if text == text[::-1]:
   → Compares the original string with its reverse.

4. print("Palindrome")
   → If both are equal, it is a palindrome.

5. Otherwise:
   → The string is not a palindrome.
"""
    },

    "reverse": {
        "title": "Reverse String Program",
        "explanation": """
1. text = input(...)
   → Gets a string from the user.

2. text[::-1]
   → Uses Python slicing to reverse the string.

3. reversed_text = text[::-1]
   → Stores the reversed string.

4. print(...)
   → Displays the reversed string.
"""
    },

    "even odd": {
        "title": "Even or Odd Program",
        "explanation": """
1. number = int(input(...))
   → Gets a number from the user.

2. number % 2
   → Finds the remainder after dividing by 2.

3. if number % 2 == 0:
   → If the remainder is 0, the number is even.

4. else:
   → Otherwise, the number is odd.

5. print(...)
   → Displays the result.
"""
    },

    "armstrong": {
        "title": "Armstrong Number Program",
        "explanation": """
1. number = int(input(...))
   → Gets a number from the user.

2. original = number
   → Stores the original number.

3. digits = len(str(number))
   → Counts the number of digits.

4. while number > 0:
   → Processes each digit.

5. digit = number % 10
   → Extracts the last digit.

6. total += digit ** digits
   → Adds the digit raised to the power of the number of digits.

7. number //= 10
   → Removes the last digit.

8. total == original
   → Checks whether the number is an Armstrong number.
"""
    },

    "sum digits": {
        "title": "Sum of Digits Program",
        "explanation": """
1. number = int(input(...))
   → Gets a number from the user.

2. total = 0
   → Creates a variable to store the sum.

3. while number > 0:
   → Processes each digit.

4. digit = number % 10
   → Gets the last digit.

5. total += digit
   → Adds the digit to the total.

6. number //= 10
   → Removes the last digit.

7. print(...)
   → Displays the sum of all digits.
"""
    },

    "leap year": {
        "title": "Leap Year Program",
        "explanation": """
1. year = int(input(...))
   → Gets a year from the user.

2. year % 400 == 0
   → Checks whether the year is divisible by 400.

3. year % 4 == 0
   → Checks whether the year is divisible by 4.

4. year % 100 != 0
   → Makes sure century years are handled correctly.

5. if condition:
   → If the complete condition is true, it is a leap year.

6. else:
   → Otherwise, it is not a leap year.
"""
    },

    "largest": {
        "title": "Largest Number Program",
        "explanation": """
1. a, b, c
   → Stores three numbers entered by the user.

2. max(a, b, c)
   → Python's max() function finds the largest value.

3. largest = max(a, b, c)
   → Stores the largest number.

4. print(...)
   → Displays the largest number.
"""
    }
}


def get_explanation(topic):

    topic = topic.lower().strip()

    if topic in EXPLANATIONS:
        return EXPLANATIONS[topic]["explanation"]

    for key in EXPLANATIONS:

        if key in topic:
            return EXPLANATIONS[key]["explanation"]

    return None


def detect_explanation_topic(question):

    question = question.lower()

    if "factorial" in question:
        return "factorial"

    if "fibonacci" in question:
        return "fibonacci"

    if "prime" in question:
        return "prime"

    if "palindrome" in question:
        return "palindrome"

    if "reverse" in question:
        return "reverse"

    if "even" in question or "odd" in question:
        return "even odd"

    if "armstrong" in question:
        return "armstrong"

    if "sum of digits" in question:
        return "sum digits"

    if "leap year" in question:
        return "leap year"

    if "largest" in question:
        return "largest"

    return None


def explain_code(question):

    topic = detect_explanation_topic(question)

    if topic is None:
        return None

    explanation = get_explanation(topic)

    if explanation is None:
        return None

    return {
        "answer": explanation,
        "category": "Code Explanation",
        "confidence": 1.0,
        "matched_question": topic
    }


if __name__ == "__main__":

    print("=" * 60)
    print("                 CODE EXPLAINER")
    print("=" * 60)

    while True:

        question = input("\nEnter topic: ").strip()

        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        result = explain_code(question)

        if result:
            print("\nExplanation:")
            print(result["answer"])
        else:
            print("\nNo explanation available for that topic.")