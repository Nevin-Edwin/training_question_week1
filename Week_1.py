import random

history = {"choices": ["Rock", 'Paper', 'Scissors']}
play_round = 1
(player_point, computer_point) = (0, 0)

while play_round < 10:
    computer = random.choices(history["choices"])[0]
    player = input('your turn choose any one of this {}:'.format(history["choices"])).title()
    result = str()

    if computer == player:
        result = "Tie on Round {}.".format(play_round)
    else:
        if (computer == "Rock" and player == "Paper") or (computer == "Paper" and player == "Scissors") or (
                computer == "Scissors" and player == "Rock"):
            player_point += 1
            result = "player won Round {}".format(play_round)
        elif (computer == "Paper" and player == "Rock") or (computer == "Scissors" and player == "Paper") or (
                computer == "Rock" and player == "Scissors"):
            computer_point += 1
            result = "Computer won Round {}".format(play_round)
        else:
            print("Enter the correct input from {}".format(history["choices"]))
            continue

    history[play_round] = {"computer_choice": computer, "player_choice": player, "result": result,
                           "points": "player point : {}, computer point : {}".format(player_point, computer_point)}
    play_round += 1


if player_point == computer_point:
    print("Both get equal points : {}, so game becomes tie.".format(player_point, computer_point))
else:
    if player_point > computer_point:
        print("Player gets {} points. \ncomputer gets {} points. \nWinner is Player".format(player_point, computer_point))
    else:
        print("Player gets {} points. \ncomputer gets {} points. \nWinner is Computer".format(player_point, computer_point))


details = int(input("Enter the round for which you need a information >> "))
print("Player choice = {} \nComputer choice = {} \n{}".format(history[details]["player_choice"], history[details]["computer_choice"], history[details]["result"]))

