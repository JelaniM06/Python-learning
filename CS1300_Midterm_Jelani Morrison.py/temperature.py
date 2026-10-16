# Temperature Conveter

temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (F or C): ").upper()

if unit == "F":
    converted = (temperature - 32) * 5 / 9
    print(f"{temperature:.2f}°F is {converted:.2f}°C")

elif unit == "C":
    converted = (temperature * 9 / 5) + 32
    print(f"{temperature:.2f}°C is {converted:.2f}°F")

else:
    print("Invalid unit. Please enter F or C.")
    