from datetime import datetime
import os


def open_input_file(filename):
    """
    Opens an input file for reading and returns a file object.

    This function attempts to open the specified file in read mode.

    If the file is found and successfully opened, it returns a file object associated with the opened file.

    If the file is not found (FileNotFoundError), an error message is printed, indicating the issue with the file,
    and the function returns None.

    :param:
        filename (str): The name of the file to open for reading.

    :return:
        file object or None:
            A file object if the file is opened successfully, otherwise None if the file is not found.
    """

    try:
        return open(filename, 'r')
    except FileNotFoundError:
        print(f"\nERROR -- There is an issue with the file {os.path.abspath(filename)}. Please reenter:\n")
        return None


def open_output_file(filename):
    """
    Opens an output file for writing and returns a file object.

    This function attempts to open the specified file in write mode.

    If the file is found and successfully opened, it returns a file object associated with the opened file.

    If there is an issue with the file (OSError), an error message is printed, indicating the issue with the file,
    and the function returns None.

    :param:
        filename (str): The name of the file to open for writing.

    :return:
        file object or None:
            A file object if the file is opened successfully, otherwise None if there is an issue with the file.
    """

    try:
        return open(filename, 'w')
    except OSError:
        print(f"\nERROR - There is an issue with file '{os.path.abspath(filename)}'. Please reenter:\n")
        return None


def read_ip_addresses(input_file):
    """
    Reads IP addresses from the given input file and returns unique IP addresses in a set.

    This function reads IP addresses from the specified input file, where each line consists of an IP address and a
    timestamp separated by a space. It stores unique IP addresses that start with specific prefixes in a set to
    ensure their uniqueness.

    :param:
        input_file (file object): The file object representing the input file with IP addresses.

    :return:
        tuple: A tuple containing two elements:
            - record_count (int): The total number of records (lines) read from the input file.
            - ip_addresses (set): A set of containing unique IP addresses with specific prefixes.
    """

    ip_addresses = set()  # Use set to store unique IP addresses
    record_count = 0

    for line in input_file:
        record_count += 1
        ip_address, timestamp = line.strip().split(" ", 1)  # Split IP address and timestamp
        if ip_address.startswith(('168.193', '224.174', '233.012')):
            ip_addresses.add(ip_address)

    input_file.close()
    return record_count, ip_addresses


def generate_report(record_count, ip_addresses, suspect_percentage, output_file):
    """
    Generates a report containing statistics about suspect IP addresses.

    This function takes various parameters as input, including the total record count, a set of unique suspect IP
    addresses, and the percentage of suspect IP addresses among all records. The function sorts the suspect IP addresses
    in ascending order and print the following information:
        - The total number of records in the file.
        - The number of unique suspect IP addresses.
        - The percentage of suspect IP addresses among all records.

    The function also writes the same report to the specified output file. Additionally, it lists the suspect IP
    addresses along with their corresponding current date and time.

    :param record_count:
        The total number of records in the file.

    :param ip_addresses:
        A set containing unique suspect IP addresses.

    :param suspect_percentage:
        The percentage of suspect IP addresses among all records.

    :param output_file:
        open('badip.txt', 'w')
    """

    sorted_ip_addresses = sorted(ip_addresses)

    print("\n Output Report")
    print("-------------")
    print(f"The total number of records in the file is: {record_count}")
    print(f"The number of suspect IP addresses is: {len(ip_addresses)}")
    print(f"The percentage of suspect IP addresses is: {suspect_percentage:.3f}")

    output_file.write("Output Report \n")
    output_file.write("------------- \n")
    output_file.write(f"The total number of records in the file is: {record_count} \n")
    output_file.write(f"The number of suspect IP addresses is: {len(ip_addresses)} \n")
    output_file.write(f"The percentage of suspect IP addresses is: {suspect_percentage:.3f} \n")
    output_file.write("\n")
    output_file.write("Suspect IP Addresses \n")
    output_file.write("-------------------- \n")

    print("\n Suspect IP Addresses")
    print("--------------------")

    for ip_address in sorted_ip_addresses:
        current_datetime = datetime.now().strftime("%a %b   %d %H:%M:%S %Y")
        print(f"IP Address = {ip_address}   Date and Time = {current_datetime}")
        output_file.write(f"IP Address = {ip_address}   Date and Time {current_datetime}\n")

    output_file.close()


def main():
    """
    Main function to process IP addresses from an input file and generate a report.
    """

    input_filename = input("Enter the input file name: ")
    input_file = open_input_file(input_filename)

    while input_file is None:
        input_filename = input("Enter the name of the input file: ")
        input_file = open_input_file(input_filename)

    output_filename = input("Enter the output file name: ")
    output_file = open_output_file(output_filename)

    while output_file is None:
        output_filename = input("Enter the output file name: ")
        output_file = open_output_file(output_filename)

    record_count, ip_addresses = read_ip_addresses(input_file)
    suspect_percentage = (len(ip_addresses) / record_count) * 100
    generate_report(record_count, ip_addresses, suspect_percentage, output_file)

    print("\n Program complete!")


if __name__ == '__main__':
    main()
