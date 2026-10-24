
# Student Profile Input Validator
# Checks every field and reports all errors together.

student_id = input("Enter student ID: ").strip()
name = input("Enter full name: ").strip()
age_input = input("Enter age: ").strip()
major_input = input("Enter major: ").strip()

errors = []

# Validate student ID.
if len(student_id) != 8:
    errors.append(
        f"Student ID must be exactly 8 characters (got {len(student_id)})"
    )

if len(student_id) == 0 or not student_id[0].isalpha():
    errors.append("Student ID must start with a letter")

# The first character is a letter; all remaining characters must be digits.
if not student_id[1:].isdigit():
    errors.append("Student ID must have 7 digits after the first letter")

# Validate full name.
if len(name) == 0:
    errors.append("Name cannot be empty")
elif len(name) < 2:
    errors.append("Name must be at least 2 characters")

# Validate age using try/except.
try:
    age = int(age_input)

    if age < 16 or age > 99:
        errors.append("Age must be between 16 and 99")
except ValueError:
    age = None
    errors.append("Age must be a valid integer")

# Validate major without considering capitalization.
valid_majors = ["CS", "IT", "CE", "DS"]
major = major_input.upper()

if major not in valid_majors:
    errors.append(
        f"Major must be one of: CS, IT, CE, DS (got {major_input})"
    )

# Display all errors or the completed profile.
if len(errors) == 0:
    print("\nProfile created successfully!")
    print(f"  Student ID: {student_id}")
    print(f"  Name:       {name}")
    print(f"  Age:        {age}")
    print(f"  Major:      {major}")
else:
    print("\nProfile has errors:")
    for error in errors:
        print(f"  - {error}")
