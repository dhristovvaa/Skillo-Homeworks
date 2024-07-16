# Problem 1 numbers.txt.py
def calculate_sum_from_file(filename):
    try:
        with open(filename, 'r') as file:
            total_sum = 0
            for line in file:
                total_sum += int(line.strip())
        return total_sum
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return None
    except ValueError:
        print("The file contains non-integer values.")
        return None


def main():
    filename = 'numbers.txt.py'
    total_sum = calculate_sum_from_file(filename)
    if total_sum is not None:
        print(f"The sum of the numbers in {filename} is: {total_sum}")


if __name__ == "__main__":
    main()


# Problem 2
def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
        return word_count
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return None


def main():
    filename = 'words.txt.py'
    word_count = count_words_in_file(filename)
    if word_count is not None:
        print(f"The number of words in {filename} is: {word_count}")


if __name__ == "__main__":
    main()

# problem 3
import csv


def write_student_scores_to_csv(filename):
    # Prompt the user to enter student names and scores
    student_data = []
    while True:
        name = input("Enter student name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        score = input("Enter student score: ")
        student_data.append([name, score])

    # Write student data to CSV file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Score'])
        writer.writerows(student_data)
    print(f"Student scores have been written to {filename}")


def main():
    filename = 'student_scores.csv'
    write_student_scores_to_csv(filename)


if __name__ == "__main__":
    main()

# Problem 4
import csv


def calculate_total_salaries(input_file, output_file):
    # Read employee data from CSV file
    with open(input_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        employee_data = list(reader)

    # Calculate total salary for each employee
    for employee in employee_data:
        base_salary = float(employee['Base Salary'])
        bonuses = float(employee['Bonuses'])
        total_salary = base_salary + bonuses
        employee['Total Salary'] = total_salary

    # Write total salaries to a new CSV file
    with open(output_file, 'w', newline='') as file:
        fieldnames = ['Employee ID', 'Name', 'Base Salary', 'Bonuses', 'Total Salary']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(employee_data)
    print(f"Total salaries have been calculated and saved in {output_file}")


def main():
    input_file = 'employee_data.csv.'
    output_file = 'total_salaries.csv'
    calculate_total_salaries(input_file, output_file)


if __name__ == "__main__":
    main()

#Problem 5

import json


with open('products.json.py', 'r') as file:
    products = json.load(file)


total_cost = sum(product['price'] for product in products)


print(f"The total cost of all products is: ${total_cost:.2f}")

#Problem 6

import json


def read_contacts(file_path):
    try:


        with open(file_path, 'r') as file:
            contacts = json.load(file)


        for contact in contacts:
            print(f"Name: {contact['name']}")
            print(f"Email: {contact['email']}")
            print(f"Phone: {contact['phone']}")
            print()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON file.")
    except KeyError as e:
        print(f"Error: Missing key {e} in one of the contacts.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    file_path = 'contacts.json.py'
    read_contacts(file_path)

#Problem 7

import csv
import json



def calculate_average(scores):
    return sum(scores.values()) / len(scores)



def read_student_data(file_path):
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                name = row['name']
                try:
                    scores = json.loads(row['scores'])
                    average_score = calculate_average(scores)
                    print(f"Student: {name}, Average Score: {average_score:.2f}")
                except json.JSONDecodeError:
                    print(f"Error: The scores for student '{name}' are not valid JSON: {row['scores']}")
                except Exception as e:
                    print(f"An unexpected error occurred while processing scores for '{name}': {e}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    file_path = 'student_data.csv.py'
    read_student_data(file_path)

#Problem 9

import xml.etree.ElementTree as ET

def read_inventory(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for product in root.findall('product'):
        name = product.find('name').text
        price = product.find('price').text
        print(f'Product: {name}, Price: {price}')

# Example usage
if __name__ == "__main__":
    read_inventory('inventory.xml.py')

#inventory.xml.py