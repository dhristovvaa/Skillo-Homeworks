# problem 0
items = {"Coffee": 2.2, "Tea": 1.5, "Chocolate": 2.5}
income = 0

for item in items.keys():
    qty = int(input(f"How many {item}s have you sold? "))
    income += qty * items[item]

print(f"\nThe income today was £{income:.2f}")


# problem 1
def get_integer_input():
    while True:
        try:
            num = int(input("Enter an integer: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nInput interrupted. Exiting.")
            return None


number = get_integer_input()
if number is not None:
    print("You entered:", number)
else:
    print("No valid integer entered.")

#problem 2
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
