import random
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
else:
    comp='g'
def game( player1, player2):
    if a==comp:
        return None
    elif comp=='s':
        if a=='w':
            return False
        elif a=='g':
            return True
    elif comp=='w':
        if a=='g':
            return False
        elif a=='s':
            return True
    elif comp=='g':
        if a=='s':
            return False
        elif a=='w':
            return True
a=input('Player enter : Snake(s), Water(w) or Gun(g)')

print('computer choose:', comp, 'player choose:', a)

b=game(comp, a)

if b==None:
    print('The match was tie')
elif b==True:
    print('Player wins')
elif b==False:
    print('Player lose')
