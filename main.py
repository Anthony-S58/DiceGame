#Jeu de dés contre ordinateur


#import de la fonction random
import random

#variables et utilisation de l'aléatoire avec random
player = random.randint(1,20)
ai = random.randint(1,20)

#condition de victoire
if player > ai :
    print("Vous avez gagné !")
else :
    print("Vous avez perdu !")