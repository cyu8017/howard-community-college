def get_scores():
    """
    This function allows the user to input a list of test scores.

    Returns:
        scores (list of floats): A list containing the entered test scores.
    :return:
    """

    num_scores = int(input("How many scores will you be entering: "))
    scores = []  # Create an empty list to store the test scores.

    # Loop to get each test score from the user and append it to the 'scores' list.
    for i in range(num_scores):
        score = float(input(f"Enter test score {i + 1} (0 - 100): "))  # Asks the user to input each test score
        scores.append(score)  # Adds the entered test score to the 'scores' list

    return scores  # Returns the list of test scores after the user has entered all of them


def display_menu():
    """
    This function displays the menu of options for the user to choose from.

    :return:
        None: The function only prints the menu options to the console.
    """

    print("\n 1. Score Metrics (min/max/avg)")
    print("2. Mine Scores (low/high scores)")
    print("3. Update Score")
    print("4. Display Scores")
    print("5. Quit")


def score_metrics(scores):
    """
    This function calculates and displays various score metrics based on the input list of test scores.

    :param scores:
        scores (list of floats): A list containing test scores.

    :return:
        None: The function only prints the calculated score metrics to the console.
    """

    num_scores = len(scores)  # Calculate the number of scores in the input list.
    highest_score = max(scores)  # Find the highest score from the input list.
    lowest_score = min(scores)  # Find the lowest score from the input list.
    average_score = sum(scores) / len(scores)  # Calculate the average score from the input.

    # Print the calculated score metrics to the console.
    print("\n\n Number of Scores:", num_scores, "\n")
    print("High Score:", highest_score)
    print("Low Score:", lowest_score)
    print("Average Score:", average_score)


def mine_scores(scores):
    """
    This function categorizes and displays scores based on their comparison to the average score.

    :param scores:
        scores (list of floats): A list containing test scores.

    :return:
        None: The function only prints the top and bottom scores to the console.
    """

    average_score = sum(scores) / len(scores)
    high_scores = [score for score in scores if score >= average_score]
    low_scores = [score for score in scores if score < average_score]
    print("\n\n Top Scores")
    for score in sorted(high_scores):
        print("{:.2f}".format(score))
    print("\n Bottom Scores")
    for score in sorted(low_scores):
        print("{:.2f}".format(score))


def update_score(scores):
    print("\n Update Score:")
    print("---------------")
    display_scores(scores)

    try:
        index = int(input("Enter the index of the score to update: "))
        new_score = float(input("Enter the new score: "))
        scores[index] = new_score
        print("Scores after update:")
        display_scores(scores)

    except (ValueError, NameError, IndexError):
        print("Invalid input or index out of range. Score update failed.")

    except Exception as e:
        print("An unexpected error occurred:", str(e))


def display_scores(scores):
    print("\n Scores in Reverse Order:")
    print("--------------------------")
    reversed_scores = scores[::1]

    for score in reversed_scores:
        print(score)


def main():
    """
    Main function
    """

    scores = get_scores()
    display_menu()

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            score_metrics(scores)
        elif choice == "2":
            mine_scores(scores)
        elif choice == "3":
            update_score(scores)
        elif choice == "4":
            display_scores(scores)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again. \n")

    display_menu()


if __name__ == "__main__":
    main()
