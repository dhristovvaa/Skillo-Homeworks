#exercises 1,1.1,2:
list_1_to_10 = list(range(1, 11))
print("List from 1 to 10:", list_1_to_10)

list_1_to_1000 = list(range(1, 1001))
print("List from 1 to 1000:", list_1_to_1000)

reversed_list_1_to_10 = list_1_to_10[::-1]
print("Reversed list from 1 to 10:", reversed_list_1_to_10)


#exercises 3:


words = ["apple", "banana", "orange", "kiwi", "pineapple"]
word_lengths = [len(word) for word in words]
print(word_lengths)

#exercises 3.1:


words = ["apple", "banana", "orange", "kiwi", "pineapple"]
word_lengths_dict = {word: len(word) for word in words}
print(word_lengths_dict)

#exercises 4:

def sum_of_even_numbers(input_list):
    """Return the sum of all even numbers in the list."""
    total = 0

    for num in input_list:
        if num % 2 == 0:
            total += num
    return total

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Sum of even numbers:", sum_of_even_numbers(numbers))

#exercises 5:

def find_max_min(tup):
    """Find the maximum and minimum values in a tuple."""
    max_value = float('-inf')
    min_value = float('inf')

    for num in tup:
        if num > max_value:
            max_value = num

        if num < min_value:
            min_value = num

    return max_value, min_value

numbers = (5, 3, 9, 1, 7, 2, 8)
max_value, min_value = find_max_min(numbers)
print("Maximum value:", max_value)
print("Minimum value:", min_value)

#exercises 6:


queue = []

def enqueue(item):
    """Add an item to the end of the queue."""
    queue.append(item)

def dequeue():
    """Remove and return the first item from the queue."""
    if len(queue) == 0:
        print("Queue is empty.")
        return None
    else:
        return queue.pop(0)

enqueue(1)
enqueue(2)
enqueue(3)

print("Queue after enqueuing elements:", queue)

item = dequeue()
print("Dequeued item:", item)
print("Queue after dequeuing:", queue)

item = dequeue()
print("Dequeued item:", item)
print("Queue after dequeuing:", queue)

item = dequeue()
print("Dequeued item:", item)
print("Queue after dequeuing:", queue)

item = dequeue()

#exercises 7:


student_accounts = {
    "Julia": ["1234567890", "9876543210"],
    "Bobi": ["2345678901"],
    "Stefan": ["3456789012", "8765432109"],
}

for student, accounts in student_accounts.items():
    print(f"{student}'s bank account numbers:")
    for account in accounts:
        print("-", account)

#exercises 8:

def hash_list(lst):
    """Hash a list by converting it to a string and hashing the string."""
    list_str = str(lst)
    hash_value = hash(list_str)
    return hash_value

my_list = [1, 2, 3, 4, 5]
hashed_value = hash_list(my_list)
print("Hashed value:", hashed_value)

#exercises 9:

def count_word_frequency(text):
    """Count the frequency of each word in the given text."""
    words = text.split()

    word_freq = {}

    for word in words:
        word = word.strip(".,!?;:\"'()[]{}")
        word = word.lower()
        word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq

sample_text = """
#Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving".
#"""
word_frequency = count_word_frequency(sample_text)
print("Word frequency:", word_frequency)

#exercises 10:


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection)

#exercises 11:

def is_subset(set1, set2):
    """Check if set1 is a subset of set2."""
    for elem in set1:
        if elem not in set2:
            return False
    return True

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print("Is set1 a subset of set2?", is_subset(set1, set2))

set3 = {4, 5, 6}
set4 = {1, 2, 3, 4, 5}
print("Is set3 a subset of set4?", is_subset(set3, set4))

#exercises 12:

def remove_duplicates(input_list):
    """Remove duplicates from a list using a set."""
    unique_set = set(input_list)
    unique_list = list(unique_set)
    return unique_list

my_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]
print("Original list:", my_list)
unique_list = remove_duplicates(my_list)
print("List after removing duplicates:", unique_list)

#exercises 13:


squares_of_evens = [num ** 2 for num in range(2, 31, 2)]
print("List of squares of even numbers from 1 to 30:", squares_of_evens)

#exercises 14:


words = ["apple", "banana", "orange", "kiwi", "pineapple"]

word_length_dict = {word: len(word) for word in words}

print("Dictionary where keys are words and values are lengths:")
print(word_length_dict)

#exercises 15:

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_numbers = {num for num in range(2, 100) if is_prime(num)}


print("Prime numbers less than 100:")
print(prime_numbers)
