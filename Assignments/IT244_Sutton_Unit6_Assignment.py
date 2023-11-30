# Conversion formulas for your reference:
# F = (C * 9/5) + 32
# C = (F - 32) * 5/9

# Define a temperature conversion function that accepts two parameters
def convertTemp(temps, tempScale):
    if tempScale.upper() == "C":
        temps[0] = (temps[1] - 32) * 5/9
    elif tempScale.upper() == "F":
        temps[1] = (temps[0] * 9/5) + 32
    else:
        print("Invalid temperature scale. Please enter 'C' or 'F'.")
        return None

    return temps

# Prompt the user to enter a temperature value and scale
tempEntered = float(input("Enter a temperature value: "))
tempScale = input("Enter a single letter to indicate the temperature scale (C or F): ")

# Define and initialize the temps list to hold two number values
temps = [0, 0]

# Use an IF/ELIF statement to evaluate the temperature scale entered
if tempScale.upper() == "C":
    temps[0] = tempEntered
elif tempScale.upper() == "F":
    temps[1] = tempEntered
else:
    print("Invalid temperature scale. Please enter 'C' or 'F'.")

# Call the temperature conversion function passing the temperature values in a list and a letter code for temperature scale
converted_temps = convertTemp(temps, tempScale)

# Display the results from the temperature conversion function
print(f"\nTemperature entered: {tempEntered} {tempScale.upper()}")
print(f"Converted temperature: {converted_temps[0]:.2f} C, {converted_temps[1]:.2f} F")
