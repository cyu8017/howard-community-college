def main():
    """
    Main function
    """

    # Print message to user
    print('Temperature conversions using a for loop. \n')

    # Print conversion table
    print("{:<5} {:<5}".format('Cels', 'Fahr'))

    # Define counter starting point.
    cels = 1

    # While loop range is 21 counts to 20 in numerical list.
    while cels <= 21:
        # Take in Celsius from loop and convert it to Fahrenheit.
        cels2Fahr = f'{((9 / 5) * cels + 32):.2f}'

        # Print solution in table.
        solution = ("{:<5} {:<5}".format(cels, cels2Fahr))

        # Increment by 1 from the starting point of 1
        cels += 1

        # Print output
        print(solution)


if __name__ == "__main__":
    main()
