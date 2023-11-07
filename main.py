import pygame
import pytmx
import pyscroll
from player import Player
import sys

class Jeu:
    # Declaration des variables
    def __init__(self):
        self.ecran= pygame.display.set_mode((1024,768))
        pygame.display.set_caption('nom du jeu')
        self.jeu_encours = True
        self.xJoueur, self.yJoueur = 200,10
        self.tailleJoueur = [32,64]
        self.vitesseJoueurX=0
        self.player = Player(self.xJoueur,self.yJoueur, self.tailleJoueur)

        self.enemie = Player(self.xJoueur+200,self.yJoueur, self.tailleJoueur)
        self.sol = pygame.Rect(0, 704, 1024, 64)

        self.gravite = (0,10)
        self.resistance = (0,0)
        self.rect = pygame.Rect(0,0, 1024, 768)
        self.colision = False
        self.horloge = pygame.time.Clock()
        self.fps = 60


        # pcharger la carte tiled
        tmx_data = pytmx.util_pygame.load_pygame('test.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.ecran.get_size())

        self.groupeCalques = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)


    def Boucle_principale (self):
        while self.jeu_encours:
            self.groupeCalques.update()
            self.groupeCalques.draw(self.ecran)  # afficher les calques de tiled
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # evenements quand une touche est apuyer
                if event.type == pygame.KEYDOWN:
                    if self.player.estMort == False:                    
                        if event.key == pygame.K_RIGHT:
                            self.vitesseJoueurX = 5
                        # Le personnage se depalace vers la gauche 
                        if event.key == pygame.K_LEFT:
                            self.vitesseJoueurX = -5
                        # Le joueur appui sur escace
                        if event.key == pygame.K_SPACE:
                            self.player.aSauter= True
                            self.player.nbsaut+=1
                    # Le perssonage se deplace a droite

                    if event.key == pygame.K_ESCAPE:
                        self.jeu_encours = False

                # evenements quand une touche est relacher
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.vitesseJoueurX = 0
                    if event.key == pygame.K_LEFT:
                        self.vitesseJoueurX = 0


            # Gestion des colisions
            if self.sol.colliderect(self.player.rect):
                self.player.resistance = (0, -10)
                self.player.colision = True
                self.player.nbsaut=0
            else:
                self.player.resistance = (0, 0)
            if self.sol.colliderect(self.enemie.rect):
                self.enemie.resistance = (0, -10)
                self.enemie.colision = True
                self.enemie.nbsaut=0
            else:
                self.enemie.resistance = (0, 0)
            if self.player.rect.colliderect(self.enemie.rect):
                print("game over")
                self.player.estMort = True
                self.vitesseJoueurX = 0
                sys.exit() 
         
            # fonction d'appel du saut sous condtions
            if self.player.colision and self.player.aSauter and self.player.nbsaut<1:
                self.player.sauter()
            
            # Appels des fonctions
            self.player.move(self.vitesseJoueurX)
            self.gravite_jeu()
            self.player.rect.clamp_ip(self.rect)

            self.player.afficher(self.ecran,(255,255,255))
            self.enemie.movementenemi(        )
            self.enemie.afficher(self.ecran, (255,0,0))
            # pygame.draw.rect(self.ecran, (255,255,255), self.sol)

            # pygame.draw.rect(self.ecran,(255,255,255),self.rect,1)

            self.horloge.tick(self.fps)
            pygame.display.flip()
    
    #gestion de la gravité 
    def gravite_jeu(self):
        self.player.rect.y +=self.gravite[1] + self.player.resistance[1]
        self.enemie.rect.y +=self.gravite[1] + self.enemie.resistance[1]

if __name__=='__main__':
    pygame.init()
    Jeu().Boucle_principale()
    pygame.quit()