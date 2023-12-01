from random import randint
from time import *
from tools import askN_Y,askInt



keypadOrd = [7,8,9,4,5,6,1,2,3]
emojilist = ("❌","⭕️")

def askPlacement(prompt : int) -> int: #fonction pour verifier que les joueurs ne joue pas sur une case deja joue
    while True:
        value = askInt(prompt)
        if 1 <= value <= 9:
            if Gametab[keypadOrd[value-1]-1] == "":
                return value
            else:
                print("\n\t/!\\ Try again with a position unused (cheater) /!\\")
        else:
            print("\n\t/!\\ Try again with a number between 1 and 9 /!\\")

def print_tic_tac_toe(Gametab): #fonction permettant d'afficher la grille tic tac toe avec les symboles de chaque joueur remplace par des emojis 
    val = []
    for i in range(len(Gametab)):
        val.append(Gametab[i])
    for x in range(len(val)):
        if val[x] == "X" or val[x] == emojilist[0]:
            val[x]= emojilist[0]
        elif val[x] == "O" or val[x] == emojilist[1]:
            val[x]= emojilist[1]
        else:
            val[x] = "  "
    
    print("\n\t     |     |\n\t {}  | {}  | {}".format(val[0], val[1], val[2]))
    print("\t_____|_____|_____\n\t     |     |\n\t {}  | {}  | {}".format(val[3], val[4], val[5]))
    print("\t_____|_____|_____\n\t     |     |\n\t {}  | {}  | {}".format(val[6], val[7], val[8]))
    print("\t     |     |\n")
    
def check_win(p_coord_list): #fonction permettant de verifier si le symbole que l'on renseigne dans variable de la fonction, a gagne
    # All possible winning combinations
    soln = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6], [0, 4, 8]]
    win=0
    # Loop to check if any winning combination is satisfied
    for x in range (len(soln)):
        if win<3:
            win=0
            for k in range(len(p_coord_list)):
                for i in range (3):
                    if p_coord_list[k]==soln[x][i]:
                        win=win+1
        else:
            return True
    if win>=3:
        return True
    return False

def check_winner(X_list,O_list): #fonction permettant de verifier si l'un des deux joueurs a gagne
    global game
    global Party
    if check_win(X_list):
        print_tic_tac_toe(Gametab)
        print("Player X has won the game!!")     
        print("\n")
        Party = False
    elif check_win(O_list):
        print_tic_tac_toe(Gametab)
        print("Player O has won the game!!")     
        print("\n")
        Party = False
    elif not("" in Gametab):
        Party = False

def O_play(): #fonction que l'on utilise pour faire jouer le joueur O (l'humain)
    o_coup =keypadOrd[askPlacement("Where do you want to play: ")-1]-1
    Gametab[o_coup] = "O"
    O_list.append(o_coup)
    
def X_play(): #fonction que l'on utilise pour faire jouer le joueur X (le bot)
    x_coup=algoS()
    #x_coup=keypadOrd[askPlacement("Where do you want to play: ")-1]-1
    Gametab[x_coup] = "X"
    X_list.append(x_coup)

def algoS(): #algorythme du bot intelligent verifiant si une combinaison gagnante est possible pour lui ou pour son adversaire, et qui prend la place pour contrer ou gagner
    global X_list
    global O_list
    global Gametab
    
    for i in range(9):  #Verification d'une possibilité de victoire
        if Gametab[i] == "":
            X_list.append(i)
            if check_win(X_list) == True:
                val = i
                X_list.pop(-1)
                return val
            X_list.pop(-1)
            
    for j in range(9):  #Verification d'une possibilité d'empecher une défaite
        if Gametab[j] == "":
            O_list.append(j)
            if check_win(O_list) == True:
                val = j
                O_list.pop(-1)
                return val
            O_list.pop(-1)
            
    #Verification d'une possibilité de victoire
    val = randint(0,8)
    while Gametab[val] != "":
        val = randint(0,8)
    return val

def game():
    game : bool = True
    global Party
    global Gametab
    global X_list
    global O_list
    while game == True: #boucle pour pouvoir refaire des parties sans avoir a relancer le programme
        print_tic_tac_toe(Gametab)
        Party = True
        while Party == True:
            
            O_play()
            print_tic_tac_toe(Gametab)
            check_winner(X_list,O_list)
            if Party == False:
                break
            X_play()
            print_tic_tac_toe(Gametab)
            check_winner(X_list,O_list)
            
        game = askN_Y("restart ? Y/N \n")
        Gametab=["","","","","","","","",""]
        X_list =[]
        O_list =[]


print("For this tic-tac-toe we will use the key board\n7|8|9\n4|5|6\n1|2|3\ncause it's the most common in keypads.")

Gametab=["","","","","","","","",""]
X_list =[]
O_list =[]
Party : bool = True
game()