def askInt(prompt : int) -> int:      #fonction pour forcer la saisie d'un nombre (entier)
    while True:
        try:
            value: int = int(input(prompt))
            return value
        
        except ValueError:
            print("\n\t/!\\ Try again with a number /!\\")

def askStr(prompt: str, allowed_inputs: list[str]) -> str:
    while True:
        value: str = input(prompt)
        if value in allowed_inputs:
            return value
        else:
            print("\n\t/!\\ Try again with an allowed input like: "+ str(allowed_inputs) +" /!\\")

        #si value n'est pas dans allowed_inputs, alors on recommence
        #sinon on renvoie value

def askN_Y(prompt : str) -> bool:                       #attends la saisie de Y ou N et renvoie un booléen correspondant
    tradbool = {"y":True,"Y":True,"n":False,"N":False}  #On prefereras l'utilisation de N_Y plutot que ask str pour par
    while True:                                         #exemple le redémarrage de partie
        try:
            value: bool = tradbool[input(prompt)]
            return value
        
        except KeyError:
            print("\n\t/!\\ Try again Y or N /!\\")