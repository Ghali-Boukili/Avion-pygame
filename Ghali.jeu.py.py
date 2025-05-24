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
FondGris = pygame.image.load("fond_gris.png")
FondGris = pygame.transform.scale(FondGris, (800, 500))
FondStar = pygame.image.load("star.png")
FondStar = pygame.transform.scale(FondStar, (200, 200))
FondEgout = pygame.image.load("fond_0.png")
FondEgout = pygame.transform.scale(FondEgout, (800, 500))




fontDebut1 = pygame.font.SysFont("Knewave", 40)
texteDebut1 = fontDebut1.render("---> Appuyez sur 'ESPACE' pour commencer ", True, (0, 0, 0))
positionTexteDebut1 = texteDebut1.get_rect(center=(400, 220))  # centré

texteDebut2 = fontDebut1.render("---> Appuyez sur 'ENTREE' pour quitter", True, (0, 0, 0))
positionTexteDebut2 = texteDebut2.get_rect(center=(366, 270))


fontFin = pygame.font.SysFont("Arial", 100)

fontDebut3 = pygame.font.SysFont("Confortaa", 80)
texteDebut3 = fontDebut3.render("Super Plane", True, (255, 180, 0))
texteFin = fontFin.render("T'ES GUEZ", True, (255, 255, 255))
texteFin2 = fontFin.render("T'ES CHAUD TOI !", True, (255, 255, 255))
positionTexteDebut3 = texteDebut3.get_rect(center=(400, 70))
positionTexteFin = texteFin.get_rect(center=(420, 300))
positionTexteFin2 = texteFin2.get_rect(center=(400, 300))


# On définit les variables qui contiendront les positions des différents éléments (vaisseau, alien, projectile)
# Chaque position est un couple de valeur '(x,y)'

positionAvion = (728,250)
positionAvionInitiale = positionAvion
positionNuage = (0,9)

positionAlien = (200,200)

# définir le nb d'aliens et comment ils sont espacés entre eux horizontalement et verticalement 
Aliens = [(110+i*60,110+j*50)for i in range(3) for j in range(6)] # i : nb d'aliens horizontalement et j : nb d'aliens verticalement

boules = []
bombes = []
nbB = 40

Nuages = [(110+i*50,40+j*40) for i in range(6) for j in range(1)]
nouveauxNuages = (0,8)

a = 3 # vitesse des nuages
niveau= 1
score = 0
m=2 # vitesse des aliens
b = 5 # vitesse des bombes

vies = 3

arial = pygame.font.SysFont("arial",15)

Porte1 = (1,random.randint(80,400))
Porte2 = (1,Porte1[1]+60)
Porte3 = (50,Porte1[1])

rectPorte1 = pygame.Rect(Porte1[0], Porte1[1], 50, 3)
rectPorte2 = pygame.Rect(Porte2[0], Porte2[1], 50, 3)
rectPorte3 = pygame.Rect(Porte3[0], Porte1[1], 2, 62)

bruitTirAvion = pygame.mixer.Sound("bruitTirAvion.mp3") 

debutJeu = False 

