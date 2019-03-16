#Importation des bibliothèques nécessaires
import os, sys
import pygame
from pygame.locals import *

#the good way
os.chdir('D:\\bureau\\ISN')

#Initialisation de la bibliothèque Pygame
pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("blanc.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
sole = pygame.image.load("sole.png").convert()
fenetre.blit(sole, (-1,456))


#rafraîchir l'écran
pygame.display.flip()

continuer = 1

#Boucle infinie
while continuer:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = 0      #On arrête la boucle
