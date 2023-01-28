import random
rand=random.randint(1,3)
if rand==1:
    comp='p'
elif rand==2:
    comp='s'
elif rand==3:
    comp='r'
def game(a, comp):
    if a==comp:
        return None
    elif comp=='p':
        if a=='r':
            return False
        elif a=='s':
            return True
    elif comp=='s':
        if a=='p':
            return False
        elif a=='r':
            return True
    elif comp=='r':
        if a=='p':
            return True
        elif a=='s':
            return False
a=input('Player choose: Paper(p), Scissor(s), and Rock(r)')

print('Computer choose: ', comp,' Player Choose: ', a)
b=game(a, comp)
if b==True:
    print('Player wins')
elif b==False:
    print('Player Loses')
elif b==None:
    print('Game was a tie')