class Cat: #Usually all class names start with upper case while variables should be all in lowwercase
    MEOWS = 3 #Python if a varaible is all in uppercase is a Constant, but just by convention,
              #There is nothing preventig the code to change the value so is handled by an "honor" system
    
    def meow(self):
        for _ in range(Cat.MEOWS): #We use the _ becasue we are not going to be using the variable anywhere else
            print("meow")

cat = Cat()
cat.meow()