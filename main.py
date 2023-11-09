import pygame
import time
from player import Player
from ennemi import Ennemi
from camera import Camera
import TiledMap
import sys

class Jeu:
    # Declaration des variables
    screen_scroll=0
    vitesse_scroll=0
    scene="menu"
    niveau=""
    appui=False
    niveau=""
    beat=0
    jacouille=False

    def __init__(self):
        self.screen_width=1024
        self.screen_height=768
        self.ecran= pygame.display.set_mode((self.screen_width,self.screen_height))
        pygame.display.set_caption('Jacques et les digietres')
        self.jeu_encours = True
        self.world_height = 0
        self.world_height = 0

        self.menu()

    def cinématique(self, images_cinématique):

        clock = pygame.time.Clock()
        frame = 0
        playing = True

        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        frame += 1
                        if frame >= len(images_cinématique):
                            playing = False

            if frame < len(images_cinématique):
                self.ecran.fill((0, 0, 0))
                self.ecran.blit(images_cinématique[frame], (0, 0))
                pygame.display.flip()


    def tuto(self):
        images_cinématique_tuto = [
            pygame.image.load("./ASSET/Cinematique/1.jpg"),
            pygame.image.load("./ASSET/Cinematique/2.jpg"),
            pygame.image.load("./ASSET/Cinematique/3.jpg"),
            pygame.image.load("./ASSET/Cinematique/4.jpg"),
        ]

        self.cinématique(images_cinématique_tuto)
        self.test=TiledMap.TiledMap("map/Tuto/tuto.tmx")
        self.test.scroll(self.ecran,self.screen_scroll)
##        pygame.mixer.music.load("Musique_tuto.mp3")
##        pygame.mixer.music.play(-1)
        self.xJoueur, self.yJoueur = 200, 650
        self.tailleJoueur = [55, 110]
        self.player = Player(self.xJoueur,self.yJoueur, self.tailleJoueur,True)
        self.player.vitesseJoueurX = 0

        self.enemie = Player(self.xJoueur+200,self.yJoueur+55, [55,64],False)

        sol1 = pygame.Rect(0, 704, 2944, 64)
        sol2 = pygame.Rect(3136, 704, 320, 64)
        sol3 = pygame.Rect(3648, 704, 512, 64)
        plateforme1 = pygame.Rect(1088, 640, 1408, 64)
        plateforme2 = pygame.Rect(1152, 576, 1280, 64)
        plateforme3 = pygame.Rect(1216, 512, 1152, 64)
        plateforme4 = pygame.Rect(1280, 448, 1024, 64)
        plateforme5 = pygame.Rect(1344, 384, 896, 64)
        portail=pygame.Rect(4132,640,64,128)
        self.plateformes = []
        self.plateformes.append(sol1)
        self.plateformes.append(sol2)
        self.plateformes.append(sol3)
        self.plateformes.append(plateforme1)
        self.plateformes.append(plateforme2)
        self.plateformes.append(plateforme3)
        self.plateformes.append(plateforme4)
        self.plateformes.append(plateforme5)
        self.plateformes.append(portail)
        self.gravite = (0,10)
        self.resistance = (0,0)
        self.rect = pygame.Rect(0,0, 1024, 768)
        self.colision = False
        self.horloge = pygame.time.Clock()
        self.fps = 60
        self.sound_d=pygame.mixer.Sound("381688__stumpbutt__retro-death-sfx.wav")
        self.sound_w=pygame.mixer.Sound("515783__matrixxx__retro-footstep.wav")
        self.sound_j=pygame.mixer.Sound("458641__matrixxx__retro-jump-02.wav")
        self.sound_j.set_volume(0.1)

    def niveau1(self):
        self.test=TiledMap.TiledMap("map/Niveau 1/niveau1.tmx")
        self.test.scroll(self.ecran,self.screen_scroll)
