def main():
    """
    Main function
    """

    total_games = 0
    total_goals = 0
    print("Welcome to the CMSY-156 Soccer Calculator \n")

    while True:
        # Input validation for total games
        valid_total_games = False
        while not valid_total_games:
            total_games = input("Please enter the number of games: ")
            if total_games.isdigit() and int(total_games) >= 0:
                valid_total_games = True
            else:
                print("Error: the number of shots taken cannot be negative i.e <0, please reenter.")

        total_games = int(total_games)
        total_shots = 0  # Initialize total_shots outside the if-else block.

        if total_games == 0:
            average_goals_per_game = 0.0
            average_shots_per_game = 0.0
            average_shots_per_goal = 0.0
        else:
            # Input validation for total shots
            valid_total_shots = False
            while not valid_total_shots:
                total_shots = input("Please enter the number of shots taken: ")
                if total_shots.isdigit() and int(total_shots) >= 0:
                    valid_total_shots = True
                else:
                    print("Error: the number of shots taken cannot be negative i.e. <0 please reenter.")

            total_shots = int(total_shots)

            # Input validation for total goals
            valid_total_goals = False
            while not valid_total_goals:
                total_goals = input("Please enter the number of goals scored: ")
                if total_goals.isdigit() and int(total_goals) >= 0:
                    valid_total_goals = True
                else:
                    print("Error: the number of goals scored cannot be negative i.e < 0, please reenter.")

            total_goals = int(total_goals)

            if total_goals == 0:
                average_shots_per_goal = 0.0
            else:
                average_shots_per_goal = total_shots / total_goals

            average_goals_per_game = total_goals / total_games
            average_shots_per_game = total_shots / total_games

        print(f"\n The average goals per game is: {average_goals_per_game:.2f}")
        print(f"The average shots on goal per game is: {average_shots_per_game:.2f}")
        print(f"The average shots per goal is: {average_shots_per_goal:.2f} \n")

        # Ask for repeat entry
        user_input = input("Do you want to continue? (y/n): ")

        while user_input.lower() not in ["y", "n"]:
            print("Error: Invalid input. Please enter 'y' or 'n'.")
            user_input = input("Do you want to continue? (y/n): ")

        if user_input.lower() == "n":
            break

    print("Thank you for using this program!")


if __name__ == '__main__':
    main()
