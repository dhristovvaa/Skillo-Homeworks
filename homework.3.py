# Problem 0:

num = int(input("Enter an integer: "))
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")

# Problem 1:

sum_of_evens = 0
for num in range(1, 101):
    if num % 2 == 0:
        sum_of_evens == num
        print("Sum of even numbers from 1 to 100;", sum_of_evens)


# Problem 2:

def main():
    while True:
        # Prompt the user with the math problem
        answer = input("How much does 5 + 17 equal to? ")

        # Check if the answer is correct
        if answer == "22":
            print("Congratulations! You provided the correct answer.")
            break  # Exit the loop if the answer is correct
        else:
            print("Sorry, that's not the correct answer. Please try again.")


if __name__ == "__main__":
    main()

# Problem 3
# Problem 3:
for num in range(1, 1001):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# Problem 4
# Initialize a flag to keep track of whether the user has guessed the correct number
import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Initialize a flag to keep track of whether the user has guessed the correct number
guessed_correctly = False

# Start the guessing loop
while not guessed_correctly:
    try:
        # Prompt the user to enter their guess
        user_guess = int(input("Guess a number between 1 and 100: "))

        # Check if the guess is too high
        if user_guess > random_number:
            print("Too high! Try again.")
        # Check if the guess is too low
        elif user_guess < random_number:
            print("Too low! Try again.")
        # If the guess is correct
        else:
            print(f"Congratulations! You guessed the correct number: {random_number}")
            guessed_correctly = True
    except ValueError:

        print("Please enter a valid integer.")

# Problem 5
import random


def generate_problem():
    # Generate two random integers between 1 and 20
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    operation = random.choice(['+', '-', '*', '/'])

    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    elif operation == '/':
        # Ensure the result of the division is an integer
        num1 = num2 * random.randint(1, 10)
        correct_answer = num1 // num2

    return num1, num2, operation, correct_answer


while True:
    # Generate a new problem
    num1, num2, operation, correct_answer = generate_problem()

    try:

        user_answer = int(input(f"What is {num1} {operation} {num2}? "))

        # Check if the answer is correct
        if user_answer == correct_answer:
            print("Correct! Well done.")
            break  # Exit the loop
        else:
            print("Incorrect. Please try again.")
    except ValueError:
        # Handle non-integer input
        print("Please enter a valid integer.")

# Problem 6
# Prompt the user to enter an integer
number = int(input("Enter an integer: "))

print(f"Multiplication table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")


# Problem 7
# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


num = int(input("Enter an integer: "))

# Check if the number is prime and print the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Problem 8


n = int(input("Enter the value of 'n': "))

for i in range(1, n + 1):
    # Print the numbers from 1 to i in each row
    for j in range(1, i + 1):
        print(j, end='')
    print()