##        pygame.mixer.music.load("Musique_tuto.mp3")
##        pygame.mixer.music.play(-1)
        self.xJoueur, self.yJoueur = 200, 650
        self.tailleJoueur = [55, 110]
        self.player = Player(self.xJoueur,self.yJoueur, self.tailleJoueur,True)
        self.player.vitesseJoueurX = 0

        self.enemie = Player(self.xJoueur+200,self.yJoueur+55, [55,64],False)

        # taile niveau 1 : 6400 x 768
        murg_lvl1 = pygame.Rect(0, 0, 64, 768)

        sol1_lvl1 = pygame.Rect(0, 704, 1600, 64)
        plateforme1_partie1_lvl1 = pygame.Rect(192, 448, 640, 10)
        plateforme2_partie1_lvl1 = pygame.Rect(768, 576, 448, 10)
        plateforme3_partie1_lvl1 = pygame.Rect(832, 384, 192, 10)
        plateforme1_1er_esca_lvl1 = pygame.Rect(1152, 576, 64, 128)
        plateforme2_1er_esca_lvl1 = pygame.Rect(1216, 640, 64, 64)

        sol2_lvl1 = pygame.Rect(1728, 704, 384, 64)

        sol3_lvl1 = pygame.Rect(2304, 704, 768, 64)
        plateforme1_partie3_lvl1 = pygame.Rect(2432, 576, 192, 10)
        plateforme2_partie3_lvl1 = pygame.Rect(2624, 512, 128, 10)
        plateforme3_partie3_lvl1 = pygame.Rect(2752, 576, 192, 10)

        plateforme1_esca2_lvl1 = pygame.Rect(3264, 704, 64, 64)
        plateforme2_esca2_lvl1 = pygame.Rect(3328, 640, 64, 128)
        plateforme3_esca2_lvl1 = pygame.Rect(3392, 576, 64, 192)
        plateforme4_esca2_lvl1 = pygame.Rect(3456, 512, 64, 256)
        plateforme5_esca2_lvl1 = pygame.Rect(3520, 448, 64, 320)
        plateforme6_esca2_lvl1 = pygame.Rect(3584, 384, 64, 384)

        plateforme1_esca3_lvl1 = pygame.Rect(3840, 384, 64, 384)
        plateforme2_esca3_lvl1 = pygame.Rect(3904, 448, 64, 320)
        plateforme3_esca3_lvl1 = pygame.Rect(3968, 512, 64, 256)
        plateforme4_esca3_lvl1 = pygame.Rect(4032, 576, 64, 192)
        plateforme5_esca3_lvl1 = pygame.Rect(4096, 640, 64, 128)
        plateforme6_esca3_lvl1 = pygame.Rect(4160, 704, 64, 64)

        self.plateformes = []

        self.plateformes.append(murg_lvl1)

        self.plateformes.append(sol1_lvl1)
        self.plateformes.append(plateforme1_partie1_lvl1)
        self.plateformes.append(plateforme2_partie1_lvl1)
        self.plateformes.append(plateforme3_partie1_lvl1)
        self.plateformes.append(plateforme1_1er_esca_lvl1)
        self.plateformes.append(plateforme2_1er_esca_lvl1)

        self.plateformes.append(sol2_lvl1)

        self.plateformes.append(sol3_lvl1)
        self.plateformes.append(plateforme1_partie3_lvl1)
        self.plateformes.append(plateforme2_partie3_lvl1)
        self.plateformes.append(plateforme3_partie3_lvl1)

        self.plateformes.append(plateforme1_esca2_lvl1)
        self.plateformes.append(plateforme2_esca2_lvl1)
        self.plateformes.append(plateforme3_esca2_lvl1)
        self.plateformes.append(plateforme4_esca2_lvl1)
        self.plateformes.append(plateforme5_esca2_lvl1)
        self.plateformes.append(plateforme6_esca2_lvl1)

        self.plateformes.append(plateforme1_esca3_lvl1)
        self.plateformes.append(plateforme2_esca3_lvl1)
        self.plateformes.append(plateforme3_esca3_lvl1)
        self.plateformes.append(plateforme4_esca3_lvl1)
        self.plateformes.append(plateforme5_esca3_lvl1)
        self.plateformes.append(plateforme6_esca3_lvl1)

        self.gravite = (0,10)
        self.resistance = (0,0)
        self.rect = pygame.Rect(0,0, 1024, 768)

##    def niveau2(self):

    def menu(self):
