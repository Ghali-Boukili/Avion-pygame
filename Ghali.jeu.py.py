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
imageAvion1 = pygame.transform.scale(imageAvion, (144, 96))
imageAvionPerdu = pygame.image.load("planePerdu.png")
imageAvionPerdu = pygame.transform.scale(imageAvionPerdu, (72, 48))
imageNuage = pygame.image.load("Cloud.png")
imageNuage = pygame.transform.scale(imageNuage,(75,70))
imageAlien = pygame.image.load("alien2.png")
imageAlien = pygame.transform.scale(imageAlien,(45,40))
FondBleu = pygame.image.load("fondBleu.png")
FondBleu = pygame.transform.scale(FondBleu, (800, 500))


fontDebut1 = pygame.font.SysFont("Knewave", 40)
texteDebut1 = fontDebut1.render("---> Appuyez sur 'ESPACE' pour commencer ", True, (0, 0, 0))
positionTexteDebut1 = texteDebut1.get_rect(center=(400, 220))  # centré

texteDebut2 = fontDebut1.render("---> Appuyez sur 'ENTREE' pour quitter", True, (0, 0, 0))
positionTexteDebut2 = texteDebut2.get_rect(center=(366, 270))

fontDebut3 = pygame.font.SysFont("Confortaa", 80)
texteDebut3 = fontDebut3.render("Super Plane", True, (255, 180, 0))
positionTexteDebut3 = texteDebut3.get_rect(center=(400, 40))

fontFin = pygame.font.SysFont("Arial", 100)
texteFin = fontFin.render("T'ES GUEZ", True, (255, 255, 255))
positionTexteFin = texteFin.get_rect(center=(420, 300))



# On définit les variables qui contiendront les positions des différents éléments (vaisseau, alien, projectile)
# Chaque position est un couple de valeur '(x,y)'

positionAvion = (728,250)
positionNuage = (0,9)

positionAlien = (200,200)

# définir le nb d'aliens et comment ils sont espacés entre eux horizontalement et verticalement 
Aliens = [(110+i*60,110+j*50)for i in range(3) for j in range(6)] # i : nb d'aliens horizontalement et j : nb d'aliens verticalement

boules = []
bombes = []

Nuages = [(110+i*50,40+j*40) for i in range(6) for j in range(1)]
nouveauxNuages = (0,9)

a = 3
niveau= 1
score = 0
m=2

Porte1 = (1,random.randint(80,400))
Porte2 = (1,Porte1[1]+60)
Porte3 = (50,Porte1[1])

rectPorte1 = pygame.Rect(Porte1[0], Porte1[1], 50, 3)
rectPorte2 = pygame.Rect(Porte2[0], Porte2[1], 50, 3)
rectPorte3 = pygame.Rect(Porte3[0], Porte1[1], 2, 62)

  

rectAvion =  pygame.Rect(positionAvion[0],positionAvion[1], 72, 48 )

for positionAlien in Aliens :
    rectAlien = pygame.Rect(positionAlien[0], positionAlien[1], 45,40)

for positionNuage in Nuages:
    rectNuage = pygame.Rect(Porte3[0], Porte1[1], 75,70)

debutJeu = False 

def dessiner():
    global fenetre, debutJeu
    
    if not debutJeu:
        fenetre.fill((211, 211,211))  # Fond gris
        fenetre.blit(texteDebut1, positionTexteDebut1)
        fenetre.blit(texteDebut2, positionTexteDebut2)
        fenetre.blit(texteDebut3, positionTexteDebut3)
        fenetre.blit(imageAvion1, (330,350))
        
    
    
    else :
        fenetre.blit(FondBleu, (0,0))
        fenetre.blit(imageAvion, positionAvion) # On dessine l'image du vaisseau à sa position
    
        for positionNuage in Nuages:
            fenetre.blit(imageNuage, positionNuage)
    
        for positionAlien in Aliens:
            fenetre.blit(imageAlien, positionAlien)
        
        pygame.draw.rect(fenetre, (0,0,0), rectPorte1, 5)    
        pygame.draw.rect(fenetre, (0,0,0), rectPorte2, 5)
        pygame.draw.rect(fenetre, (255,255,255), rectPorte3, 10)
    
    
    pygame.display.flip() # Rafraichissement complet de la fenêtre avec les dernières opérations de dessin


# Fonction en charge de gérer les évènements clavier (ou souris)
def gererClavierEtSouris():
    global positionAvion, debutJeu, continuer
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
            continuer = 0
    # Gestion du clavier: Quelles touches sont pressées ?
    touchesPressees = pygame.key.get_pressed()
    if not debutJeu:
        if touchesPressees[pygame.K_SPACE]:
            pygame.time.wait(1000)
            debutJeu = True
        elif touchesPressees[pygame.K_RETURN]:
            continuer = 0 
    elif debutJeu :
        if touchesPressees[pygame.K_SPACE] == False:
            appui=False 
    #if touchesPressees[pygame.K_SPACE] == True and appui==False and nbproj>0:
     #   projectiles.append((positionVaisseau[0]+32,positionVaisseau[1]))
     #   nbproj=nbproj-1
     #   appui=True
        if touchesPressees[pygame.K_UP] == True and positionAvion[1]>80:
            positionAvion = ( positionAvion[0] , positionAvion[1]-5)
        if touchesPressees[pygame.K_DOWN] == True and positionAvion[1]<452:
            positionAvion = ( positionAvion[0]  , positionAvion[1]+5)
        if touchesPressees[pygame.K_RIGHT] == True and positionAvion[0]<728 and positionAvion[0]>0:
            positionAvion = ( positionAvion[0] + 2 , positionAvion[1])
        #if touchesPressees[pygame.K_LEFT] == True and positionAvion[0]>0:
            #positionAvion = ( positionAvion[0] - 2 , positionAvion[1])
    #else :
        #if

# On crée une nouvelle horloge qui nous permettra de fixer la vitesse de rafraichissement de notre fenêtre
clock = pygame.time.Clock()

# La boucle infinie de pygame:
# On va continuellement dessiner sur la fenêtre, gérer les évènements et calculer certains déplacements
continuer = 1
while continuer==1:
    # pygame permet de fixer la vitesse de notre boucle:
    # ici on déclare 50 tours par secondes soit une animation à 50 images par secondes
    clock.tick(50)
    positionAvion = (positionAvion[0] - 0.4, positionAvion[1])
    dessiner()
    gererClavierEtSouris()

    for i in range(len(Nuages)):
            Nuages[i] = (Nuages[i][0]+a, Nuages[i][1])
            if Nuages[i][0] > 800:
                Nuages[i] = nouveauxNuages
            if score != 0 :
                niveau += 1
                a += 0.05
                score = 1
                
    
    
    
    
    
    
    
    
    
    
    if rectAvion.colliderect(rectAlien):
        positionAvion.remove()
        imageAvion = imageAvionPerdu
        for i in range(len(positionAvion)):
            positionAvion[i] = (positionAvion[i][0],positionAvion[i][1]+4) 
                
    
    
    # On vérifie si on doit inverser la direction AVANT de rebouger encore
    for alien in Aliens:
        if alien[1] + m >= 450 or alien[1] + m <= 100:
            m = m*(-1)
            break

    # déplace tt les aliens en mm temps
    for i in range(len(Aliens)):
        if positionAvion != (-1, -1):
            Aliens[i] = (Aliens[i][0], Aliens[i][1] + m)
    
    
    
    
    
    
    
    
    
    
    

## A la fin, lorsque l'on sortira de la boucle, on demandera à Pygame de quitter proprement
pygame.quit()
sys.exit()



