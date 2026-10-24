
# Campus Cafe Menu
# Allows customers to order food, customize items, and receive a receipt.

print("==============================")
print("    CAMPUS CAFE ORDER SYSTEM")
print("==============================")
print("1. Coffee       - $3.50")
print("2. Sandwich     - $6.00")
print("3. Salad        - $5.50")
print("4. Combo        - $8.00")
print("5. Exit")
print("==============================")

# Get and validate the menu choice.
try:
    choice = int(input("Enter your choice (1-5): "))
except ValueError:
    choice = 0

if choice == 5:
    print("Thank you for visiting the Campus Cafe!")

elif choice not in [1, 2, 3, 4]:
    print("Invalid menu choice. Please choose 1-5.")

else:
    # Set the base item and price.
    if choice == 1:
        item = "Coffee"
        price = 3.50

    elif choice == 2:
        item = "Sandwich"
        price = 6.00

    elif choice == 3:
        item = "Salad"
        price = 5.50

    else:
        item = "Combo (Sandwich + Coffee)"
        price = 8.00

    # Customize coffee or the coffee included in a combo.
    if choice == 1 or choice == 4:
        size = input("Enter coffee size (small/medium/large): ")
        size = size.strip().lower()

        if size == "medium":
            price += 1.00
            coffee_size = "Medium"
        elif size == "large":
            price += 2.00
            coffee_size = "Large"
        else:
            if size != "small":
                print("Invalid size. Defaulting to Small.")
            coffee_size = "Small"

        if choice == 1:
            item = f"{coffee_size} Coffee"
        else:
            item = f"Combo with {coffee_size} Coffee"

    # Customize sandwich or sandwich included in a combo.
    if choice == 2 or choice == 4:
        cheese = input("Add cheese? (yes/no): ").strip().lower()

        if cheese == "yes":
            price += 0.75
            if choice == 2:
                item += " + Cheese"
            else:
                item += " + Cheese"
        elif cheese != "no":
            print("Invalid response. No cheese added.")

    # Customize salad dressing.
    if choice == 3:
        dressing = input(
            "Choose dressing (ranch/italian/vinaigrette/none): "
        ).strip().lower()

        if dressing not in ["ranch", "italian", "vinaigrette", "none"]:
            print("Invalid dressing. Defaulting to none.")
            dressing = "none"

        item = f"Salad ({dressing.title()} dressing)"

    # Validate the customer's name.
    name = input("Enter your name: ").strip()

    while name == "":
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()

    # Validate quantity as a positive integer.
    while True:
        try:
            quantity = int(input("How many? "))

            if quantity > 0:
                break
            else:
                print("Quantity must be a positive integer.")
        except ValueError:
            print("Please enter a valid whole number.")

    # Calculate subtotal, tax, and total.
    subtotal = price * quantity
    tax = subtotal * 0.07
    total = subtotal + tax

    # Print the order receipt.
    print("\n==============================")
    print("         ORDER RECEIPT")
    print("==============================")
    print(f"Customer:   {name}")
    print(f"Item:       {item}")
    print(f"Quantity:   {quantity}")
    print(f"Unit Price: ${price:.2f}")
    print(f"Subtotal:   ${subtotal:.2f}")
    print(f"Tax (7%):   ${tax:.2f}")
    print(f"Total:      ${total:.2f}")
    print("==============================")
    print("Thank you for your order!")
