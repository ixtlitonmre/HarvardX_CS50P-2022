def main():
    yell("This", "is",  "CS50")

def yell(*words):
    uppercased = [word.upper() for word in words]
    #THe previous line is doing the same thing as a map but using the list comprehension functionality of python
    print(*uppercased)

if __name__ == "__main__":
    main()