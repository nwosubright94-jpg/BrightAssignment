# List of all students registered in the class
all_students = {
    "Chimaroke",
    "Mary",
    "Amby",
    "Sarah",
    "Grace",
    "Emmanuella",
    "Blessing",
    "Esther",
    "Ruth",
    "Bright"
}

# Students who attended on Monday
monday = {
    "Bright",
    "Mary",
    "Amby",
    "Grace",
    "Emmanuella"
}

# Students who attended on Tuesday
tuesday = {
    "Mary",
    "Grace",
    "Bright",
    "Chimaroke",
    "Blessing"
}

# Students who attended on Wednesday
wednesday = {
    "Mary",
    "Grace",
    "Bright",
    "Blessing",
    "Amby"
}

# Find students who attended on all three days
# The intersection operator (&) returns common students
all_three_days = monday & tuesday & wednesday

# Find students who attended at least one day
# The union operator (|) combines all attendees without duplicates
attended_at_least_once = monday | tuesday | wednesday

# Find students who missed at least one day
# Anyone not in the "all three days" group missed at least one class
missed_at_least_one = all_students - all_three_days

# Create an empty set to store students who attended only once
onlyOnce = set()

# Check each student one by one
for student in all_students:

    # Start attendance count at zero
    count = 0

    # Add 1 if the student attended Monday
    if student in monday:
        count += 1

    # Add 1 if the student attended Tuesday
    if student in tuesday:
        count += 1

    # Add 1 if the student attended Wednesday
    if student in wednesday:
        count += 1

    # If attendance count is exactly 1,
    # the student attended only once
    if count == 1:
        onlyOnce.add(student)

# Find students who never attended any class
# These students are not present in the combined attendance list
neverAttended = all_students - attended_at_least_once

# Display the attendance report heading
print("ATTENDANCE REPORT")
print("-------------------------")

# Display students who attended all three days
print("Students Who Attended All 3 Days:")
print(all_three_days)

# Display students who missed at least one day
print("\nStudents Who Missed At Least One Day:")
print(missed_at_least_one)

# Display students who attended only once
print("\nStudents Who Came Only Once:")
print(onlyOnce)

# Display students who never attended any class
print("\nStudents Who Never Attended:")
print(neverAttended)
