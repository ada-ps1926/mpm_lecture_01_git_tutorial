import sys


def add (x,y):
    print(x+y)


def multiply(x,y):
    print(x*y)


if __name__ == "__main__":
    operation = sys.argv[2] 
    x = int(sys.argv[4])
    y = int(sys.argv[6])

    if operation == "add":
        add (x,y)
    elif operation == "multiply":
        multiply(x,y)