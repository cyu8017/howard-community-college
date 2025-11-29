def validate_input(item):
    """
    Validate user input for a non-negative integer value.

    :param item:
        (str): A description of the item for which the  user is providing the input.

    :return:
        (int): A non-negative integer value provided by the user.
    """
    while True:
        value = input(f"Enter the number of {item}: ")
        if value.isdigit() and int(value) >= 0:
            return int(value)
        else:
            print(f"Error - {item} cannot be negative. Please reenter. \n")


def main():
    """
    Main function
    """

    print("Welcome to the CMSY-156 Soccer Calculator\n")

    while True:
        total_games = validate_input("games")

        if total_games == 0:
            average_goals_per_game = 0.0
            average_shots_per_game = 0.0
            average_shots_per_goal = 0.0
        else:
            total_shots = validate_input("shots taken")
            total_goals = validate_input("goals made")

            if total_goals == 0:
                average_shots_per_goal = 0.0
            else:
                average_shots_per_goal = total_shots / total_goals
            average_goals_per_game = total_goals / total_games
            average_shots_per_game = total_shots / total_games

        print(f"\n\n The average goals per game is: {average_goals_per_game:.2f}")
        print(f"The average shots on goal per game is: {average_shots_per_game:.2f}")
        print(f"The average shots per goal is: {average_shots_per_goal:.2f} \n")

        user_input = input("Do you want to continue? (y/n): ")

        while user_input.lower() not in ["y", "n"]:
            print("Error: Invalid input. Please enter 'y' or 'n'.")
            user_input = input("Do you want to continue? (y/n): ")

        if user_input.lower() == "n":
            break

    print("Thank you for using this program!")


if __name__ == '__main__':
    main()
