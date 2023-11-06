import pygame
from Player import player
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
    
    def Boucle_principale (self):
        while self.jeu_encours:
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    sys.exit()
                if event.type== pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.vitesseJoueurX = 1
                    if event.key == pygame.K_LEFT:
                        self.vitesseJoueurX = -1
                if event.type== pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.vitesseJoueurX = 0
                    if event.key == pygame.K_LEFT:
                        self.vitesseJoueurX = 0

            self.player.move(self.vitesseJoueurX)
            self.ecran.fill((0,0,0))
            self.player.afficher(self.ecran)
            pygame.display.flip()


if __name__=='__main__':
    pygame.init()
    jeu().Boucle_principale()
    pygame.quit()