import random


def screen(choice):
    print("|{}|{}|{}|".format(choice[0], choice[1], choice[2]))
    print("|{}|{}|{}|".format(choice[3], choice[4], choice[5]))
    print("|{}|{}|{}|".format(choice[6], choice[7], choice[8]))


def row_check(val, sym):
    for row in range(0, 7, 3):
        if val[row] == val[row+1] == val[row+2] == sym:
            return True
    return False


def col_check(val, sym):
    for row in range(0, 3):
        if val[row] == val[row+3] == val[row+6] == sym:
            return True
    return False


def diag_check(val, sym):
    if val[0] == val[4] == val[8] == sym:
        return True
    elif val[2] == val[4] == val[6] == sym:
        return True
    else:
        return False


def compare(valuee, symbol):
    return row_check(valuee, symbol) or col_check(valuee, symbol) or diag_check(valuee, symbol)


def play_game():
    his = [None]*10
    flag = 0
    options = ["X", "O"]
    values = [" "]*9
    sample = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(0, 9):
        if i % 2 == 0:
            while True:
                user = int(input("Now your turn, select a position :"))
                if user in sample:
                    sample.remove(user)
                    values[user] = options[0]
                    screen(values)
                    his[i] = values
                    if compare(values, options[0]):
                        result = "User Won the Game"
                        his[9] = result
                        flag = 1
                    break
                else:
                    print("selected position is already occupied, select another position..")
                    continue
            if flag == 1:
                break
        else:
            print("Computer turn")
            computer = random.choice(sample)
            sample.remove(computer)
            values[computer] = options[1]
            screen(values)
            his[i] = values
            if compare(values, options[1]):
                result = "Computer Won the Game"
                his[9] = result
                break
    if i == 8:
        result = "Tie in Game"
        his[i+1] = result

    return his


# main part
game_rounds = 1
history = {}
sam = [0, 1, 2, 3, 4, 5, 6, 7, 8]
while game_rounds <= 10:
    screen(sam)
    history[game_rounds] = play_game()
    game_rounds += 1

details = int(input("Are you want to see any round :"))
for key, value in history.items():
    if key == details:
        for element in range(len(value)-1):
            if value[element] is not None:
                print("Move {}".format(element+1))
                screen(value[element])
        print(value[-1])
