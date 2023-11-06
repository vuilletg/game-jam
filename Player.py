import pygame

class player(pygame.sprite.Sprite):

    def __init__(self,x,y, taille):
      super().__init__()
      self.x = x
      self.y = y
      self.taille = taille
      self.rect = pygame.Rect(self.x, self.y, self.taille[0], self.taille[1])
      self.aSauter=False
      self.saut =0
      self.saut_monte=0
      self.saut_decente=10
      self.nbsaut=0


    def move(self, vitesse):
       self.rect.x += vitesse
    
    def afficher(self, surface):
       pygame.draw.rect(surface, (255,255,255), self.rect)

    def sauter(self):
        if self.aSauter:
            if self.saut_monte>=10:
                self.saut_decente-=1
                self.saut = self.saut_decente
            else:
                self.saut_monte+=1
                self.saut = self.saut_monte

            if self.saut_decente<0:
                self.saut_monte = 0
                self.saut_decente = 5
                self.aSauter = False

        self.rect.y= self.rect.y - (10 *(self.saut/2))