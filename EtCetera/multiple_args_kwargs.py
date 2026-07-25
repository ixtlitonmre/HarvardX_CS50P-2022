def f(*args, **kwargs):
    #*args indicate that the function can recive 0 or more positional arguments
    #**kwargs indicates the function can also can support key word arguments, arguments that can be called by its name
    print("Positional:", args)
    print("Named:", kwargs)

m = [10,5,2]

f(m)

f(100, 50, 25)
f(100, 50, 25, 5)
f(10)
f(galleons=100, sickles=50, knuts=25)
f()