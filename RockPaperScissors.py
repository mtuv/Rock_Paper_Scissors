import random


def rps():
    print("This program allows you to play rock, paper, scissors.")

    while True:
        first_input = int(input("Please choose if you want to play best out of 3 or out of 5.\n"))
        if first_input == 3 or first_input == 5:
            break
        else:
            print("Please input 3 or 5")

    print("Type in your choice in lowercase.")

    play_input = str(raw_input("rock, paper, scissors!\n"))

    comp_choice = random.randint(0, 2)

    print(comp_choice)

    comp_score = 0

    play_score = 0

    while True:  # 0 is rock, 1 is paper, 2 is scissors

        if comp_score == first_input or play_score == first_input:
            break

        if (comp_choice == 0 and play_input.__eq__("rock") or comp_choice == 1 and play_input.__eq__("paper") or
                comp_choice == 2 and play_input.__eq__("scissors")):
            print("It's a tie! Both you and the computer chose " + play_input)
            comp_choice = random.randint(0, 2)
            play_input = str(raw_input("rock, paper, scissors!\n"))
            continue

        if comp_choice == 0 and play_input.__eq__("paper"):
            print("Computer: rock\nPlayer: " + play_input)
            print("The player has won the round!")
            play_score += 1
            comp_choice = random.randint(0, 2)
            play_input = str(raw_input("rock, paper, scissors!\n"))
            continue

        if comp_choice == 0 and play_input.__eq__("scissors"):
            print("Computer: rock\nPlayer: " + play_input)
            print("The computer has won the round!")
            comp_score += 1
            comp_choice = random.randint(0, 2)
            play_input = str(raw_input("rock, paper, scissors!\n"))
            continue

        if comp_choice == 1 and play_input.__eq__("rock"):
            print("Computer: paper\nPlayer: " + play_input)
            print("The computer has won the round!")
            comp_score += 1
            comp_choice = random.randint(0, 2)
            play_input = str(raw_input("rock, paper, scissors!\n"))
            continue

        if comp_choice == 1 and play_input.__eq__("scissors"):
            print("Computer: paper\nPlayer: " + play_input)
            print("The computer has won the round!")
            comp_score += 1
            comp_choice = random.randint(0, 2)
            play_input = str(raw_input("rock, paper, scissors!\n"))
            continue

        if comp_choice == 2 and play_input.__eq__("paper"):
            print("Computer: scissors\nPlayer: " + play_input)
            print("The computer has won the round!")
            comp_score += 1
            comp_choice = random.randint(0, 2)
            play_input = str(raw_input("rock, paper, scissors!\n"))
            continue

        if comp_choice == 2 and play_input.__eq__("rock"):
            print("Computer: scissors\nPlayer: " + play_input)
            print("The player has won the round!")
            play_score += 1
            comp_choice = random.randint(0, 2)
            play_input = str(raw_input("rock, paper, scissors!\n"))
            continue

    if play_score > comp_score:
        print("You win! The computer won " + str(comp_score) +
              " rounds. You won " + str(play_score) + " rounds.")

    if play_score < comp_score:
        print("The Computer wins! The computer won " + str(comp_score) +
              " rounds. You won " + str(play_score) + " rounds.")
    return


rps()


