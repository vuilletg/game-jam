import pygame
import pytmx
import pyscroll
from player import Player
from ennemi import Ennemi
import sys

class Jeu:
    # Declaration des variables
    scene="menu"
    def __init__(self):
        self.ecran= pygame.display.set_mode((1024,768))
        pygame.display.set_caption('nom du jeu')
        self.jeu_encours = True
        self.menu()



    def start(self):
        self.xJoueur, self.yJoueur = 200, 650
        self.tailleJoueur = [32,32]
        self.vitesseJoueurX=0
        self.player = Player(self.xJoueur,self.yJoueur, self.tailleJoueur)
        self.enemie = Ennemi(self.xJoueur+200,self.yJoueur, self.tailleJoueur)
        self.sol = pygame.Rect(0, 704, 1024, 64)
        self.murg = pygame.Rect(0, 0, 32, 768)
        self.murd = pygame.Rect(998, 0, 32, 768)
        self.plafond = pygame.Rect(0, 0, 1024, 64)

        self.plateformes = []
        plateforme1 = pygame.Rect(320, 640, 240, 64)
        plateforme2 = pygame.Rect(624, 516, 192, 96)
        self.plateformes.append(plateforme1)
        self.plateformes.append(plateforme2)

        self.gravite = (0,10)
        self.resistance = (0,0)
        self.rect = pygame.Rect(0,0, 1024, 768)
        self.colision = False
        self.horloge = pygame.time.Clock()
        self.fps = 60




        # pcharger la carte tiled

    def menu(self):
        self.ecran.fill((0,0,0))
        font= pygame.font.Font(None,125)
        text= pygame.font.Font(None,50)
        titre=font.render("Nom du jeu",True,(0,0,0))
        bouton1=text.render("Nouvelle partie", True,(0,0,0))
        bouton2=text.render("Crédits", True,(0,0,0))
        surf1 = pygame.Surface((700,100))
        surf1.fill((255,255,255))
        button1=surf1.get_rect()
        self.ecran.blit(surf1,(162,75))
        self.ecran.blit(titre,(512-font.size("Nom du jeu")[0]/2,125-font.size("Nom du jeu")[1]/2))
        surf2 = pygame.Surface((300,75))
        surf2.fill((255,255,255))
        button2=surf2.get_rect()
        self.ecran.blit(surf2,(362,350))
        self.ecran.blit(bouton1,(512-text.size("Nouvelle partie")[0]/2,387-text.size("Nouvelle partie")[1]/2))
        surf3 = pygame.Surface((300,75))
        surf3.fill((255,255,255))
        button3=surf3.get_rect()
        self.ecran.blit(surf3,(362,550))
        self.ecran.blit(bouton2,(512-text.size("Crédits")[0]/2,587-text.size("Crédits")[1]/2))
        tmx_data = pytmx.util_pygame.load_pygame('Egout.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.ecran.get_size())
        self.groupeCalques = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        pygame.display.flip()

    def credits(self):
        self.ecran.fill((0,0,0))
        font= pygame.font.Font(None,125)
        text= pygame.font.Font(None,50)
        titre=font.render("Nom du jeu",True,(0,0,0))
        bouton1=text.render("Nouvelle partie", True,(0,0,0))
        bouton2=text.render("Crédits", True,(0,0,0))
        surf1 = pygame.Surface((600,100))
        surf1.fill((255,255,255))
        button1=surf1.get_rect()
        self.ecran.blit(surf1,(162,75))
        self.ecran.blit(titre,(512-font.size("Nom du jeu")[0]/2,125-font.size("Nom du jeu")[1]/2))
        surf2 = pygame.Surface((300,75))
        surf2.fill((255,255,255))
        button2=surf2.get_rect()
        self.ecran.blit(surf2,(362,350))
        self.ecran.blit(bouton1,(512-text.size("Nouvelle partie")[0]/2,387-text.size("Nouvelle partie")[1]/2))
        surf3 = pygame.Surface((300,75))
        surf3.fill((255,255,255))
        button3=surf3.get_rect()
        self.ecran.blit(surf3,(362,550))
        self.ecran.blit(bouton2,(512-text.size("Crédits")[0]/2,587-text.size("Crédits")[1]/2))
        pygame.display.flip()
        tmx_data = pytmx.util_pygame.load_pygame('Egout.tmx')

    def gameover(self):
        self.ecran.fill((0,0,0))
        font= pygame.font.Font(None,125)
        text= pygame.font.Font(None,50)
        titre=font.render("Game over",True,(0,0,0))
        bouton1=text.render("Réessayer", True,(0,0,0))
        bouton2=text.render("Menu principal", True,(0,0,0))
        surf1 = pygame.Surface((700,100))
        surf1.fill((255,255,255))
        button1=surf1.get_rect()
        self.ecran.blit(surf1,(162,75))
        self.ecran.blit(titre,(512-font.size("Game over")[0]/2,125-font.size("Game over")[1]/2))
        surf2 = pygame.Surface((300,75))
        surf2.fill((255,255,255))
        button2=surf2.get_rect()
        self.ecran.blit(surf2,(362,350))
        self.ecran.blit(bouton1,(512-text.size("Réessayer")[0]/2,387-text.size("Réessayer")[1]/2))
        surf3 = pygame.Surface((300,75))
        surf3.fill((255,255,255))
        button3=surf3.get_rect()
        self.ecran.blit(surf3,(362,550))
        self.ecran.blit(bouton2,(512-text.size("Menu principal")[0]/2,587-text.size("Menu principal")[1]/2))
        pygame.display.flip()


    def Boucle_principale (self):
        while self.jeu_encours:
            self.groupeCalques.update()
            self.groupeCalques.draw(self.ecran)  # afficher les calques de tiled
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN and self.scene=="menu":
                    if pygame.mouse.get_pos()[0]>362 and pygame.mouse.get_pos()[0]<662 and pygame.mouse.get_pos()[1]>350 and pygame.mouse.get_pos()[1]<425:
                        self.scene="jeu"
                        self.start()
                    if pygame.mouse.get_pos()[0]>362 and pygame.mouse.get_pos()[0]<662 and pygame.mouse.get_pos()[1]>550 and pygame.mouse.get_pos()[1]<625:
                        self.scene="credits"
                        self.credits()
                if event.type==pygame.MOUSEBUTTONDOWN and self.scene=="game over":
                    if pygame.mouse.get_pos()[0]>362 and pygame.mouse.get_pos()[0]<662 and pygame.mouse.get_pos()[1]>350 and pygame.mouse.get_pos()[1]<425:
                        self.scene="jeu"
                        self.start()
                    if pygame.mouse.get_pos()[0]>362 and pygame.mouse.get_pos()[0]<662 and pygame.mouse.get_pos()[1]>550 and pygame.mouse.get_pos()[1]<625:
                        self.scene="menu"
                        self.menu()

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

                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_UP:
                        self.jeu_encours = False

                # evenements quand une touche est relacher
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.vitesseJoueurX = 0
                    if event.key == pygame.K_LEFT:
                        self.vitesseJoueurX = 0

            if self.scene=="jeu":
                # Gestion des colisions
                self.detection_collisions(self.player)
                self.detection_collisions(self.enemie)

                # fonction d'appel du saut sous condtions
                if self.player.colision and self.player.aSauter and self.player.nbsaut<2:
                    self.player.sauter()

                # Appels des fonctions
                self.player.move(self.vitesseJoueurX)
                self.gravite_jeu()
                self.player.rect.clamp_ip(self.rect)

                self.player.afficher(self.ecran,(255,255,255))
                self.enemie.movement()
                self.enemie.afficher(self.ecran, (255,0,0))
                # pygame.draw.rect(self.ecran, (255,255,255), self.sol)

                # pygame.draw.rect(self.ecran,(255,255,255),self.rect,1)

                self.horloge.tick(self.fps)
                if self.player.rect.colliderect(self.enemie.rect):
                    print("game over")
                    self.player.estMort = True
                    del self.player
                    del self.enemie
                    self.scene="game over"
                    self.gameover()
                pygame.display.flip()

    #gestion de la gravité
    def gravite_jeu(self):
        self.player.rect.y +=self.gravite[1] + self.player.resistance[1]
        self.enemie.rect.y +=self.gravite[1] + self.enemie.resistance[1]


    def detection_collisions(self, entite):
        if self.sol.colliderect(entite.rect):
            entite.resistance = (0, -10)
            entite.colision = True
            entite.nbsaut = 0
        else:
            entite.resistance = (0, 0)

        # colisions avec les murs
        if self.murg.colliderect(entite.rect):
            self.player.rect.x = entite.right
        if self.murd.colliderect(entite.rect):
            entite.rect.x = self.murd.left - entite.rect.width

           # collisions avec les plateformes du niveau
        for plateforme in self.plateformes:
            if entite.rect.colliderect(plateforme):
                distancemin = min(abs(entite.rect.bottom - plateforme.top),
                                  abs(entite.rect.top - plateforme.bottom),
                                  abs(entite.rect.right - plateforme.left),
                                  abs(entite.rect.left - plateforme.right))

                if distancemin == abs(entite.rect.bottom - plateforme.top):
                    entite.colision = True  # pour reset le(s) saut
                    entite.nbsaut = 0
                    entite.rect.y = plateforme.top - self.player.rect.height

                elif distancemin == abs(entite.rect.top - plateforme.bottom):
                    entite.rect.y = plateforme.bottom

                elif distancemin == abs(entite.rect.right - plateforme.left):
                    entite.rect.x = plateforme.left - self.player.rect.width

                elif distancemin == abs(entite.rect.left - plateforme.right):
                    entite.rect.x = plateforme.right


if __name__=='__main__':
    pygame.init()
    Jeu().Boucle_principale()
    pygame.quit()