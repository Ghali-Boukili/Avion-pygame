# -*- coding: utf-8 -*-

import pygame
import sys
import random

pygame.init() # initialisation du module "pygame" 

fenetre = pygame.display.set_mode( (600,600) ) # Création d'une fenêtre graphique de taille 600x600 pixels
pygame.display.set_caption("spaceInvaders") # Définit le titre de la fenêtre


# Chargement des images:
#    On définit et affecte les variables qui contiendront les images du vaisseau ou de l'alien
imageAlien = pygame.image.load("alien.png")
imageVaisseau = pygame.image.load("vaisseau.png")
imageVaisseau = pygame.transform.scale(imageVaisseau, (64, 64)) # On redimensionne l'image du vaisseau à une taille de 64x64 pixels

# On définit les variables qui contiendront les positions des différents éléments (vaisseau, alien, projectile)
# Chaque position est un couple de valeur '(x,y)'
positionVaisseau = (300,525)
aliens = [(110+i*50,40+j*40) for i in range(8) for j in range(4)]
stars = [(random.randint(0,600),random.randint(0,600)) for i in range(100)]
projectiles = []
bombes=[]
appui = False
arial24 = pygame.font.SysFont("arial",24)
nbproj=100
score=0
d=1
change=False


# Fonction en charge de dessiner tous les éléments sur notre fenêtre graphique.
# Cette fonction sera appelée depuis notre boucle infinie
def dessiner():
    global imageAlien, imageVaisseau, fenetre
    # On remplit complètement notre fenêtre avec la couleur noire: (0,0,0)
    # Ceci permet de 'nettoyer' notre fenêtre avant de la dessiner
    fenetre.fill( (0,0,0) )
    for star in stars:
        pygame.draw.circle(fenetre, (255,255,255), star, 2)
    fenetre.blit(imageVaisseau, positionVaisseau) # On dessine l'image du vaisseau à sa position
    surfaceproj = arial24.render("nbproj:"+str(nbproj),True,pygame.Color(0,255,255))
    surfacescore = arial24.render("score:"+str(score),True,pygame.Color(0,255,255))
    fenetre.blit(surfaceproj, (5,5))
    fenetre.blit(surfacescore, (500,5))
    for positionAlien in aliens:
        fenetre.blit(imageAlien, positionAlien)  # On dessine l'image du vaisseau à sa position
    for projectile in projectiles:
        pygame.draw.circle(fenetre, (255,255,255), projectile, 5) # On dessine le projectile (un simple petit cercle)
    for bombe in bombes:
        pygame.draw.circle(fenetre, (255,0,0), bombe, 7)
    pygame.display.flip() # Rafraichissement complet de la fenêtre avec les dernières opérations de dessin


# Fonction en charge de gérer les évènements clavier (ou souris)
# Cette fonction sera appelée depuis notre boucle infinie
def gererClavierEtSouris():
    global continuer, positionVaisseau, projectiles,appui,nbproj
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
            continuer = 0
    # Gestion du clavier: Quelles touches sont pressées ?
    touchesPressees = pygame.key.get_pressed()
    if touchesPressees[pygame.K_SPACE] == False:
        appui=False
    if touchesPressees[pygame.K_SPACE] == True and appui==False and nbproj>0:
        projectiles.append((positionVaisseau[0]+32,positionVaisseau[1]))
        nbproj=nbproj-1
        appui=True
    if touchesPressees[pygame.K_RIGHT] == True and positionVaisseau[0]<536:
        positionVaisseau = ( positionVaisseau[0] + 5 , positionVaisseau[1])
    if touchesPressees[pygame.K_LEFT] == True and positionVaisseau[0]>0:
        positionVaisseau = ( positionVaisseau[0] - 5 , positionVaisseau[1])

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

    # On fait avancer le projectile (si il existe)
    rectVaisseau=pygame.Rect(positionVaisseau,(64,64))
    
    for b in range(len(bombes)):
        rectbombe=pygame.Rect(bombes[b][0]-7,bombes[b][1]-7,14,14)
        bombes[b] = (bombes[b][0],bombes[b][1]+3)
        if bombes[b][1]>600:
            bombes[b]=(-1,-1)
        
        if rectVaisseau.colliderect(rectbombe):
            bombes[b]=(-1,-1)
            print("perdu")
        
        
    
    for k in range(len(stars)):
        stars[k] = (stars[k][0],(stars[k][1]+1)%600)
    
    for j in range(len(aliens)):
        aliens[j] = (aliens[j][0]+d,aliens[j][1])
    
        if aliens[j][0]>567 or aliens[j][0]<0:
            change=True
            
    if change==True:
        for j in range(len(aliens)):
            aliens[j] = (aliens[j][0],aliens[j][1]+10)
        change=False
        d=d*(-1)
    
    
    for i in range(len(projectiles)):
        projectiles[i] = (projectiles[i][0], projectiles[i][1] - 5) # le projectile "monte" vers le haut de la fenêtre
        
        if projectiles[i][1]<0:
            projectiles[i]=(-1,-1)
        
        for j in range(len(aliens)):
            rectalien=pygame.Rect( aliens[j], (33, 27) )
            rectproj=pygame.Rect( projectiles[i][0]-5,projectiles[i][1]-5,10,10)
            if rectalien.colliderect(rectproj):
                projectiles[i]=(-1,-1)
                aliens[j]=(-1,-1)
                score=score+1
        

    
    while (-1,-1) in projectiles:
        projectiles.remove((-1,-1))
    
    while (-1,-1) in aliens:
        aliens.remove((-1,-1))
    
    while (-1,-1) in bombes:
        bombes.remove((-1,-1))
    
    if random.randint(0,100)<2:
        inda=random.randint(0,len(aliens)-1)
        print(inda)
        bombes.append((aliens[inda][0]+16,aliens[inda][1]+34))


## A la fin, lorsque l'on sortira de la boucle, on demandera à Pygame de quitter proprement
pygame.quit()
sys.exit()



