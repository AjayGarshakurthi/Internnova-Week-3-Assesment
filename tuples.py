# Demonstration of Tuples
# Creating a tuple
numbers = (10, 20, 30, 40, 50)
print("Original Tuple:", numbers)

# Accessing elements using indexing
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# Tuple slicing
print("Sliced Tuple:", numbers[1:4])

# Finding the length
print("Length of Tuple:", len(numbers))

# Basic tuple operations
tuple2 = (60, 70, 80)

# Concatenation
result = numbers + tuple2
print("Concatenated Tuple:", result)

# Repetition
print("Repeated Tuple:", numbers * 2)

# Membership
print("Is 30 present?", 30 in numbers)

# Maximum and minimum
print("Maximum Value:", max(numbers))
print("Minimum Value:", min(numbers))
