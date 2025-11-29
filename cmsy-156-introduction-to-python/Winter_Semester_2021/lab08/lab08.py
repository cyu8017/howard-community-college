def main():
    """
    Main function
    """

    # Dictionary to define room numbers for each course.
    course_room_number = {
        'CS101': '3004',
        'CS102': '4501',
        'CS103': '6755',
        'NT110': '1244',
        'CM241': '1411',
    }

    # Dictionary to define instructors for each course.
    course_instructor = {
        'CS101': 'Haynes',
        'CS102': 'Alvardo',
        'CS103': 'Rich',
        'NT110': 'Burke',
        'CM241': 'Lee',
    }

    # Dictionary to define time for each course.
    course_time = {
        'CS101': '8:00am',
        'CS102': '9:00am',
        'CS103': '10:00am',
        'NT110': '11:00am',
        'CM241': '11:00pm',
    }

    # Prompt the user to enter the course number to search.
    print("Course: CS101 CS102 CS103 NT110, CM241\n")
    course_number_entry = input("Enter a course number to display: ")

    # Print catalog:
    # - If course_number_entry is empty. Print an error message.
    # - If course_number_entry is in the course_room_number dictionary. Print results.
    # - If course_number_entry is invalid. Print course number and error message.
    if course_number_entry == "":
        print("Your entry is empty. Please enter a course number.")
    elif course_number_entry in course_room_number:
        print("\n", course_number_entry, "\n")
        print("Room        : ", course_room_number.get(course_number_entry))
        print("Instructor  : ", course_instructor.get(course_number_entry))
        print("Time        : ", course_time.get(course_number_entry))
    else:
        print(course_number_entry, ": not found")


if __name__ == "__main__":
    main()
