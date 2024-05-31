# Problem 0:

def sum_elements(arr):
    result = 0
    for num in arr:
        result += num
        return result


test_lists = [
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50],
    [],
    [-1, -2, -3, -4, -5]
]

for lst in test_lists:
    print(f"Sum of elements in {lst}: {sum_elements(lst)}")


# Problem 1:

def simple_calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"


print("5 + 3 =", simple_calculator(5, 3, '+'))
print("10 - 4 =", simple_calculator(10, 4, '-'))
print("3 * 7 =", simple_calculator(3, 7, '*'))
print("8 / 2 =", simple_calculator(8, 2, '/'))
print("5 / 0 =", simple_calculator(5, 0, '/'))
print("9 % 3 =", simple_calculator(9, 3, '%'))

# Problem 2:
import geometry

# Calculate the area of a square
square_side = 5
square_area = geometry.square_area(square_side)
print("Area of square with side", square_side, "is", square_area)

# Calculate the area of a rectangle using the same function
rectangle_length = 4
rectangle_width = 6
rectangle_area = geometry.rectangle_area(rectangle_length, rectangle_width)
print("Area of rectangle with length", rectangle_length, "and width", rectangle_width, "is", rectangle_area)

# Calculate the area of a triangle
triangle_base = 8
triangle_height = 3
triangle_area = geometry.triangle_area(triangle_base, triangle_height)
print("Area of triangle with base", triangle_base, "and height", triangle_height, "is", triangle_area)

# Calculate the area of a circle
circle_radius = 7
circle_area = geometry.circle_area(circle_radius)
print("Area of circle with radius", circle_radius, "is", circle_area)

# Problem 3:
import temperature_converter


def test_celsius_to_fahrenheit():
    assert temperature_converter.celsius_to_fahrenheit(0) == 32
    assert temperature_converter.celsius_to_fahrenheit(100) == 212
    assert temperature_converter.celsius_to_fahrenheit(-40) == -40
    print("All celsius_to_fahrenheit tests passed.")


def test_fahrenheit_to_celsius():
    assert temperature_converter.fahrenheit_to_celsius(32) == 0
    assert temperature_converter.fahrenheit_to_celsius(212) == 100
    assert temperature_converter.fahrenheit_to_celsius(-40) == -40
    print("All fahrenheit_to_celsius tests passed.")


def run_tests():
    test_celsius_to_fahrenheit()
    test_fahrenheit_to_celsius()


if __name__ == "__main__":
    run_tests()


# Problem 4:

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

    # Test cases


print("Factorial of 0:", factorial(0))
print("Factorial of 1:", factorial(1))
print("Factorial of 5:", factorial(5))
print("Factorial of 10:", factorial(10))

# Problem 5:


shopping_carts = {}

def add_item(customer_id, item, price, quantity):
    if customer_id not in shopping_carts:
        shopping_carts[customer_id] = {}
    if item in shopping_carts[customer_id]:
        shopping_carts[customer_id][item]['quantity'] += quantity
    else:
        shopping_carts[customer_id][item] = {'price': price, 'quantity': quantity}

def remove_item(customer_id, item, quantity):
    if customer_id in shopping_carts and item in shopping_carts[customer_id]:
        if shopping_carts[customer_id][item]['quantity'] > quantity:
            shopping_carts[customer_id][item]['quantity'] -= quantity
        else:
            del shopping_carts[customer_id][item]
        if not shopping_carts[customer_id]:  # if the cart is empty, remove the customer entry
            del shopping_carts[customer_id]

def calculate_total(customer_id):
    if customer_id not in shopping_carts:
        return 0
    total = 0
    for item, details in shopping_carts[customer_id].items():
        total += details['price'] * details['quantity']
    return total

def display_cart(customer_id):
    if customer_id not in shopping_carts or not shopping_carts[customer_id]:
        print("Cart is empty.")
        return
    print("Shopping cart contents:")
    for item, details in shopping_carts[customer_id].items():
        print(f"{item}: ${details['price']} x {details['quantity']} = ${details['price'] * details['quantity']}")
    print(f"Total: ${calculate_total(customer_id)}")

def main():
    while True:
        print("\nOnline Shopping Cart")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Calculate total")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            customer_id = input("Enter customer ID: ")
            item = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            add_item(customer_id, item, price, quantity)
            print(f"Added {quantity} of {item} to the cart.")

        elif choice == '2':
            customer_id = input("Enter customer ID: ")
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            remove_item(customer_id, item, quantity)
            print(f"Removed {quantity} of {item} from the cart.")

        elif choice == '3':
            customer_id = input("Enter customer ID: ")
            display_cart(customer_id)

        elif choice == '4':
            customer_id = input("Enter customer ID: ")
            total = calculate_total(customer_id)
            print(f"Total price for customer {customer_id}: ${total}")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Problem 6

import os

def explore_os_module():
    # Get current working directory
    cwd = os.getcwd()
    print(f"Current Working Directory: {cwd}")

    # List files and directories in the current directory
    files = os.listdir(cwd)
    print("\nFiles and directories in the current directory:")
    for file in files:
        print(file)

    # Create a new directory
    new_dir = os.path.join(cwd, "new_directory")
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
        print(f"\nNew directory created: {new_dir}")
    else:
        print(f"\nDirectory already exists: {new_dir}")

    # Rename a file or directory
    old_name = os.path.join(cwd, "old_name.txt")
    new_name = os.path.join(cwd, "new_name.txt")
    if not os.path.exists(old_name):
        with open(old_name, 'w') as f:
            f.write("Sample file content")
        print(f"\nCreated file: {old_name}")

    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"\nRenamed {old_name} to {new_name}")

    # Get the status of a file or directory
    if os.path.exists(new_name):
        file_status = os.stat(new_name)
        print(f"\nFile status for {new_name}: {file_status}")

    # Execute a system command
    os.system('echo Hello, World!')

    # Get environment variables
    home_dir = os.environ.get('HOME')
    print(f"\nHome Directory: {home_dir}")

    # Walk through a directory tree
    print("\nWalking through the directory tree:")
    for dirpath, dirnames, filenames in os.walk(cwd):
        print(f'Found directory: {dirpath}')
        for file_name in filenames:
            print(f'\t{file_name}')

if __name__ == "__main__":
    explore_os_module()
