def compute_average(total, count):
    """
    Computes the average given the total and count of items.

    This function calculates the average value by dividing the total by the count of items.
    If the count is zero, the function returns 0 to avoid division by zero and prevent errors.

    :param total:
        (float or int): The sum or total of the items.

    :param count:
        (int): The number of items used to calculate the average.

    :return:
        (float): The computed average value if count is not zero, otherwise returns 0.
    """

    return total / count if count != 0 else 0


def display_game_results(goals_per_game, shots_per_game, shots_per_goal):
    """
    Display the results of the soccer game statistics.

    This function takes three parameters: goals_per_game, shots_per_game, and shots_per_goal, which represent the
    computed averages for goals scored per game, shots taken per game, and shots taken per goal respectively. It prints
    out these statistics in a formatted manner.

    :param goals_per_game:
        (float): The average number of goals scored per game.

    :param shots_per_game:
        (float): The average number of shots taken per game.

    :param shots_per_goal:
        (float): The average number of shots taken per goal.
    """

    print("The goals per game is: {:.2f}".format(goals_per_game))
    print("The shots per game is: {:.2f}".format(shots_per_game))
    print("The shot per goal is: {:.2f}".format(shots_per_goal))


def main():
    """
    Main function
    """

    print("CMSY-156 Soccer Calculator \n")

    total_games_played = int(input("Enter games: "))
    total_shots_made = int(input("Enter shots: "))
    total_goals_scored = int(input("Enter goals: "))

    if total_games_played == 0:
        average_goals_per_game_scored = 0.0
        average_shots_per_game_made = 0.0
        average_shots_per_goal_made = 0.0
    else:
        average_goals_per_game_scored = compute_average(total_goals_scored, total_games_played)
        average_shots_per_game_made = compute_average(total_shots_made, total_games_played)

        if total_games_played == 0:
            average_shots_per_goal_made = 0.0
        else:
            average_shots_per_goal_made = compute_average(total_shots_made, total_goals_scored)

    display_game_results(average_goals_per_game_scored, average_shots_per_game_made, average_shots_per_goal_made)

    print("Thank you for using this program.")


if __name__ == '__main__':
    main()
