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

#variables et utilisation de l'aléatoire avec random
player = random.randint(1,20)
print("Vous lancez votre dé...")
time.sleep(2)
print("Vous avez obtenu : " + str(player))

time.sleep(2)

ai = random.randint(1,20)
print("L'ordinateur lance son dé...")
time.sleep(2)
print("L'ordinateur a obtenu : " + str(ai))

time.sleep(1)

#condition de victoire
if player > ai :
    print("Vous avez gagné !")
else :
    print("Vous avez perdu !")