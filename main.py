#Jeu de dés contre ordinateur


#import de la fonction random
import random

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