def dessiner():
    global fenetre, debutJeu
    
    if not debutJeu:
        fenetre.blit(FondGris,(0,0))  # Fond gris
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
        pygame.draw.rect(fenetre, (255,255,255),rectPorte3, 10) # une porte qui s'affiche aléatoirement en mm position [0]
        
        for boule in boules:
            pygame.draw.circle(fenetre, (0,0,0), boule, 6)
        
        for bombe in bombes:
            pygame.draw.circle(fenetre, (91, 60, 17), bombe, 10)
            
        afficheBoules = arial.render("boules: "+str(nbB),True,pygame.Color(0,0,0))
        afficheScore = arial.render("vies: "+str(vies),True,pygame.Color(0,0,0))
        afficheNiveau = arial.render("niveau: "+str(niveau),True,pygame.Color(0,0,0))
        fenetre.blit(afficheScore, (730,460)) # afficher le score en bas à droite de l'ecran ainsi que le nb de boules
        fenetre.blit(afficheBoules, (730,480))
        fenetre.blit(afficheNiveau, (10,480))
        
        rectAvion =  pygame.Rect(positionAvion[0],positionAvion[1], 72, 48 )
        if rectAvion.colliderect(rectPorte3) : # SECRET DU jeu : si collision de l'avion avec la porte 3, on gagne
            fenetre.blit(texteFin2, positionTexteFin2)
            pygame.display.update()                      
            pygame.time.wait(2000)                       
            pygame.quit()                               
            sys.exit()
        if  niveau==10:
            fenetre.blit(texteFin2, positionTexteFin2)
            pygame.display.update()                      
            pygame.time.wait(2000)                       
            pygame.quit()                               
            sys.exit()
            
        if vies == 0 and positionAvion[1]>500:
            fenetre.blit(texteFin, positionTexteFin)
            pygame.display.update()                      
            pygame.time.wait(4000)                       
            pygame.quit()                               
            sys.exit()
        
            
    pygame.display.flip() # Rafraichissement complet de la fenêtre avec les dernières opérations de dessin


# Fonction en charge de gérer les évènements clavier (ou souris)
def gererClavierEtSouris():
    global positionAvion, debutJeu, continuer, nbB, boules, appui
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
        if touchesPressees[pygame.K_SPACE] == True and nbB>0 and appui == False:
            boules.append((positionAvion[0],positionAvion[1]+26))
            nbB = nbB-1
            appui=True
        if touchesPressees[pygame.K_UP] == True and positionAvion[1]>80:
            positionAvion = ( positionAvion[0] , positionAvion[1]-4)
        if touchesPressees[pygame.K_DOWN] == True and positionAvion[1]+20<452:
            positionAvion = ( positionAvion[0]  , positionAvion[1]+4)
        if touchesPressees[pygame.K_RIGHT] == True and positionAvion[0]<728 and positionAvion[0]>0 and positionAvion[1]+20<452:
            positionAvion = ( positionAvion[0] + 2 , positionAvion[1])
        #if touchesPressees[pygame.K_LEFT] == True and positionAvion[0]>0:
            positionAvion = ( positionAvion[0] , positionAvion[1]+2)
        
         
        if touchesPressees[pygame.K_SPACE] == True and nbB>0:  # bruit à chaque tire
            bruitTirAvion.play()

# On crée une nouvelle horloge qui nous permettra de fixer la vitesse de rafraichissement de notre fenêtre
clock = pygame.time.Clock()

