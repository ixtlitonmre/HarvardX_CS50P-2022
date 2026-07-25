def meow(n:int ) -> str:
    """Meow n times.    #Is a convention in ython to ducment your functions after the definition and
                        #With the 3 double quotes instead of the #, this way other tools can help to create the documentation for the functions in your project
    :param n Number of times to meow  #Reestructured text ... convention used by programmers to docuemnt functions
    :type n: int
    :rise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")