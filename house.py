# Match
# _ handle any case that hasn't been.

name = input("What is your name? ")

match name:
    case "Sally" | "Gakii" | "Marion" :
        print("Kuja")
    case ("Phancy"):
        print("Ruri")
    case _:
        print("Who? ")

''' if name == "Sally" or name == "Phancy" or name == "Marion":
        print("Kuja")
    elif name == "Gakii":
        print("Ruri")
    else:
        print("Who?")
'''
    