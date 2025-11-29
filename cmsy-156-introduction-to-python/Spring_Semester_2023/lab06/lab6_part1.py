def get_currency_exchange(country):
    """
    Retrieves the currency exchange rate for a specific country from a file.

    :param country:
        (str): The name of the country for which the exchange rate is needed.

    :return:
        (tuple): A tuple containing the currency code (str) and the exchange rate (float) for the given country.
            If the country is not found in the file, it returns (None, None).
    """

    with open('Exchrate.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if data[0] == country:
                return data[1], float(data[2])
    return None, None


def main():
    """
    Main function
    """

    country_name = input("Enter the name of a country: ")
    currency, exchange_rate = get_currency_exchange(country_name)

    if currency and exchange_rate:
        print("Lab6-1 Answer")
        print(f"Currency: {currency}")
        print(f"Exchange rate: {exchange_rate}")
    else:
        print(f"{country_name} is not in the file.")


if __name__ == '__main__':
    main()
