def convert_to_numeric(number):
    """
    Converts an input string to its numeric representation based on a phone keypad.

    :param number:
        (str): The input string to be converted.

    :return:
        (str): The numeric representation of the input string.
    """

    # Initialize an empty string to store the numeric representation.
    numeric_number = ''

    # Iterate through each character in the input string.
    for char in number:
        # Check if the character is an alphabetic letter.
        if char.isalpha():
            # Convert the character to uppercase to handle both upper and lowercase letters.
            char = char.upper()

            # Map the character to its corresponding numeric representation.
            if 'A' <= char <= 'C':
                numeric_number += '2'
            elif 'D' <= char <= 'F':
                numeric_number += '3'
            elif 'G' <= char <= 'I':
                numeric_number += '4'
            elif 'J' <= char <= 'L':
                numeric_number += '5'
            elif 'M' <= char <= 'O':
                numeric_number += '6'
            elif 'P' <= char <= 'S':
                numeric_number += '7'
            elif 'T' <= char <= 'V':
                numeric_number += '8'
            elif 'W' <= char <= 'Z':
                numeric_number += '9'
        else:
            # If the character is not an alphabetic letter, keep it as is.
            numeric_number += char

    # Return the final numeric representation of the input string.
    return numeric_number


def main():
    """
    Main function
    """

    telephone_number_entry = input("Enter a phone number to be translated: ")
    numeric_telephone_number = convert_to_numeric(telephone_number_entry)
    print(numeric_telephone_number)


if __name__ == "__main__":
    main()
    