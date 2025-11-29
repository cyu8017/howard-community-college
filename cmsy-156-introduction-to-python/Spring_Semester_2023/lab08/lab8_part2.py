def capitalize_sentence(sentence_input):
    """
    Capitalize the first letter of each word in a sentence.

    This function takes a sentence_input as input, splits the sentence into individual words, capitalizes the first
    letter of each word, and then joins the capitalized words back into a sentence.

    :param sentence_input:
        (str): The input sentence to be capitalized.

    :return:
        str: A new sentence with the first letter of each word capitalized.
    """

    words = sentence_input.split(" ")
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)


def main():
    """
    Main function
    """

    sentence_input = input("Enter sentence to be capitalized: ")
    print(capitalize_sentence(sentence_input))


if __name__ == '__main__':
    main()
