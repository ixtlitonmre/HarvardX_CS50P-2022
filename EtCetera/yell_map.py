def main():
    yell("This", "is",  "CS50")

def yell(*words):
    uppercased = map(str.upper, words) 
    #Here the str.upper (is a function) is passed as a parameter that is why the parenthesis are not included
    print(*uppercased)

if __name__ == "__main__":
    main()