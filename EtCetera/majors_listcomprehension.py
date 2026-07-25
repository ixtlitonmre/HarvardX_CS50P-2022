def main():
    students = [
        {"name": "Bob",     "major": "Mathematics"},
        {"name": "Charlie", "major": "Physics"},
        {"name": "Sam", "major": "Computer Science"},
        {"name": "Alice",   "major": "Computer Science"},
        {"name": "Tim", "major": "Computer Science"}
    ]
    withComputerScienseStudents = [
        student["name"] for student in students if student["major"] == "Computer Science"
    ]
    for withComputerScienseStudent in sorted(withComputerScienseStudents):
        print(withComputerScienseStudent)

if __name__ == "__main__":
    main()