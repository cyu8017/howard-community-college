def main():
    """
    Main function
    """

    valid_temperature = False
    start_temperature = 0

    while not valid_temperature:
        start_temperature = float(input("Enter the starting temperature: "))

        if start_temperature >= -273.15:
            valid_temperature = True
        else:
            print("Error: Temperatures cannot be below absolute zero (-273.15°C). Please re-enter! \n")

    # Part 2: Displaying table using a while loop
    print("\nTemperature conversions using a while loop\n")
    print(f"{'Cels': >10}{'Fahr': >12}{'Kelvin': >10}")
    iteration = 0

    while iteration <= 30:
        celsius_temperature_entry = start_temperature + iteration
        fahrenheit_temp = (9/5) * celsius_temperature_entry + 32
        kelvin_temp = celsius_temperature_entry + 273.15
        print(f"{celsius_temperature_entry: >10.2f}{fahrenheit_temp: >12.2f}{kelvin_temp: >10.2f}")
        iteration += 1

    # Part 3: Displaying table using a for loop
    print("\n Temperature conversions using a for loop \n")
    print(f"{'Cels': >10}{'Fahr': >12}{'Kelvin': >10}")

    for iteration in range(31):
        celsius_temperature_entry = start_temperature + iteration
        fahrenheit_temp = (9/5) * celsius_temperature_entry + 32
        kelvin_temp = celsius_temperature_entry + 273.15
        print(f"{celsius_temperature_entry: >10.2f}{fahrenheit_temp: >12.2f}{kelvin_temp: >10.2f}")

    print("\nThank you for using this program")


if __name__ == '__main__':
    main()
