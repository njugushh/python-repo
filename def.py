# Scope - variable exising only in ocntext that you defined it
def happy_birthday(name, age):
    print(f"Happy birthday {name}")
    print(f"You are {age} years old")
    
happy_birthday("Dan", 20)

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name("dan", "njuguna")
print(full_name)

def hello(to):
    print("hello,", to)
    
name = input("What's your name? ")
hello(name.capitalize())



def main():
    x = int(input("What is x? "))
    print(f"x squareroot is {squareroot(x)}")
    
def squareroot(n):
    return n / n
main()


    