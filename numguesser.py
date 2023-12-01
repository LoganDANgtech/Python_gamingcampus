from random import randint  #On utiliseras seulement la fonction randint de random
from tools import askInt , askN_Y 
init : bool = True


def Config_tries():  #Configuration du nombre d'essais
    global itrytot
    srepConfigtry : str = askN_Y("\nDo you want to configure your tries ? Y/N\n")    
    if srepConfigtry == True:
        itrytot = askInt("New tries: ")

def Config_lim():   #Configurations des limites
    global imin
    global imax
    srepConfiglim : str = askN_Y("\nDo you want to configure your limits ? Y/N\n")    
    if srepConfiglim == True:
        imin = askInt("New minimum: ")
        imax = askInt("New maximum: ")
        if imin > imax:                 #si le minimum est plus élevé que le maximum on les intervertis
            iplaceholder : int = imin 
            imin = imax 
            imax = iplaceholder
            print("the minimum and maximum didn't match they were swapped.")

def game(itrytot : int, imin : int, imax : int):    #Fonction principale du jeu

    itry : int = itrytot
    ix : int = randint(imin,imax)

    while not(itry <= 0):

        print("\n" +str(itry) + " tries left !")
        iguess : int = int(askInt("Take a guess between " + str(imin) + " and " + str(imax) + ": "))
        itry -= 1

        if iguess > ix:
            print("Lower")
        elif iguess < ix:
            print("Higher")
        else:
            print("\nYou guessed right in " + str(itrytot - itry) +" tries !")
            itry = -1

    if itry == 0:
        srepRestart : bool= askN_Y("\nYou exceed " + str(itrytot) + " tries ! :,(\nthe number was: " + str(ix) + "\n  restart ? Y/N \n")
    else:
        srepRestart : bool = askN_Y("restart ? Y/N \n")

    if srepRestart == True:    #Si le joueur veut rejouer la fonction se rapelle
        game(itrytot,imin,imax)



while init == True:    #Boucle pour initialiser et reconfigurer le jeu
    
    #Init
    imin : int = 0
    imax : int = 100
    itrytot : int = 10 
    
    Config_tries()
    Config_lim()

    #Jeu
    game(itrytot,imin,imax)

    #Reconfigurer le jeu ou fermer
    init = askN_Y("Do you want to re-configure the game ? Y/N\n")
