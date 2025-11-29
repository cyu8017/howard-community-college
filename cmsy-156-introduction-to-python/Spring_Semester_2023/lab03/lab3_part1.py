def main():
    """
    Main function
    """

    # Define cost for pizza, tax, and delivery charge.
    pizza_prices = {
        1: 17.10,  # Cheese Pizza
        2: 18.49,  # Garden Fresh Pizza
        3: 19.75   # Meat Lovers Pizza
    }

    sales_tax_rate = 0.06
    delivery_charge = 5.00

    # Create a dictionary to map pizza choice numbers to names.
    pizza_names = {
        1: "Cheese Pizza",
        2: "Garden Fresh Pizza",
        3: "Meat Lovers Pizza"
    }

    # Show the user a menu of pizza options.
    print("Welcome to the CMSY-156 Pizza Shop")
    print("What would you like to order today?\n")

    # Allow the user to enter their pizza choice.
    while True:
        try:
            pizza_choice = int(input(
                "Enter 1 for a Cheese pizza, "
                "2 for a Garden Fresh pizza, "
                "or 3 for a Meat Lovers pizza: "
            ))
            if pizza_choice in pizza_names:
                break
            else:
                print("Invalid pizza choice. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a valid pizza choice.\n")

    # Allow the user to select order type (delivery or pickup).
    while True:
        try:
            order_type = int(input("Enter 1 for delivery, or 2 for pickup: "))
            if order_type == 1 or order_type == 2:
                break
            else:
                print("Invalid order type. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a valid order type.\n")

    # Handle the delivery-specific information.
    if order_type == 1:
        delivery_address = input("Please enter the delivery address: ")
        delivery_charge_message = f"The total cost with tax, tip, and delivery charge is: "
    else:
        delivery_address = ""
        delivery_charge = 0.00
        delivery_charge_message = ""

    # Allow the user to enter the tip amount.
    while True:
        try:
            tip_amount = float(input("Please enter the amount of the tip: $"))
            if tip_amount >= 0:
                break
            else:
                print("Invalid tip amount. Please enter a positive value.\n")
        except ValueError:
            print("Invalid input. Please enter a valid tip amount.\n")

    # Calculate the cost of the selected pizza and the total cost due.
    pizza_name = pizza_names[pizza_choice]
    pizza_cost = pizza_prices[pizza_choice]
    sales_tax_amount = pizza_cost * sales_tax_rate
    total_cost_due = pizza_cost + sales_tax_amount + delivery_charge + tip_amount

    print("\nYou ordered the", pizza_name)

    # Display the total cost with appropriate messages.
    if order_type == 2:
        print(f"The total cost with tax and tip is: ${total_cost_due:.2f}")
    elif order_type == 1:
        print(f"{delivery_charge_message}${total_cost_due:.2f}")
        print("The pizza will be delivered to:", delivery_address)

    print("\nThank you for using the CMSY-156 Pizza Shop. Please come again!")


if __name__ == '__main__':
    main()
