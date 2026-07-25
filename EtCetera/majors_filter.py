def main():
    students = [
        {"name": "Bob",     "major": "Mathematics"},
        {"name": "Charlie", "major": "Physics"},
        {"name": "Sam", "major": "Computer Science"},
        {"name": "Alice",   "major": "Computer Science"},
        {"name": "Tim", "major": "Computer Science"}
    ]
    ComputerScienseStudents = filter(is_ComputerScienseStudent, students)
    #The filter function requires that the function used in the first parameter returs true or false
    #and will use it on all the elements of the dictionary, could also be a list in the second parameter.

    #ComputerScienseStudents = filter(lambda student: student["major"]== "Computer Science", students)
    #If we know we are only going o use the function is_ComputerScienseStudent once in the code
    #we can define a lambda function as ilustrated in the previous line of code and we will get the same
    #results

    for ComputerScienseStudent in sorted(ComputerScienseStudents, key=lambda student: student["name"]):
        print(ComputerScienseStudent["name"])

def is_ComputerScienseStudent(student):
    return student["major"] == "Computer Science"

if __name__ == "__main__":
    main()