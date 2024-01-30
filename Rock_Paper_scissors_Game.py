import random as rand

def play():
    user= input("'R' for rock, 'P' for paper & 'S' for scissors : ")
    Computer=rand.choice(['r','p','s'])
    print("computer chose %s" %Computer )
    if user==Computer:
        return 'Its a tie!!!!'
    if Winner(user,Computer):
        return 'You Won!!!!!'
    return 'you lost!!!!!'

def Winner(player,opponent):
   
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
print(play())