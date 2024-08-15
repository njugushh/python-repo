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
