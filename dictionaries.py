# Demonstration of Dictionaries

# Creating a student dictionary
student = {
    "Name": "Rahul",
    "Age": 21,
    "Course": "B.Tech ECE",
    "City": "Hyderabad"
}

print("Student Information:", student)

# Accessing values
print("Student Name:", student["Name"])
print("Student Age:", student.get("Age"))

# Adding a new key-value pair
student["College"] = "ABC Engineering College"
print("After Adding:", student)

# Updating values
student["Age"] = 22
student["City"] = "Bangalore"
print("After Updating:", student)

# Removing data
student.pop("College")
print("After Removing:", student)

# Displaying keys
print("Dictionary Keys:", student.keys())

# Displaying values
print("Dictionary Values:", student.values())

# Displaying key-value pairs
print("Dictionary Items:", student.items())

# Using update() method
student.update({"Course": "B.Tech"})
print("After Using Update Method:", student)