##        pygame.mixer.music.load("Musique_menu.mp3")
##        pygame.mixer.music.play(-1)
        self.ecran.fill((0,0,0))
        font= pygame.font.Font(None,125)
        text= pygame.font.Font(None,50)
        titre=font.render("Jacques et les digietres",True,(0,0,0))
        bouton1=text.render("Nouvelle partie", True,(0,0,0))
        bouton2=text.render("Crédits", True,(0,0,0))
        surf1 = pygame.Surface((1000,100))
        surf1.fill((255,255,255))
        button1=surf1.get_rect()
        self.ecran.blit(surf1,(12,75))
        self.ecran.blit(titre,(512-font.size("Jacques et les digietres")[0]/2,125-font.size("Jacques et les digietres")[1]/2))
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

    def credits(self):
        self.ecran.fill((0, 0, 0))
        font_title = pygame.font.Font(None, 125)
        font_text = pygame.font.Font(None, 50)

        # Titre Retour
        title_retour = font_title.render("Retour", True, (255, 255, 255))
        surf_retour = pygame.Surface((200, 75))
        surf_retour.fill((0, 0, 0))
        surf_retour_rect = surf_retour.get_rect(topleft=(20, 40))
        self.ecran.blit(surf_retour, surf_retour_rect)
        self.ecran.blit(title_retour, surf_retour_rect.move(0, -15))

        # Section Crédits
        surf_credits = pygame.Surface((800, 200))
        surf_credits.fill((0, 0, 0))
        surf_credits_rect = surf_credits.get_rect(center=(self.ecran.get_width() // 2, self.ecran.get_height() // 2))
        self.ecran.blit(surf_credits, surf_credits_rect)
        title_credits = font_text.render("Crédits :", True, (255, 255, 255))
        self.ecran.blit(title_credits, surf_credits_rect.move(0, -75))

        # Colonne de gauche (Bruitages, Musiques, Cinématique)
        left_column_rect = pygame.Rect(self.ecran.get_width() - 1000, 300, 400, 200)
        pygame.draw.rect(self.ecran, (0, 0, 0), left_column_rect)

        left_credits = ["Bruitages: freesound.org", "Musiques: fesliyanstudios.com", "Cinématique: Insta - @Suhi_Stev"]
        for i, credit_text in enumerate(left_credits):
            credit_render = font_text.render(credit_text, True, (255, 255, 255))
            self.ecran.blit(credit_render, left_column_rect.move(0, i * 50))

        # Colonne de droite (Programmeurs, Level Designer)
        right_column_rect = pygame.Rect(self.ecran.get_width() - 400, 300, 400, 200)
        pygame.draw.rect(self.ecran, (0, 0, 0), right_column_rect)

        line_height = 50  # Espacement vertical entre les lignes


        right_credits = [
            "Level Designer: "
            "DASSAC Noah",
            "Programmeurs:",
            "REYMOND Romain",
            "ROUMEAS Elinaï",
            "VUILLET Gaspard"]
        for i, credit_text in enumerate(right_credits):
            credit_render = font_text.render(credit_text, True, (255, 255, 255))
            text_rect = credit_render.get_rect(midright=(right_column_rect.right - 10, right_column_rect.top + i * line_height))
            self.ecran.blit(credit_render, text_rect.topleft)

        pygame.display.flip()


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
##            self.groupeCalques.update()
##            self.groupeCalques.draw(self.ecran)  # afficher les calques de tiled
            for event in pygame.event.get():
                if self.scene == "credits":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 250 and pygame.mouse.get_pos()[1] > 50 and pygame.mouse.get_pos()[1] < 125:
                            self.scene = "menu"
                            self.menu()
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN and self.scene=="menu":
                    if pygame.mouse.get_pos()[0]>362 and pygame.mouse.get_pos()[0]<662 and pygame.mouse.get_pos()[1]>350 and pygame.mouse.get_pos()[1]<425:
                        self.tuto()
                        self.niveau="tuto"
                        self.scene="jeu"
                        pygame.mixer.music.stop()
                    if pygame.mouse.get_pos()[0]>362 and pygame.mouse.get_pos()[0]<662 and pygame.mouse.get_pos()[1]>550 and pygame.mouse.get_pos()[1]<625:
                        self.scene="credits"
                        self.credits()
                if event.type==pygame.MOUSEBUTTONDOWN and self.scene=="game over":
                    if pygame.mouse.get_pos()[0]>362 and pygame.mouse.get_pos()[0]<662 and pygame.mouse.get_pos()[1]>350 and pygame.mouse.get_pos()[1]<425:
                        self.scene="jeu"
                        pygame.mixer.music.stop()
                        self.tuto()
                    if pygame.mouse.get_pos()[0]>362 and pygame.mouse.get_pos()[0]<662 and pygame.mouse.get_pos()[1]>550 and pygame.mouse.get_pos()[1]<625:
                        self.scene="menu"
                        pygame.mixer.music.stop()
                        self.menu()
                if event.type==pygame.MOUSEBUTTONDOWN and self.scene=="credits":
                    if pygame.mouse.get_pos()[0]>50 and pygame.mouse.get_pos()[0]<250 and pygame.mouse.get_pos()[1]>50 and pygame.mouse.get_pos()[1]<125:
                        self.scene="menu"
                        self.menu()



                # evenements quand une touche est apuyer
                if self.scene=="jeu":
                    if event.type == pygame.KEYDOWN:
                        if self.player.estMort == False:
                            if event.key == pygame.K_RIGHT:
                                self.player.vitesseJoueurX = 5
                                self.player.direction =0
                                pygame.mixer.Sound.play(self.sound_w)
                                self.appui=True
                                self.tappui=time.time()
                            # Le personnage se depalace vers la gauche
                            if event.key == pygame.K_LEFT:
                                self.player.vitesseJoueurX = -5
                                self.player.direction =5
                                pygame.mixer.Sound.play(self.sound_w)
                                self.appui=True
                                self.tappui=time.time()
                            # Le joueur appui sur escace
                            if event.key == pygame.K_SPACE:
                                self.player.aSauter= True
                                self.player.nbsaut+=1
                                if self.player.nbsaut<2:
                                    pygame.mixer.Sound.play(self.sound_j)
                        # Le perssonage se deplace a droite

                        if event.key == pygame.K_ESCAPE:
                            self.jeu_encours = False

                    # evenements quand une touche est relacher
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            self.player.vitesseJoueurX = 0
                            self.player.direction =0
                            self.appui=False
                        if event.key == pygame.K_LEFT:
                            self.player.vitesseJoueurX = 0
                            self.player.direction =0
                            self.appui=False


            if self.scene=="jeu":
                self.ecran.fill((0,0,0))
                self.test.scroll(self.ecran,self.screen_scroll)

                self.player.rect.x += self.vitesse_scroll
                self.enemie.rect.x += self.vitesse_scroll

                # Mettez à jour la position des plateformes
                for plateforme in self.plateformes:
                    plateforme.x+=self.vitesse_scroll
                self.enemie.x += self.screen_scroll
                # Gestion des colisions
                self.detection_collisions(self.player)
                self.detection_collisions(self.enemie)
                # fonction d'appel du saut sous condtions
                if self.player.colision and self.player.aSauter and self.player.nbsaut<2:
                    self.player.sauter()

                if self.appui==True:
                    if time.time()-self.tappui>=0.3:
                        self.tappui=time.time()
                        pygame.mixer.Sound.play(self.sound_w)

                # Appels des fonctions
                self.vitesse_scroll=self.player.move(self.player.vitesseJoueurX)
                self.screen_scroll+=self.vitesse_scroll
                self.gravite_jeu()
                self.player.rect.clamp_ip(self.rect)
                if not self.player.colision:
                    self.player.etat = "dans_les_airs"
                elif self.player.vitesseJoueurX != 0:
                    self.player.etat = "en_cours"
                else:
                    self.player.etat = "immobile"
                self.ecran.fill((0,0,0))
                self.test.scroll(self.ecran,self.screen_scroll)
                self.player.afficher(self.ecran)
                self.enemie.movementenemie()
                self.enemie.afficher(self.ecran)
                # pygame.draw.rect(self.ecran, (255,255,255), self.sol)

                # pygame.draw.rect(self.ecran,(255,255,255),self.rect,1)

                self.horloge.tick(self.fps)
                if self.player.rect.colliderect(self.enemie.rect):
                    print("game over")
                    self.screen_scroll=0
                    self.vitesse_scroll=0
                    self.jacouille=False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(self.sound_d)
                    self.player.estMort = True
                    del self.player
                    del self.enemie
                    self.scene="game over"
                    self.gameover()
                self.beat+=1
                pygame.display.flip()
                if self.niveau=="tuto":
                    if self.player.rect.colliderect(self.plateformes[8]):
                        del self.player
                        del self.enemie
                        self.screen_scroll=0
                        self.vitesse_scroll=0
                        self.niveau="niveau 1"
                        self.niveau1()
                if self.niveau=="niveau 1":
                    if self.beat >= 240:
                        self.beat=0
                        if self.jacouille:
                            self.jacouille = False
                            self.test.scroll(self.ecran, self.screen_scroll)
                        else:
                            self.jacouille = True
                    if self.jacouille:
                        self.ecran.fill((0,0,0))

    #gestion de la gravité
    def gravite_jeu(self):
        self.player.rect.y +=self.gravite[1] + self.player.resistance[1]
        self.enemie.rect.y +=self.gravite[1] + self.enemie.resistance[1]


    def detection_collisions(self, entite):
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