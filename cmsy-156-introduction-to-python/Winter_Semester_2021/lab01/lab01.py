def main():
    """
    Main function
    """

    # Prompt the user for a Celsius temperature entry.
    # Take the entry as a float.
    celsiusEntry = float(input("Enter the Celsius temperature: "))

    # Conversion to Fahrenheit equation.
    c2F = (9 / 5) * celsiusEntry + 32

    # Print result.
    print(f'{celsiusEntry:.2f}', "degrees Celsius converted to Fahrenheit is:", f'{c2F:.2f}')


if __name__ == '__main__':
    main()