# La boucle infinie de pygame:
# On va continuellement dessiner sur la fenêtre, gérer les évènements et calculer certains déplacements
continuer = 1
while continuer==1:
    # pygame permet de fixer la vitesse de notre boucle:
    # ici on déclare 50 tours par secondes soit une animation à 50 images par secondes
    clock.tick(50)
    if positionAvion[0] > 0 : # pour que l'avion ne sorte pas de l'écran à gauche
        positionAvion = (positionAvion[0] - 0.5, positionAvion[1])
    
    
    dessiner()
    gererClavierEtSouris()

    for i in range(len(Nuages)):
        Nuages[i] = (Nuages[i][0]+a, Nuages[i][1])
        if Nuages[i][0] > 800:
            Nuages[i] = nouveauxNuages # reviens à la position initiale 
                
    
    for i in range(len(boules)):
        boules[i]=(boules[i][0]-5,boules[i][1])
        if boules[i][0]<0:
            boules[i]=(-1,-1)
        
    for i in range(len(bombes)):
        bombes[i] = (bombes[i][0] + b, bombes[i][1])
        if bombes[i][0] > 800:
            bombes[i] = (-1, -1)
    
    t =3
    if random.randint(0,100)<t: # 3 tires au début
        proba=random.randint(0,len(Aliens)-1)
        bombes.append((Aliens[proba][0]+16,Aliens[proba][1]+30)) 
        if len(Aliens)==0:
            t+=1 
        
    for positionBoule in boules:
        rectBoule = pygame.Rect(positionBoule[0], positionBoule[1], 6, 6)

    for i in range(len(bombes)):
        rectBombe = pygame.Rect(bombes[i][0], bombes[i][1], 8, 8)  
 
    rectAvion =  pygame.Rect(positionAvion[0],positionAvion[1], 72, 48 )

    for positionAlien in Aliens :
        rectAlien = pygame.Rect(positionAlien[0], positionAlien[1], 45,40)

    for positionNuage in Nuages:
        rectNuage = pygame.Rect(Porte3[0], Porte1[1], 75,70)
    
    
    # Gestion des collisions avec les aliens
    for positionAlien in Aliens:
        rectAlien = pygame.Rect(positionAlien[0], positionAlien[1], 45, 40)
        if rectAvion.colliderect(rectAlien):
            imageAvion = imageAvionPerdu
             # fait tomber l'avion 
            while positionAvion[1] < 500:
                positionAvion = (positionAvion[0], positionAvion[1] + 4)
                dessiner()
                clock.tick(50)
            continuer = 0  # fin du jeu
    
    for positionAlien in Aliens[:]:  # On parcourt une copie
        rectAlien = pygame.Rect(positionAlien[0], positionAlien[1], 45, 40)
        for positionBoule in boules[:]:  # Pareil pour les boules
            rectBoule = pygame.Rect(positionBoule[0], positionBoule[1], 6, 6)
            if rectBoule.colliderect(rectAlien):
                Aliens.remove(positionAlien)  # Supprime l'alien
                boules.remove(positionBoule)  # Supprime la boule
                break  # On arrête la boucle pour cette boule
      
    for positionBombe in bombes[:]:  
        rectBombe = pygame.Rect(positionBombe[0], positionBombe[1], 10, 10)
        if rectBombe.colliderect(rectAvion):
            bombes.remove(positionBombe)
            vies = vies - 1
            if vies == 0:
                imageAvion = imageAvionPerdu
                while positionAvion[1] < 500:
                    positionAvion = (positionAvion[0], positionAvion[1] + 4)
                    dessiner()
                    clock.tick(50)
                continuer = 0  
                
            # fait tomber l'avion

    # On vérifie si on doit inverser la direction des aliens avant qu'ils rebougent
    for alien in Aliens:
        if alien[1] + m >= 450 or alien[1] + m <= 100:
            m = m*(-1)
            break

    # déplace tt les aliens en mm temps
    for i in range(len(Aliens)):
        if positionAvion != (-1, -1):
            Aliens[i] = (Aliens[i][0], Aliens[i][1] + m)
            
    # effacer              
    while (-1,-1) in boules:
        boules.remove((-1,-1))
    
    while (-1,-1) in bombes:
        bombes.remove((-1,-1))
    
    while (-1,-1) in Aliens:
        Aliens.remove((-1,-1))
    
    if len(Aliens) == 0:
        if niveau <= 10:
            niveau += 1
            bombes[i] = (bombes[i][0] + b, bombes[i][1])
            m +=2
            b +=1
            nbB = 40
        else:
            m = 0
        positionAvion = positionAvionInitiale
        Aliens = [(110+i*60,110+j*50) for i in range(3) for j in range(6)]
        nbB = 40
        bombes.clear()
        boules.clear()  
        continue
    
    for positionBoule in boules[:]:
        rectBoule = pygame.Rect(positionBoule[0], positionBoule[1], 6, 6)
        if rectBoule.colliderect(rectPorte3):
            vies += 1
            boules.remove(positionBoule)
            break  
    
     
## A la fin, lorsque l'on sortira de la boucle, on demandera à Pygame de quitter proprement
pygame.quit()
sys.exit()
