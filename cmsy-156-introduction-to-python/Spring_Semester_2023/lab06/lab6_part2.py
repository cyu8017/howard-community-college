def get_countries_by_exchange_rate():
    """
    Get a list of countries sorted by their exchange rates.

    This function reads data from the 'Exchange.txt' file, which contains information about countries and their
    exchange rates. It then creates a list of tuples, where each tuple contains the country and the country name and its
    corresponding exchange rate.

    The list is sorted on the exchange rates in ascending order.

    :return:
        list: A sorted list of typles, where each typle contains the country and its exchange rate.
    """

    countries = []
    with open('Exchrate.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            countries.append((data[0], float(data[2])))
    countries.sort(key=lambda x: x[1])
    return countries


def main():
    """
    Main function
    """

    # Get the countries sorted by exchange rate in ascending order
    sorted_countries = get_countries_by_exchange_rate()

    # Display the sorted countries
    for country, exchange_rate in sorted_countries:
        print(country)


if __name__ == '__main__':
    main()
