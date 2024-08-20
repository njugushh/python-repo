# Ask user for their name
#name is a variable = Container that stores a value/values
name = input("What's your name? ")

# Remove whitespace from str
# Capitalize 
name = name.strip().capitalize().title()

# Split the strings into substrings 
first, last = name.split()

# Say Hello to user
# Print is a function = set of actions the computer executes for you
# Corner case = \ \ escape character
print("Hello", first, ",\"Welcome back.\"")

# Parameters - print(*object, sep=" ", end="\n")
# Positonal parameters = the first argument is printed first and so forth
# Named parameter = optional and are passed at the end of statement 
location = input("Where are you from? ")
print("I'm from ", location, end="")
print(" ,the capital of Kenya.")

# Format string = f
age = int(input("What is your age? "))
print(f"I'm {age} years old.")
