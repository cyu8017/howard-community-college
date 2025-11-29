delivery_address = ""


def display_menu():
    """
    Displays the menu options for the pizza shop and asks the user to enter their choice.

    :return:
        (int): The user's choice as an integer representing the selected menu option.
    """
    print("What would you like to order today? \n")
    print("1. Cheese Pizza")
    print("2. Garden Fresh Pizza")
    print("3. Meat Lovers Pizza")
    print("4. Checkout")
    while True:
        try:
            customer_choice = int(input("Enter your order here: "))
            return customer_choice
        except ValueError:
            display_error_message()


def display_error_message():
    """
    Displays an error message for invalid user input.
    :return:
    """
    print("Error: Please enter a valid value. Please try again! \n")


def get_tip_amount():
    """
    Asks the user to enter the tip amount and validates if it's a non-negative float.

    :return:
        (float): The tip amount entered by the user.
    """
    while True:
        try:
            tip = float(input("Please enter the amount of the tip: $"))
            if tip >= 0:
                return tip
            else:
                display_error_message()
        except ValueError:
            display_error_message()


def main():
    """
    Main function
    """

    global delivery_address
    print("Welcome to the CMSY-156 Pizza Shop\n")
    while True:
        try:
            order_type = int(input("Enter 1 for delivery or 2 for pickup: "))
            if order_type == 1 or order_type == 2:
                break
            else:
                display_error_message()
        except ValueError:
            display_error_message()

    if order_type == 1:
        delivery_cost = 5
        delivery_address = input("Enter the delivery address: ")
    else:
        delivery_cost = 0

    total_cost = 0
    while True:
        choice = display_menu()
        if choice == 1:
            total_cost += 17.10 * 1.06
            print("\nYou ordered a Cheese pizza")
        elif choice == 2:
            total_cost += 18.49 * 1.06
            print("\nYou ordered a Garden Fresh pizza")
        elif choice == 3:
            print("\nYou ordered a Meat Lovers pizza")
            total_cost += 19.75 * 1.06
        elif choice == 4:
            break
        else:
            display_error_message()

    tip_amount = get_tip_amount()
    total_cost = total_cost + tip_amount + delivery_cost

    if order_type == 1:
        print("The total cost with tax, tip, and delivery charge is: $", round(total_cost, 2))
        print("The pizza will be delivered to:", delivery_address)

    if order_type == 2:
        print("The total cost with tax and tip is $", round(total_cost, 2))

    print("\nThank you for using the CMSY-156 Pizza Shop. Please come again")


if __name__ == '__main__':
    main()
