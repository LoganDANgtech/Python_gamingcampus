from random import randint
from tools import *

EmojiOrd = ["📄","🏔️","✂️"]     #papier -> pierre -> ciseaux

win_round = [(("Tie !\n"),(0,0)),               #tuple comptage points = gauche:win , droite;loose
             (("You won the round !\n"),(1,0)),
             (("You loosed the round\n"),(0,1))]

win_game = ["You loosed the game...","It's a tie you have the same score !","You won the game !!!"]

win_round_matrix =  [((0),(1),(2)),   # 0:tie 1:win 2:loose
                     ((2),(0),(1)),
                     ((1),(2),(0))]

def asksign(prompt : int) -> int:     #fonction pour forcer la saisie d'un nombre entre 1 et 3
    while True:
        value : int = askInt(prompt)
        while not( 1 <= value <= 3 ):
            print("\n\t/!\\ Try again with a number between 1 and 3 /!\\")
            value = int(askInt(prompt))
        return value

def Vs(Uenter,Oenter,scoreU,scoreO):
    print(EmojiOrd[Uenter-1] + "\tvs\t" + EmojiOrd[Oenter-1])
    print(win_round[win_round_matrix[Uenter-1][Oenter-1]][0])
    
    scoreU = scoreU + int(win_round[win_round_matrix[Uenter-1][Oenter-1]][1][0])
    scoreO = scoreO + int(win_round[win_round_matrix[Uenter-1][Oenter-1]][1][1])
    return scoreU,scoreO

def result(scoreU,scoreO):
    scoreU +=1
    scoreO +=1
    print(win_game[ min( 2 , int(( scoreU/scoreO  + (scoreU/scoreO > 1)*( scoreU%scoreO ) )) ) ])   #calcul du score avec une condititon


def game():
    game : bool = True
    irepConfigtries : int = askInt("\nHow many rounds do you want to play: ")
    while game == True:

        ListcoupU = []  #liste coup utilisateur
        ListcoupO = []  #liste coup ordi

        scoreU : int = 0
        scoreO : int = 0
        
        for i in range(0,irepConfigtries):
            ListcoupO.append(randint(1,3))

        print("1 = 📄\n2 = 🏔️\n3 = ✂️\n")

        for i in range(0,irepConfigtries):
            Uselect : int = asksign("Choose your sign: ")
            ListcoupU.append(Uselect)
            scoreU,scoreO = Vs(ListcoupU[i],ListcoupO[i],scoreU,scoreO)
            

        print("\n\t"+ str(scoreU) + " : " + str(scoreO) +"")
        result(scoreU,scoreO)

        game = askN_Y("restart ? Y/N \n")


game()