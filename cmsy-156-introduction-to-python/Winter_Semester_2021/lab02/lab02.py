def main():
    """
    Main function
    """

    # Prompt the user for Fahrenheit temperature entry.
    # Take in the entry as a float.
    fahrenheitEntry = float(input("Enter the Fahrenheit temperature: "))

    # Conversion to Celsius equation.
    f2C = (fahrenheitEntry - 32) * 5 / 9

    # Print result.
    print(f'{fahrenheitEntry:.2f}', "degrees Fahrenheit converts to approximately", f'{f2C:.2f}', "degrees Celsius.")


if __name__ == "__main__":
    main()
