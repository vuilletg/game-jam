import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x,y,taille,joueur):
        super().__init__()
        self.joueur=joueur
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
        self.etat = "idle"
        self.vitesseJoueurX = 0
        if self.joueur:
            self.idle = [pygame.image.load(f"./ASSET/mc/Idle ({i}).png") for i in range(1, 6)]
            self.dead = [pygame.image.load(f"./ASSET/mc/Dead ({i}).png") for i in range(1, 6)]
            self.run = [pygame.image.load(f"./ASSET/mc/Run ({i}).png") for i in range(1, 6)]
        self.animation_index = 10
        self.direction = "droite"
        if self.joueur:
            self.sprite = self.idle[0]
        else:
            self.sprite=pygame.Surface((taille[0],taille[1]))
            self.sprite.fill((255,0,0))
        self.animation_speed = 5  # pour la vitesse de l'animation
        self.frame_counter = 0

        self.deplacement_enemi = 0
        self.vitesse_enmei = 2
        self.screen_width=1024
        self.screen_height=768

    def move(self, vitesse):
        self.rect.x += vitesse
        if vitesse > 0:
            self.direction = "droite"
        elif vitesse < 0:
            self.direction = "gauche"
        screen_scroll=0
        if self.rect.right> self.screen_width - 200 or self.rect.left<200:
            self.rect.x-=vitesse
            screen_scroll=-vitesse
        return screen_scroll

    def afficher(self, surface):
        if self.joueur:
            self.frame_counter += 1
            if self.frame_counter >= self.animation_speed:
                self.frame_counter = 0
                self.animation_index = (self.animation_index + 1) % 5
                if self.estMort:
                    # Animation quand le joueur est mort
                    self.sprite = self.dead[self.animation_index]
                elif self.vitesseJoueurX != 0:
                    # Animation quand le joueur court
                    self.sprite = self.run[self.animation_index]
                    if self.direction == "gauche":
                        self.sprite = pygame.transform.flip(self.sprite, True, False)
                else:
                    # Animation quand le joueur est immobile
                    self.sprite = self.idle[self.animation_index]
        surface.blit(self.sprite, self.rect.topleft)


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
                self.saut_decente = 7
                self.aSauter = False

        self.rect.y= self.rect.y -(6*(self.saut/1.5))

    def movementenemie(self):
        if self.deplacement_enemi < -100 or self.deplacement_enemi > 100:
            self.vitesse_enmei *= -1
        self.rect.x += self.vitesse_enmei
        self.deplacement_enemi += self.vitesse_enmei

    def __del__(self):
        print("destruction du joueur")