# Display welcome message
print("Welcome to The Ice Creamery!")

# Create a list for storing 7 ice cream flavors
flavorlist = ["Vanilla", "Chocolate", "Strawberry", "Pistachio", "Butter Pecan", "Cookie Dough", "Neapolitan"]

# Change the name of one flavor from the list
flavorlist[4] = "Rocky Road"

# Append a new flavor to the list to make 8
flavorlist.append("Banana")

# Sort the list into alphabetical order
flavorlist.sort()

# Loop through each flavor, displaying the name and number of the flavor
for index, flavor in enumerate(flavorlist, 1):
    print(f"{index}. {flavor}")

# Define dictionaries to hold price and description for each size cone
conePrices = {"S": "$1.50", "M": "$2.50", "L": "$3.50"}
coneSizes = {"S": "small", "M": "medium", "L": "large"}

# Prompt the user to enter the desired size cone (s, m, l)
customerSize = input("Enter the desired size cone (S, M, L): ").upper()

# Prompt the user to enter the number for the desired flavor
customerFlavor = input("Enter the number for the desired flavor: ")

try:
    customerFlavor = int(customerFlavor)
except ValueError:
    print("Invalid flavor number. Please enter a valid number.")

# Check if the customerFlavor is within a valid range
if 1 <= customerFlavor <= len(flavorlist):
    chosen_flavor = flavorlist[customerFlavor - 1]
    chosen_price = conePrices.get(customerSize, "Invalid size")
    chosen_size = coneSizes.get(customerSize, "Invalid size")
    print(f" You have choosen a {chosen_size}, {chosen_flavor} ice cream cone. Final Price: {chosen_price}")
else:
    print("Invalid flavor number. Please enter a valid number.")
