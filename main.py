import random


def play():
    user = input(""""what's your choice? 'r' for rock, 'p' for paper , 's' for scissors\n  """)
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "you and your computer both chosen {}. So it's a tie ".format(computer)
    if is_win(user, computer):
        return "you have chosen {} and the computer has chosen {}. You won!".format(user, computer)
    return " your have choose {} adn the computer has chosen {}. you lost :(".format(user, computer)


def is_win(player, opponent):
    # return true is the player beats the opponent
    # winning conditions: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player=='s' and opponent =='p') or (player == 'p' and opponent == 'r' ):
        return True
    return False


play()
