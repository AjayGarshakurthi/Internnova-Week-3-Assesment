# Demonstration of Set Operations

# Creating a set
students = {"Rahul", "Priya", "Arun", "Kiran", "Priya"}
print("Original Set:", students)

# Removing duplicate values
print("Set Without Duplicates:", students)

# Adding an element
students.add("Sneha")
print("After Adding:", students)

# Removing an element
students.remove("Kiran")
print("After Removing:", students)

# Creating two sets
python_students = {"Rahul", "Priya", "Arun", "Sneha"}
java_students = {"Priya", "Arun", "Kiran", "Ravi"}

# Union
print("Students in Both Courses:", python_students.union(java_students))

# Intersection
print("Students in Both Python and Java:", python_students.intersection(java_students))

# Difference
print("Students Only in Python:", python_students.difference(java_students))

