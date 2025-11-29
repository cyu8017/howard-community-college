def main():
    """
    Main function
    """

    try:
        with open("nameslist1.txt", "r") as namelist1, \
             open("nameslist2.txt", "r") as namelist2, \
             open('allnames.txt', 'w') as allnames:
            allnames.writelines(namelist1)
            allnames.writelines(namelist2)

    except FileNotFoundError:
        print("Error -- One or more input files not found.")

    except IOError:
        print("Error -- An error occurred while reading or writing the files.")

    except Exception as e:
        print("Error -- An unexpected error occurred:", str(e))


if __name__ == '__main__':
    main()
