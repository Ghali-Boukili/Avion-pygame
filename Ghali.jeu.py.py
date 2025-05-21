# -*- coding: utf-8 -*-

import pygame
import sys
import random

pygame.init() # initialisation du module "pygame" 

fenetre = pygame.display.set_mode( (800,500) ) # Création d'une fenêtre graphique de taille 600x600 pixels
pygame.display.set_caption("Super Plane") 


# Chargement des images:
#    On définit et affecte les variables qui contiendront les images du vaisseau ou de l'alien
imageAvion = pygame.image.load("plane.png")
imageAvion = pygame.transform.scale(imageAvion, (72, 48))
imageAvionPerdu = pygame.image.load("planePerdu.png")
imageAvionPerdu = pygame.transform.scale(imageAvionPerdu, (72, 48))
imageAlien = pygame.image.load("alien2.png")
imageNuage = pygame.image.load("Cloud.png")
FondBleu = pygame.image.load("fondBleu.png")
FondBleu = pygame.transform.scale(FondBleu, (800, 500))


# On définit les variables qui contiendront les positions des différents éléments (vaisseau, alien, projectile)
# Chaque position est un couple de valeur '(x,y)'

positionAvion = (738,250)


# Fonction en charge de dessiner tous les éléments sur notre fenêtre graphique.
# Cette fonction sera appelée depuis notre boucle infinie
def dessiner():
    global fenetre
    # On remplit complètement notre fenêtre avec la couleur noire: (0,0,0)
    # Ceci permet de 'nettoyer' notre fenêtre avant de la dessiner
    
    fenetre.blit(FondBleu, (0,0))
    fenetre.blit(imageAvion, positionAvion) # On dessine l'image du vaisseau à sa position
    
    pygame.display.flip() # Rafraichissement complet de la fenêtre avec les dernières opérations de dessin


# Fonction en charge de gérer les évènements clavier (ou souris)
# Cette fonction sera appelée depuis notre boucle infinie
def gererClavierEtSouris():
    global positionAvion
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
            continuer = 0
    # Gestion du clavier: Quelles touches sont pressées ?
    touchesPressees = pygame.key.get_pressed()
    if touchesPressees[pygame.K_SPACE] == False:
        appui=False
    #if touchesPressees[pygame.K_SPACE] == True and appui==False and nbproj>0:
     #   projectiles.append((positionVaisseau[0]+32,positionVaisseau[1]))
     #   nbproj=nbproj-1
     #   appui=True
    if touchesPressees[pygame.K_UP] == True and positionAvion[1]>0:
        positionAvion = ( positionAvion[0] , positionAvion[1]-5)
    if touchesPressees[pygame.K_DOWN] == True and positionAvion[1]<452:
        positionAvion = ( positionAvion[0]  , positionAvion[1]+5)
    if touchesPressees[pygame.K_RIGHT] == True and positionAvion[0]<728:
        positionAvion = ( positionAvion[0] + 2 , positionAvion[1])
    if touchesPressees[pygame.K_LEFT] == True and positionAvion[0]>0:
        positionAvion = ( positionAvion[0] - 2 , positionAvion[1])

# On crée une nouvelle horloge qui nous permettra de fixer la vitesse de rafraichissement de notre fenêtre
clock = pygame.time.Clock()

# La boucle infinie de pygame:
# On va continuellement dessiner sur la fenêtre, gérer les évènements et calculer certains déplacements
continuer = 1
while continuer==1:
    # pygame permet de fixer la vitesse de notre boucle:
    # ici on déclare 50 tours par secondes soit une animation à 50 images par secondes
    clock.tick(50) 

    dessiner()
    gererClavierEtSouris()


## A la fin, lorsque l'on sortira de la boucle, on demandera à Pygame de quitter proprement
pygame.quit()
sys.exit()



