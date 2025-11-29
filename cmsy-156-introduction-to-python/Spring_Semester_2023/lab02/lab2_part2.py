def calculate_sales_tax(total_cost):
    """
    Calculate the sales tax amount.

    This function takes the total_cost of a purchase as input and calculates the sales tax amount at a fixed rate of 5%.
    It returns the computed sales tax.

    :param total_cost:
        (float): The total cost of the purchase.

    :return:
        float: The sales tax amount calculated at 5% of the total cost.
    """

    return total_cost * 0.05


def calculate_shipping_cost(phone_cost):
    """
    Calculate the shipping cost for a phone.

    This function takes the phone_cost as input and calculates the shipping cost at a fixed rate of 1.8%.
    It returns the computed shipping cost.

    :param phone_cost:
        (float): The cost of the phone.

    :return:
        float: THe shipping cost calculated at 1.8% of the phone_cost.
    """

    return phone_cost * 0.018


def calculate_total_amount(phone_cost, warranty_cost):
    """
    Calculate the total amount including phone cost, warranty cost, sales tax, and shipping cost.

    This function takes two parameters, phone_cost and warranty_cost, and calculates the total amount considering the
    combined cost of the phone and warranty. It then adds the sales tax, calculated by the 'calculate_sales_tax()'
    function, and the shipping cost, calculated by the 'calculate_shipping_cost function', to obtain the final total
    amount.

    :param phone_cost:
        (float): The cost of the phone.

    :param warranty_cost:
        (float): The cost of the warranty.

    :return:
        float: The total amount, which includes cost, warranty cost, sales tax, and shipping cost.
    """

    total_cost = phone_cost + warranty_cost
    sales_tax = calculate_sales_tax(total_cost)
    shipping_cost = calculate_shipping_cost(phone_cost)
    return total_cost + sales_tax + shipping_cost


def print_receipt(make_model, phone_cost, warranty_cost):
    """
    Print a receipt for the phone purchase.

    This function takes three parameters, make_model, phone_cost, and warranty_cost, and prints a receipt for the phone
    purchase. It calculates the sales tax using the 'calculate_sales_tax()' function, calculates the shipping cost using
    the 'calculate_shipping_cost()' function, and calculates the total amount due, including phone cost, warranty cost,
    sales tax, and shipping cost, using the 'calculate_total_amount()' function.

    :param make_model:
        (str): The make and model of the phone.

    :param phone_cost:
        (float): The cost of the phone.

    :param warranty_cost:
        (float): The cost of the warranty.

    :return:
        None
    """

    sales_tax = calculate_sales_tax(phone_cost + warranty_cost)
    shipping_cost = calculate_shipping_cost(phone_cost)
    total_amount_due = calculate_total_amount(phone_cost, warranty_cost)

    print("\n Receipt:")
    print("Model: {}".format(make_model))
    print("Cost of Phone: ${:.2f}".format(phone_cost))
    print("Warranty cost: ${:.2f}".format(warranty_cost))
    print("Sales Tax: ${:.2f}".format(sales_tax))
    print("Shipping Cost: ${:.2f}".format(shipping_cost))
    print("Total Price: ${:.2f}".format(total_amount_due))


def main():
    """
    Main function
    """

    make_model = input("Enter the phone model:")
    phone_cost = float(input("Enter the phone cost: $"))
    warranty_cost = float(input("Enter the warranty cost: $"))

    print_receipt(make_model, phone_cost, warranty_cost)


if __name__ == '__main__':
    main()
