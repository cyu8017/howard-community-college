def main():
    """
    Main function
    """

    # Display the title of the program
    print("Welcome to the CMSY-169 Pizza Shop!")

    # Initialize variables
    pizzas = []
    delivery_address = None
    total_cost = 0.0

    # Ask if it's pickup or delivery
    while True:
        pizza_option = input("Enter 1 for delivery or 2 for pickup: ")

        if pizza_option == '2':
            break
        elif pizza_option == '1':
            delivery_address = input("Enter the delivery address: ")
            break
        else:
            print("Error: Please enter either 1 or 2. Please try again!")
            print()

    # Display menu

    # Take pizza orders
    while True:
        print("What would you like to order today? \n")
        print("1. Cheese Pizza")
        print("2. Garden Fresh Pizza")
        print("3. Meat Lovers Pizza")
        print("4. Checkout")
        choice = int(input("Enter your order here: "))

        if choice == 1:
            pizzas.append(('Cheese', 17.10))
            print("\n You ordered a Cheese pizza")
        elif choice == 2:
            pizzas.append(('Garden Fresh', 18.49))
            print("\n You ordered a Garden Fresh pizza.")
        elif choice == 3:
            pizzas.append(('Meat Lovers', 19.75))
            print("\n You ordered a Meat Lovers pizza.")
        elif choice == 4:
            break
        else:
            print("Error: Please enter a valid menu option. Please try again!")

    # Calculate total cost with tax.
    for pizza in pizzas:
        total_cost += pizza[1] + (pizza[1] * 0.06)  # Add pizza cost with 6% sales tax

    tip = float(input("Please enter the amount of the tip: $"))
    total_cost += tip

    if delivery_address:
        total_cost += 5.0  # Delivery charge of $5

    # Display total cost
    print("The total cost with tax, tip and delivery charge is: $", round(total_cost, 2))

    if delivery_address:
        print("The pizza will be delivered to:", delivery_address)

    # Display thank you message
    print("Thank you for using the CMSY-156 Pizza Shop. Please come again")


if __name__ == '__main__':
    main()
