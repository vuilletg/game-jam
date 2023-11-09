import pygame

class Ennemi (pygame.sprite.Sprite):

    def __init__(self,x,y, taille):
        self.x = x
        self.y = y
        self.taille = taille
        self.rect = pygame.Rect(self.x, self.y, self.taille[0], self.taille[1])
        self.deplacement_enemi=0
        self.vitesse_enmei=2
        self.colision = False

    def movement(self):
        if self.deplacement_enemi <-100 or self.deplacement_enemi >100:
            self.vitesse_enmei*=-1
        self.rect.x +=self.vitesse_enmei
        self.deplacement_enemi +=self.vitesse_enmei
    def afficher(self, surface, color):
       pygame.draw.rect(surface, color, self.rect)