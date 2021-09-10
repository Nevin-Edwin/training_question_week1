import random


def game_result(comp, pla, roundd):
    if comp == pla:
        return ["Tie on Round {}".format(roundd), 0, 0]
    else:
        if (comp == 0 and pla == 1) or (comp == 1 and pla == 2) or (
                comp == 2 and pla == 0):
            return ["Player won Round {}".format(roundd), 1, 0]
        else:
            return ["Computer won Round {}".format(roundd), 0, 1]


choices = ["Rock", "Paper", "Scissors"]
history = {}
play_round = 1

while play_round <= 10:
    try:
        computer = random.randint(0, 2)
        player_input = input('your turn choose any one of this [Paper, Rock, Scissors]: ').title()
        player = choices.index(player_input)
        out_fun = game_result(computer, player, play_round)

        history[play_round] = [choices[computer], player_input, out_fun[0],
                               history.get(play_round - 1, [0] * 4)[3] + out_fun[1],
                               history.get(play_round - 1, [0] * 5)[4] + out_fun[2]]
        play_round += 1

    except ValueError as ve:
        print("Enter the input correctly same as [paper, rock, scissors]")

while True:
    try:
        details = int(input("Enter the round for which you need the information >> "))
        print("Player choice = {} \nComputer choice = {} \n{}".format(history.get(details)[1], history.get(details)[0],
                                                                      history.get(details)[2]))
        break

    except:
        print("There is only {} Rounds, please select round between 0 and {}".format(play_round - 1, play_round - 1))
