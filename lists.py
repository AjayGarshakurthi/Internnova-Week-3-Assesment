# Demonstration of List Operations

# Creating a list
marks = [85, 90, 75, 60, 95]
print("Original List:", marks)

# Accessing elements
print("First Mark:", marks[0])
print("Last Mark:", marks[-1])

# Adding elements
marks.append(88)
print("After Adding:", marks)

# Updating elements
marks[2] = 80
print("After Updating:", marks)

# Removing elements
marks.remove(60)
print("After Removing:", marks)

# Sorting the list
marks.sort()
print("Ascending Order:", marks)

# Sorting in descending order
marks.sort(reverse=True)
print("Descending Order:", marks)
