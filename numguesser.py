from random import randint  #On utiliseras seulement la fonction randint de random

init : bool = True


def askInt(prompt) -> int:  #Fonction pour forcer la saisie d'un nombre (entier)
    while True:
        try:
            value: int = int(input(prompt))
            return value
        
        except ValueError:
            print("/!\\ Try again with a number /!\\")

def Config_tries():  #Configuration du nombre d'essais
    global itrytot
    srepConfigtry : str = input("\nDo you want to configure your tries ? Y/N\n")    
    if srepConfigtry == "Y" or srepConfigtry == "y":
        itrytot = askInt("New tries: ")

def Config_lim():   #Configurations des limites
    global imin
    global imax
    srepConfiglim : str = input("\nDo you want to configure your limits ? Y/N\n")    
    if srepConfiglim == "Y" or srepConfiglim == "y":
        imin = askInt("New minimum: ")
        imax = askInt("New maximum: ")
        if imin > imax:
            iplaceholder : int = imin 
            imin = imax 
            imax = iplaceholder
            print("the minimum and maximum didn't match they were swapped.")

def game(itrytot,imin,imax):    #Fonction principale du jeu

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
        srepRestart = input("\nYou exceed " + str(itrytot) + " tries ! :,(\nthe number was: " + str(ix) + "\n  restart ? Y/N \n")
    else:
        srepRestart = input("restart ? Y/N \n")

    if srepRestart == "y" or srepRestart == "Y":    #Si le joueur veut rejouer la fonction se rapelle
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
    srepReConfig : str = input("Do you want to re-configure the game ? Y/N\n")
    if not(srepReConfig == "Y" or srepReConfig == "y"):
        init = False