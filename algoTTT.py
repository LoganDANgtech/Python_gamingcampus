
def algo(Gametab,lastAction):
    wincond : int  = ()
    
    #Ojoue corner
    if lastAction == "millieu":#joueur joue millieu
        pass
        #Ojoue opposite corner
        if lastAction == "corner": #joueur joue corner
            pass
            #Ojoue corner a bloquer (si 1 -> 9 | si 3 -> 7 | si 7 -> 3 | si 9 -> 1)
            #joueur joue x
            #Ojoue win cond (border non bloquée)
            ###     END     ###
        else:   #joueur joue border
            pass
            #Obloque wincond
            if wincond == False: #Joueur bloque wincond
                pass
                #Obloque wincond

                #joueur joue border
                #Obloque wincond
                ###     END     ### (1 tie)
            else:   #Joueur ne bloque pas la wincond
                pass
                #Ojoue wincond
                ###     END     ###

            
    elif lastAction == "corner": #joueur joue corner
        pass
        #Oforce play avec un corner adjacent
        if wincond == False:    #joueur bloque wincond
            pass
            #Ojoue last corner
            if lastAction == "millieu": #joueur joue millieu
                pass
                #Ojoue win cond (border entre 2 corner)
                ###     END     ###
            else: #joueur joue border
                pass
                #Ojoue win cond (millieu)
                ###     END     ###


        else:   #joueur ne bloque pads la wincond
            pass
            #Ojoue win cond (border entre 2 corner)
            ###     END     ###



    elif lastAction == "bord": #joueur joue bord
        pass
        #Oforce play corner
        if wincond == False:    #joueur bloque wincond
            pass
            #Ojoue mid
            #joueur joue x
            #Ojoue win cond
            ###     END     ###


        else:
            pass
            #Ojoue win cond (border entre 2 corner)
            ###     END     ###