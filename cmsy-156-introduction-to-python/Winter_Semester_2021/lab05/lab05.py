import sys


def to_fahr(ctemp):
    """
    Convert a temperature from Celsius to Fahrenheit.

    :param ctemp:
        (float): The temperature in Celsius.

    :return:
        (float): The equivalent temperature in Fahrenheit.
    """

    return (9 / 5) * ctemp + 32


def to_cels(ftemp):
    """
    Convert a temperature from Fahrenheit to Celsius.

    :param ftemp:
        (float): The temperature in Fahrenheit.

    :return:
        (float): The equivalent temperature in Celsius.
    """

    return (ftemp - 32) * 5 / 9


def display_menu():
    """
    Display a menu of temperature conversion options for the user to choose from.

    :return:
        None: The function only prints the menu options to the console.
    """

    print("Temperature Conversions \n")
    print("1) Celsius to Fahrenheit")
    print("2) Fahrenheit to Celsius")
    print("3) Quit")


def main():
    """
    Main function
    """

    # Print menu, then prompt user for an input.
    display_menu()
    choice = input('Enter your choice:  \n')

    # This while loop will always re-run the application until the user quits.
    while choice != 3:

        # User choice 1
        # Prompt the user to enter a Celsius temperature.
        # Print Fahrenheit temperature.
        if choice == '1':
            print('Convert Celsius to Fahrenheit')
            ctemp = float(input('Enter the Celsius temperature to convert: '))
            print(f'{ctemp :.2f}', 'degrees Celsius is', f'{(to_fahr(ctemp)):.2f}', 'degrees Fahrenheit.')

        # User choice 2
        # Prompt the user to enter a Fahrenheit temperature.
        # Print Celsius temperature.
        elif choice == '2':
            print('Convert Fahrenheit to Celsius')
            ftemp = float(input('Enter the Fahrenheit temperature to convert: '))
            print(f'{ftemp :.2f}', 'degrees Fahrenheit is', f'{(to_cels(ftemp)):.2f}', 'degrees Celsius.')

        # User choice 3
        # Exit this program.
        elif choice == '3':
            print('Exiting the program...')
            sys.exit()

        # If the user does not select choice 3, keep printing the menu.
        # Then prompt the user for an input.
        print('\n')  # Print blank line
        display_menu()
        choice = input('Enter your choice: ')


if __name__ == "__main__":
    main()
