"""
Summary of List Methods in Python
"""

# Adding elements
def add_elements():
    fruits = ["apple", "banana", "orange"]
    fruits.append("grape")
    print(f"Append: {fruits}")  # ['apple', 'banana', 'orange', 'grape']
    
    numbers = [1, 2, 3, 4, 5]
    numbers.insert(2, 10)
    print(f"Insert: {numbers}")  # [1, 2, 10, 3, 4, 5]

# Removing elements
def remove_elements():
    fruits = ["apple", "banana", "orange", "banana"]
    fruits.remove("banana")
    print(f"Remove: {fruits}")  # ['apple', 'orange', 'banana']
    
    numbers = [1, 2, 3, 4, 5]
    popped = numbers.pop(3)
    print(f"Pop: {numbers}, Popped value: {popped}")  # [1, 2, 3, 5], 4
    
    fruits = ["apple", "banana", "orange"]
    del fruits[1]
    print(f"Del: {fruits}")  # ['apple', 'orange']

# Finding elements
def find_elements():
    fruits = ["apple", "banana", "orange"]
    index = fruits.index("banana")
    print(f"Index: {index}")  # 1
    
    fruits = ["apple", "banana", "orange", "banana"]
    count = fruits.count("banana")
    print(f"Count: {count}")  # 2

# Sorting and reversing
def sort_reverse():
    numbers = [5, 2, 4, 1, 3]
    numbers.sort()
    print(f"Sort: {numbers}")  # [1, 2, 3, 4, 5]
    
    numbers = [1, 2, 3, 4, 5]
    numbers.reverse()
    print(f"Reverse: {numbers}")  # [5, 4, 3, 2, 1]

# List comprehension
def list_comprehension():
    numbers = [1, 2, 3, 4, 5]
    squared = [num ** 2 for num in numbers if num % 2 == 0]
    print(f"Squared evens: {squared}")  # [4, 16]
    
    evens = [num for num in range(1, 11) if num % 2 == 0]
    print(f"Even numbers: {evens}")  # [2, 4, 6, 8, 10]

# Built-in functions and methods
def built_in_methods():
    fruits = ["apple", "banana", "orange"]
    print(f"Length: {len(fruits)}")  # 3
    
    numbers = [1, 2, 3, 4, 5]
    print(f"Min: {min(numbers)}, Max: {max(numbers)}")  # 1, 5
    print(f"Sum: {sum(numbers)}")  # 15
    
    numbers = [5, 2, 4, 1, 3]
    print(f"Sorted: {sorted(numbers)}")  # [1, 2, 3, 4, 5]
    
    fruits.clear()
    print(f"Clear: {fruits}")  # []
    
    fruits = ["apple", "banana", "orange"]
    fruits_copy = fruits.copy()
    print(f"Copy: {fruits_copy}")  # ['apple', 'banana', 'orange']

# Running all functions if executed as a script
if __name__ == "__main__":
    add_elements()
    remove_elements()
    find_elements()
    sort_reverse()
    list_comprehension()
    built_in_methods()
