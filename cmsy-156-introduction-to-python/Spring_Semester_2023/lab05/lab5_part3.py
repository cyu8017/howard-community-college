def to_fahr(celsius_temperature):
    # ftemp = (9 / 5) * celsius_temperature + 32
    # return ftemp
    return (9/5) * celsius_temperature + 32


def to_cels(ftemp):
    celsius_temperature = (ftemp - 32) * 5 / 9
    return celsius_temperature


def display_menu():
    print("Temperature Conversions \n")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Quit")


def main():
    """
    Main function
    """

    display_menu()

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nConvert Celsius to Fahrenheit")
            while True:
                try:
                    celsius = float(input("Enter the Celsius temperature to convert: "))
                    if celsius < -273.15:
                        print("Error - temp below absolute zero. Please reenter! \n")
                    else:
                        break
                except ValueError:
                    print("Error: invalid selection. Please reenter \n")

            fahrenheit = to_fahr(celsius)
            print(f"{celsius:.2f} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit. \n")
            display_menu()

        elif choice == "2":
            print("\nConvert Fahrenheit to Celsius")
            while True:
                try:
                    fahrenheit = float(input("Enter the Fahrenheit temperature to convert: "))
                    if fahrenheit < -459.67:
                        print("Error - temp below absolute zero. Please reenter! \n")
                    else:
                        break
                except ValueError:
                    print("Invalid input! Please enter a valid temperature.")

            celsius = to_cels(fahrenheit)
            print(f"{fahrenheit:.2f} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius. \n")
            display_menu()

        elif choice == "3":
            print("Thank you for using this program")
            break

        else:
            print("Error: invalid selection. Please reenter \n")
            display_menu()


if __name__ == '__main__':
    main()
