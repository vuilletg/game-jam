import pygame
from Player import player
from sol import sol
import sys

class jeu:
    def __init__(self):
        self.ecran= pygame.display.set_mode((1100,600))
        pygame.display.set_caption('nom du jeu')
        self.jeu_encours = True
        self.xJoueur, self.yJoueur = 200,300
        self.tailleJoueur = [32,64]
        self.vitesseJoueurX=0
        self.player = player(self.xJoueur,self.yJoueur,self.tailleJoueur)
        self.sol = sol()
        self.gravite = (0,10)
        self.resistance = (0,0)
        self.rect = pygame.Rect(0,0, 1100, 600)
        self.colision =False
        self.horloge = pygame.time.Clock()
        self.fps= 60
    
    def Boucle_principale (self):
        while self.jeu_encours:
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    sys.exit()
                if event.type== pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.vitesseJoueurX = 10
                    if event.key == pygame.K_LEFT:
                        self.vitesseJoueurX = -10
                    if event.key == pygame.K_SPACE:
                        self.player.aSauter= True
                        self.player.nbsaut+=1
                if event.type== pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.vitesseJoueurX = 0
                    if event.key == pygame.K_LEFT:
                        self.vitesseJoueurX = 0

            if self.sol.rect.colliderect(self.player.rect):
                self.resistance = (0, -10)
                self.colision = True
                self.player.nbsaut=0
            else:
                self.resistance = (0, 0)

            if self.colision and self.player.aSauter and self.player.nbsaut<1:
                self.player.sauter()
            self.player.move(self.vitesseJoueurX)
            self.gravite_jeu()
            self.player.rect.clamp_ip(self.rect)
            self.ecran.fill((0,0,0))
            self.player.afficher(self.ecran)
            self.sol.afficher(self.ecran)
            pygame.draw.rect(self.ecran,(255,255,255),self.rect,1)
            self.horloge.tick(self.fps)
            pygame.display.flip()
    
    def gravite_jeu(self):
        self.player.rect.y +=self.gravite[1] + self.resistance[1]


if __name__=='__main__':
    pygame.init()
    jeu().Boucle_principale()
    pygame.quit()