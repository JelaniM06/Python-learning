hours = float(input("Enter hours parked: "))
vehicle = input("Enter vehicle type (car or truck): ").lower()
member = input("Are you a member? (yes or no): ").lower()

if hours <= 0:
    print("Invalid hours.")

elif vehicle == "car":
    if hours <= 2:
        fee = 4.00
    elif hours <= 8:
        fee = 4.00 + 1.50 * (hours - 2)
    else:
        fee = 13.00 + 1.00 * (hours - 8)

    if member == "yes":
        fee = fee * 0.80

    print("\n--- Parking Receipt ---")
    print(f"Hours: {hours:.2f}")
    print("Vehicle: Car")
    print(f"Member: {'Yes' if member == 'yes' else 'No'}")
    print(f"Parking fee: ${fee:.2f}")
    print("-----------------------")

elif vehicle == "truck":
    if hours <= 2:
        fee = 8.00
    elif hours <= 8:
        fee = 8.00 + 2.50 * (hours - 2)
    else:
        fee = 23.00 + 2.00 * (hours - 8)

    if member == "yes":
        fee = fee * 0.80

    print("\n--- Parking Receipt ---")
    print(f"Hours: {hours:.2f}")
    print("Vehicle: Truck")
    print(f"Member: {'Yes' if member == 'yes' else 'No'}")
    print(f"Parking fee: ${fee:.2f}")
    print("-----------------------")

else:
    print("Invalid vehicle type.")