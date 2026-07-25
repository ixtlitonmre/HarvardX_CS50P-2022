students = [
    {"name": "Alice",   "major": "Computer Science"},
    {"name": "Bob",     "major": "Mathematics"},
    {"name": "Charlie", "major": "Physics"},
    {"name": "Sam", "major": "Computer Science"},
    {"name": "Tim", "major": "Computer Science"}
]

#major =[student["major"] for student in students]
"""
majors = [] #is the same than major = list()
for student in students:
    if student["major"] not in major:
        majors.append(student["major"])
"""

# Thee previous code can be done with a set comprehension, which automatically handles duplicates:
majors = {student["major"] for student in students}

"""
# The previous code is the same as:
majors = set()
for student in students:
    majors.add(student["major"]) """

for major in sorted(majors):
    print(major)
