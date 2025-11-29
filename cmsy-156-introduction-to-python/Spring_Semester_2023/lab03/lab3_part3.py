def main():
    """
    Main function
    """

    regular_price_per_scoop = 2.75
    discounted_price_per_scoop = 2.10
    waffle_cone_price = 1.55

    print("How many scoops would you like?")
    num_of_ice_cream_scoops = int(input("Enter the number of scoops (minimum 1): "))

    if num_of_ice_cream_scoops <= 0:
        print(f"You asked for {num_of_ice_cream_scoops} scoops. You must order one or more scoops.")
        exit()

    waffle_cone = input("Would you like a waffle cone? (y/n): ").lower()

    if num_of_ice_cream_scoops <= 2 and waffle_cone == 'n':
        total_cost = num_of_ice_cream_scoops * regular_price_per_scoop
    elif num_of_ice_cream_scoops <= 2 and waffle_cone == 'y':
        print(f"The price of a waffle cone is ${waffle_cone_price:.2f}")
        total_cost = num_of_ice_cream_scoops * regular_price_per_scoop + waffle_cone_price
    elif num_of_ice_cream_scoops >= 2 and waffle_cone == 'n':
        total_cost = num_of_ice_cream_scoops * discounted_price_per_scoop
    elif num_of_ice_cream_scoops >= 2 and waffle_cone == 'y':
        print(f"The price of a waffle cone is ${waffle_cone_price:.2f}")
        total_cost = num_of_ice_cream_scoops * discounted_price_per_scoop + waffle_cone_price
    else:
        total_cost = num_of_ice_cream_scoops * discounted_price_per_scoop

    if num_of_ice_cream_scoops == 1:
        print(f"\n The price per scoop is: ${regular_price_per_scoop:.2f}")
        print(f"You ordered {num_of_ice_cream_scoops} scoop")
        print(f"Your total cost is: ${total_cost:.2f}")
        print("Thank you for using the program")

    elif num_of_ice_cream_scoops == 2:
        print(f"\n The price per scoop is: ${regular_price_per_scoop:.2f}")
        print(f"You ordered {num_of_ice_cream_scoops} scoops")
        print(f"Your total cost is: ${total_cost:.2f}")
        print("Thank you for using the program")

    elif num_of_ice_cream_scoops >= 3:
        print(f"\n The price per scoop is: ${discounted_price_per_scoop:.2f}")
        print(f"You ordered {num_of_ice_cream_scoops} scoops")
        print(f"Your total cost is: ${total_cost:.2f}")
        print("Thank you for using the program")


if __name__ == '__main__':
    main()
