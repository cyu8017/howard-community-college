def read_names_from_file(filename):
    """
    Reads names from a text file and returns them as a list of strings.

    :param filename:
        (str) The name of the file to read.

    :return:
        (list) A list of names read from the file. If there's an error during the file reading,,
            an empty list will be returned.
    """

    names = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                names.append(line.strip())
    except IOError:
        print(f"Error: Could not open file {filename}")
    return names


def write_names_to_file(filename, names):
    """
    Writes a list of names to a text file.

    :param filename:
        (str) The name of the file to write to.

    :param names:
        (list) A list of names to be written to the file.

    :return: None
    """

    try:
        with open(filename, 'w') as file:
            for name in names:
                file.write(name + '\n')
    except IOError:
        print(f"Error: Could not open file {filename}")


def main():
    """
    Main function
    """

    female_names_list = read_names_from_file("FemaleNames.txt")
    male_names_list = read_names_from_file("MaleNames.txt")
    combined_names_list = female_names_list + male_names_list
    combined_names_list.sort()

    for name in combined_names_list:
        print(name)

    names_a_to_i = [
        name for name in combined_names_list
        if name and name[0].lower() in 'abcdefghi'
    ]

    names_j_to_r = [
        name for name in combined_names_list
        if name and name[0].lower() in 'jklmnopqr'
    ]

    names_s_to_z = [
        name for name in combined_names_list
        if name and name[0].lower() in 'stuvwxyz'
    ]

    write_names_to_file('babyNamesAtoI.txt', names_a_to_i)
    write_names_to_file('babyNamesJtoR.txt', names_j_to_r)
    write_names_to_file('babyNamesStoZ.txt', names_s_to_z)


if __name__ == '__main__':
    main()
