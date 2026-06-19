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

monday = {
    "Bright",
    "Mary",
    "Amby",
    "Grace",
    "Emmanuella"
}

tuesday = {
    "Mary",
    "Grace",
    "Bright",
    "Chimaroke",
    "Blessing"
}

wednesday = {
    "Mary",
    "Grace",
    "Bright",
    "Blessing",
    "Amby"
}

all_three_days = monday & tuesday & wednesday

attended_at_least_once = monday | tuesday | wednesday

missed_at_least_one = all_students - all_three_days

onlyOnce = set()

for student in all_students:

    count = 0

    if student in monday:
        count += 1

    if student in tuesday:
        count += 1

    if student in wednesday:
        count += 1

    if count == 1:
        onlyOnce.add(student)

neverAttended = all_students - attended_at_least_once

print("ATTENDANCE REPORT")
print("-------------------------")

print("Students Who Attended All 3 Days:")
print(all_three_days)

print("\nStudents Who Missed At Least One Day:")
print(missed_at_least_one)

print("\nStudents Who Came Only Once:")
print(onlyOnce)

print("\nStudents Who Never Attended:")
print(neverAttended)