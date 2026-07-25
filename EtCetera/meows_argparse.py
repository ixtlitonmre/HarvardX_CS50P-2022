import argparse

parser = argparse.ArgumentParser(description="Meow like a cat") #The description is displayed when the arg -h is used
parser.add_argument("-n", default=1, help="Number of times to meow", type=int)
#The description is displayed when the arg -h is used, the argument n defaults to 1 and it is connverted to eb an integer
args = parser.parse_args()

for _ in range(args.n):
    print("meow")