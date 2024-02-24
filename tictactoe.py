import random

# Evangelos Georgosoulis
# difficulty modes for pve
# easy - random
# medium -
# hard -


def board(list):  # emfanhsh pinaka trilizas
    print("-------------")
    print(f"|{list[0]}|{list[1]}|{list[2]}|")
    print("-------------")
    print(f"|{list[3]}|{list[4]}|{list[5]}|")
    print("-------------")
    print(f"|{list[6]}|{list[7]}|{list[8]}|")
    print("-------------")


def check_win(list, score1, score2, win, vs):  # elegxos gia tripleta win
    if list[0] == list[1] == list[2] == "\033[91m X \033[0m":
        print("Player 1 wins!")
        win = True
        score1 += 1
        return score1, score2, win
    elif list[3] == list[4] == list[5] == "\033[91m X \033[0m":
        print("Player 1 wins!")
        win = True
        score1 += 1
        return score1, score2, win
    elif list[6] == list[7] == list[8] == "\033[91m X \033[0m":
        print("Player 1 wins!")
        win = True
        score1 += 1
        return score1, score2, win
    elif list[0] == list[3] == list[6] == "\033[91m X \033[0m":
        print("Player 1 wins!")
        win = True
        score1 += 1
        return score1, score2, win
    elif list[1] == list[4] == list[7] == "\033[91m X \033[0m":
        print("Player 1 wins!")
        win = True
        score1 += 1
        return score1, score2, win
    elif list[2] == list[5] == list[8] == "\033[91m X \033[0m":
        print("Player 1 wins!")
        win = True
        score1 += 1
        return score1, score2, win
    elif list[0] == list[4] == list[8] == "\033[91m X \033[0m":
        print("Player 1 wins!")
        win = True
        score1 += 1
        return score1, score2, win
    elif list[6] == list[4] == list[2] == "\033[91m X \033[0m":
        print("Player 1 wins!")
        win = True
        score1 += 1
        return score1, score2, win

    if list[0] == list[1] == list[2] == "\033[96m O \033[0m":
        print(f"{vs} wins!")
        win = True
        score2 += 1
        return score1, score2, win
    elif list[3] == list[4] == list[5] == "\033[96m O \033[0m":
        print(f"{vs} wins!")
        win = True
        score2 += 1
        return score1, score2, win
    elif list[6] == list[7] == list[8] == "\033[96m O \033[0m":
        print(f"{vs} wins!")
        win = True
        score2 += 1
        return score1, score2, win
    elif list[0] == list[3] == list[6] == "\033[96m O \033[0m":
        print(f"{vs} wins!")
        win = True
        score2 += 1
        return score1, score2, win
    elif list[1] == list[4] == list[7] == "\033[96m O \033[0m":
        print(f"{vs} wins!")
        win = True
        score2 += 1
        return score1, score2, win
    elif list[2] == list[5] == list[8] == "\033[96m O \033[0m":
        print(f"{vs} wins!")
        win = True
        score2 += 1
        return score1, score2, win
    elif list[0] == list[4] == list[8] == "\033[96m O \033[0m":
        print(f"{vs} wins!")
        win = True
        score2 += 1
        return score1, score2, win
    elif list[6] == list[4] == list[2] == "\033[96m O \033[0m":
        print(f"{vs} wins!")
        win = True
        score2 += 1
        return score1, score2, win

    return score1, score2, win


def scoreboard(score1, score2, vs):  # pinakas score
    print("------------SCOREBOARD------------")
    print(f"\033[91mPlayer 1\033[0m \t \t \033[96m{vs}\033[0m\n")
    print(f"   \033[91m{score1}\033[0m\t\t\t    \033[96m{score2}\033[0m")
    print("----------------------------------")


def player1(list):  # Player 1 plays
    print("Player 1 has '\033[1;32;0m X'")
    slot = int(input("Choose your next move (0-8):"))
    while list[slot] != "   ":  # elegxos an exei hdh gemisei to slot
        print("Space occupied!. Choose again:")
        slot = int(input("Choose your next move (0-8):"))
    list[slot] = "\033[91m X \033[0m"  # vale 'X' me xrwma kokkino


def player2(list):  # Player 2 plays
    print("Player 2 has 'O'")
    slot = int(input("Choose your next move (0-8):"))
    while list[slot] != "   ":
        print("Space occupied!. Choose again:")
        slot = int(input("Choose your next move (0-8):"))
    list[slot] = "\033[96m O \033[0m"  # vale 'O' me xrwma mple


def computer(list):  # Computer plays
    print("Computer has 'O")

    move = random.randint(0, 8)
    while list[move] != "   ":
        move = random.randint(0, 8)
    list[move] = "\033[96m O \033[0m"  # vale 'O' me xrwma mple


def difficulty():  # epilogh duskolias
    diff = int(input("Choose difficulty\n 1.Easy 2.Medium 3.Hard\n"))
    while diff != 1 and diff != 2 and diff != 3:
        print("Wrong option. Choose again.")
        diff = int(input("Choose difficulty\n 1.Easy 2.Medium 3.Hard\n"))
    return diff


def main():
    option = 1
    score1, score2 = 0, 0
    diff = 0
    vs = ""

    while option != 2:  # option = 2 == end game
        list = ["   "] * 9  # arxikopoihsh listas me kena

        play_mode = int(
            input("Choose a mode...\n 1.Player vs Player\n 2.Player vs Computer\n")
        )
        while play_mode != 1 and play_mode != 2:  # elegxos gia swstes times
            print("Error. Try again.")
            play_mode = int(
                input("Choose a mode...\n 1.Player vs Player\n 2.Player vs Computer\n")
            )

        if play_mode == 1:  # PvP
            vs = "Player2"
            win = False
            board(list)
            while win == False and list.__contains__("   "):
                # loop mexri na gemisei o pinakas/nikh
                player1(list)
                board(list)
                score1, score2, win = check_win(list, score1, score2, win, vs)
                if win == False and list.__contains__("   "):
                    # periptwsh pou gemizei o pinakas
                    player2(list)
                    board(list)
                    score1, score2, win = check_win(list, score1, score2, win, vs)

            if win == False:
                print("ITS A TIE!")
        elif play_mode == 2:  # PvE
            vs = "Computer"
            win = False
            diff = difficulty()
            board(list)
            if diff == 1:  # easy mode
                while win == False and list.__contains__("   "):
                    player1(list)
                    board(list)
                    score1, score2, win = check_win(list, score1, score2, win, vs)
                    if win == False and list.__contains__("   "):
                        computer(list)
                        board(list)
                        score1, score2, win = check_win(list, score1, score2, win, vs)
                if win == False:
                    print("ITS A TIE!")
            elif diff == 2:  # medium mode
                pass
            elif diff == 3:  # hard mode
                pass

        scoreboard(score1, score2, vs)  # emfanhsh pinaka score

        option = int(input("Do you want to play again?\n 1. YES\n 2. NO\n"))
        while option != 1 and option != 2:
            print("Error. Try again.")
            option = int(input("Do you want to play again?\n 1. YES\n 2. NO\n"))

    print("\033[95m~Thanks for playing~\033[0m")


if __name__ == "__main__":
    main()
