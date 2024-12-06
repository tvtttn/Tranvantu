print('Trần Văn Tú MSV 235752021610056')
# Import the custom module
import list_operations

# Get the list size and values from the user
n = int(input("Enter the number of elements in the list: "))

# Create the list from user input
numbers = []
for i in range(n):
    num = float(input(f"Enter element {i + 1}: "))
    numbers.append(num)

# Sort the list using the module
sorted_numbers = list_operations.sort_list(numbers)

# Find the largest and smallest elements
largest = list_operations.find_max(numbers)
smallest = min(numbers)  # Using built-in `min` function

# Display the results
print("\nOriginal list:", numbers)
print("Sorted list:", sorted_numbers)
print("Largest element:", largest)
print("Smallest element:", smallest)
