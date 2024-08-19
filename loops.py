# while loop - a block of code that can do stuff again and again
# We count from 0

'''i = 3
while i != 0:
    print("Meow")
    i = i -1
'''
     

i = 0
while i < 3:
    print("Meow")
    i += 1


# For loop - iterate over a list of items
# Lists - new data types represented in square brackets
#_ it is used because it isnt necessarily going to be used in the future
for _ in range(3):
    print("Hi")
    
# Shorter version i guess
print("Wow\n" * 3,end="")

while True:
    n = int(input("What is n? "))
    if n < 0 :
        continue # continues with loop is correct answer is not given
    else: 
        break
    
    