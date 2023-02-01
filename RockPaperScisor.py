import random
def rps():
    user=input("what your choice?; \nr for Rock \ns for Scisor\np for Paper\n")
    computer=random.choice(['r','s','p'])
    print(f"computer chosen {computer}")
    if user==computer:
        return "draw"
    if win(user,computer):
        return "you win"
    return "you lose"
def win(player,opponent):
    if (player=='r' and opponent=='s')or(player=='s' and opponent=='p')or(player=='p' and opponent=='r'):
        return True
print(rps())

            