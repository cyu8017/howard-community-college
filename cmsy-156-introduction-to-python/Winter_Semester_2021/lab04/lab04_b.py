def main():
    """
    Main function
    """

    # Print message to user
    print('Temperature conversions using a for loop. \n')

    # Print conversion table
    print("{:<5} {:<5}".format('Cels', 'Fahr'))

    # List Celsius degrees from 0 to 20.
    for cels in range(0, 21):
        # Take in Celsius from loop and convert it to Fahrenheit.
        cels2Fahr = f'{((9 / 5) * cels + 32):.2f}'

        # Print solution in table.
        solution = ("{:<5} {:<5}".format(cels, cels2Fahr))

        # Print output
        print(solution)


if __name__ == "__main__":
    main()
