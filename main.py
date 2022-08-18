#Jeu de dés contre ordinateur


#import de la fonction random
import random

#text to ascii for visual in shell
print("""  _____  _             _____                      
 |  __ \(_)           / ____|                     
 | |  | |_  ___ ___  | |  __  __ _ _ __ ___   ___ 
 | |  | | |/ __/ _ \ | | |_ |/ _` | '_ ` _ \ / _ \`
 | |__| | | (_|  __/ | |__| | (_| | | | | | |  __/
 |_____/|_|\___\___|  \_____|\__,_|_| |_| |_|\___|
                                                  
                                                  """)

#variables et utilisation de l'aléatoire avec random
player = random.randint(1,20)
print("Vous avez obtenu : " + str(player))

ai = random.randint(1,20)
print("L'ordinateur a obtenu : " + str(ai))

#condition de victoire
if player > ai :
    print("Vous avez gagné !")
else :
    print("Vous avez perdu !")