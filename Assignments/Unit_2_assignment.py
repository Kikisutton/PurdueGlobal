# print a string statment with a list of acceptable colors
ColorChoice = print("Your color choices are red, blue, green, white or yellow")

# enter a color value from list and assign user input
userColor = input("Enter a color from the list above: ")

# convert color entered to all lowercase
color = userColor.lower()

# create a variable name dvalidColor and set it to true
validColor = True

# set new variable spanishColor and convert color choice to spanish
if color == "red":
    spanishColor = "rojo"
elif color == "blue":
    spanishColor = "azul"
elif color == "green":
    spanishColor = "verde"
elif color == "white":
    spanishColor = "blanco"
elif color == "yellow":
    spanishColor = "amarillo"
else:
    validColor = False

if validColor:
    print(f"The color {userColor} in Spanish is {spanishColor}")
else:
    print("That is not a valid color for this program. Ese no es un color valido")