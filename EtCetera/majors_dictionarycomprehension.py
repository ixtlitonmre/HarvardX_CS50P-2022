def main():
    students = ["Sam", "Alice", "Tim"]

    ComputerScienseStudents = {student: "Computer Science" for student in students}
    #Dictionary comprehension works like the list comprehension, but instead of square brackets
    #we use curly braquets and the result is a dictionary.
    #This example adds the major 'Computer Science to all the students in the list

    print(ComputerScienseStudents)

if __name__ == "__main__":
    main()