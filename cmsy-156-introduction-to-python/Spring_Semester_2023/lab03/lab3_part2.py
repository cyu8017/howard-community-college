def main():
    """
    Main function
    """

    print("Welcome to the CMSY-156 Soccer Calculator")

    while True:
        total_games = int(input("\nEnter the total number of games: "))

        if total_games == 0:
            average_goals_per_game = 0.0
            average_shots_per_game = 0.0
            average_shots_per_goal = 0.0
        else:
            total_shots = int(input("Enter the total number of shots taken: "))
            total_goals = int(input("Enter the total number of goals scored: "))

            if total_goals == 0:
                average_shots_per_goal = 0.0
            else:
                average_shots_per_goal = total_shots / total_goals

            average_goals_per_game = total_goals / total_games
            average_shots_per_game = total_shots / total_games

        print(f"\nThe average goals per game is: {average_goals_per_game:.2f}")
        print(f"The average shots on goal per game is: {average_shots_per_game:.2f}")
        print(f"The average shots per goal is: {average_shots_per_goal:.2f} \n")

        user_input = input("Do you want to continue? (yes/no): ")

        if user_input.lower() == "no":
            break

    print("Thank you for using this program!")


if __name__ == '__main__':
    main()
