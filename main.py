#Jeu de dés contre ordinateur


#import de la fonction random
import random

#import de la fonction time pour ralentir le jeu
import time

#text to ascii for visual in shell
print("""  _____  _             _____                      
 |  __ \(_)           / ____|                     
 | |  | |_  ___ ___  | |  __  __ _ _ __ ___   ___ 
 | |  | | |/ __/ _ \ | | |_ |/ _` | '_ ` _ \ / _ \`
 | |__| | | (_|  __/ | |__| | (_| | | | | | |  __/
 |_____/|_|\___\___|  \_____|\__,_|_| |_| |_|\___|
                                                  
                                                  """)
def des():
    #variables et utilisation de l'aléatoire avec random
    player = random.randint(1,20)
    print("Vous lancez votre dé...")
    time.sleep(2)
    print("Vous avez obtenu : " + str(player))

    time.sleep(2)
    print()

    ai = random.randint(1,20)
    print("L'ordinateur lance son dé...")
    time.sleep(2)
    print("L'ordinateur a obtenu : " + str(ai))

    time.sleep(1)
    print()

    #condition de victoire
    if player > ai :
        print("Vous avez gagné !")
    elif player == ai :
        print("Ex-aequo")
    else :
        print("Vous avez perdu !")

    print()
    print("Voulez-vous quitter ? O/N")
    cont = input()

    if cont == "O" or cont == "o" :
        exit()
    elif cont == "N" or cont == "n" : 
        pass
    else :
        print("Je n'ai pas compris votre réponse. Jouons à nouveau.")

#main loop
while True :
    print("Appuyez sur Entrée pour lancer votre dé.")
    roll = input()
    des()