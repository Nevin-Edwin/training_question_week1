import random

history = {"choices": ["Rock", 'Paper', 'Scissors']}
play_round = 1
(player_point, computer_point) = (0, 0)

while play_round <= 10:
    computer = random.choices(history.get("choices"))[0]
    player = str(input('your turn choose any one of this {}:'.format(history.get("choices")))).title()
    result = str()

    if computer == player:
        result = "Tie on Round {} ".format(play_round)
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
            print("Enter the correct input from {}".format(history.get("choices")))
            continue

    history[play_round] = {"computer_choice": computer, "player_choice": player, "result": result,
                           "points": "player point : {}, computer point : {}".format(player_point, computer_point)}
    play_round += 1

if player_point == computer_point:
    print("Both get equal points : {}, so game becomes tie.".format(player_point, computer_point))
else:
    if player_point > computer_point:
        print(
            "Player gets {} points. \ncomputer gets {} points. \nWinner is Player".format(player_point, computer_point))
    else:
        print("Player gets {} points. \ncomputer gets {} points. \nWinner is Computer".format(player_point,
                                                                                              computer_point))

while True:
    try:
        details = int(input("Enter the round for which you need the information >> "))
        print("Player choice = {} \nComputer choice = {} \n{}".format(history.get(details).get("player_choice"),
                                                                      history.get(details).get("computer_choice"),
                                                                      history.get(details).get("result")))
        break

    except ValueError as ve:
        print("Enter the Number between 1 to {}".format(play_round - 1))

    except:
        print("There is only {} Rounds, please select round between {}".format(play_round - 1, play_round - 1))
