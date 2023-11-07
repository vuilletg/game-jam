import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, taille):
        super().__init__()
        self.x = x
        self.y = y
        self.taille = taille
        self.rect = pygame.Rect(self.x, self.y, self.taille[0], self.taille[1])
        self.aSauter = False
        self.saut = 0
        self.saut_monte = 0
        self.saut_decente = 7
        self.nbsaut = 0
        self.resistance = (0, 0)
        self.colision = False
        self.estMort = False
        self.deplacement_enemi = 0
        self.vitesse_enmei = 2

    def move(self, vitesse):
        self.rect.x += vitesse
    
    def afficher(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)

    def sauter(self):
        if self.aSauter:
            if self.saut_monte >= 10:
                self.saut_decente -= 1
                self.saut = self.saut_decente
            else:
                self.saut_monte += 1
                self.saut = self.saut_monte

            if self.saut_decente < 0:
                self.saut_monte = 0
                self.saut_decente = 7
                self.aSauter = False

        self.rect.y = self.rect.y - (7*(self.saut/1.5))

    def movementenemi(self):
        if self.deplacement_enemi < -100 or self.deplacement_enemi > 100:
            self.vitesse_enmei *= -1
        self.rect.x += self.vitesse_enmei
        self.deplacement_enemi += self.vitesse_enmei

    def __del__(self):
        print("destruction du joueur")
