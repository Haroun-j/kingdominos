#------------------IMPORTS------------------------
import pygame as pg ,sys
from pygame.locals import *
from random import randint
import pygame_menu
from button import Button
from params import Params # importer la classe Params
from dominos_liste import RL,ld_img # deux listes l'une contient les dominos en lettres et l'autre contient les meme en images

print(RL)
'''une liste 24 dominos (2 joueurs) générés aléatoirement
à partir de la liste de base dans la classe "Params"  '''

liste_choix=[]
''' une liste utilisé dans la fonction "choix_domino()" dans laquelle
on va enregistrer l'indice du domino choisie [0..3] '''

pos=0


ecran = None  # pour l'affichage, initialisé après

class Ecran:
    def __init__(self,bg_img, dim_x, dim_y, titre):
        self.cursor = (0,0)  # la position d'écriture (écraser avec la position voulue)
        self.taille_fonte_y = 15  # petite taille permet l'affichage sous replit.com
        pg.init()
        if not pg.font.get_init():
            print("Désolé, les fontes de caractères sont absentes, je ne peux démarrer")
            quit()
        self.font = pg.font.SysFont("Courrier, Monospace",
                                    self.taille_fonte_y)
        self.taille_fonte_x = self.font.size('A')[0]
        self.ecran = pg.display.set_mode((dim_x,                  #taille d'écran 1280*720
                                          dim_y))
        self.bg_img = pg.transform.scale(bg_img,(dim_x,         # changer la taille de l'image de l'arrière plan 
                                          dim_y))
        
    def write(self, texte, fgcolor=(255,255,255), bgcolor=(0,0,0)):
        if texte == '        ' :
            bgcolor = (100, 100, 100)
        if texte == 'R1' :
            bgcolor = (127, 0, 255)
        elif texte == 'R2' :
            bgcolor = (255, 0, 127)
        texte = self.font.render(texte,
                            True,
                            pg.Color(fgcolor),
                            pg.Color(bgcolor))
        self.ecran.blit(texte,
                        (self.cursor[0]*self.taille_fonte_x,
                         self.cursor[1]*self.taille_fonte_y))
        pg.display.flip()
        
        
    '''Menu ----------------------------------------------------------------
        ---------------------------------------------------------------------'''
    
    
    def get_font(self,size):                        # retourner le font utilisé dans les boutons
        return pg.font.Font("assets/font.ttf", size)
    
    
    def play(self):
        #terrains = preparer_terrains()    # on n'a pas utiliser numpy et on a choisit de dessiner
                                          #les terrains directement (expliqué dans le rapport)
        while True:
            PLAY_MOUSE_POS = pg.mouse.get_pos()
            
            self.ecran.fill((100, 100, 100))           # l'arrière plan du jeu devient gris
            
            PLAY_BACK = Button(image=None, pos=(90, 50), 
                                text_input="BACK", font=self.get_font(30), base_color="White", hovering_color="Green")
            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(self.ecran)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.main_display_menu()
                        
            print('le jeu commence !!')        
            dessiner_terrains(self.ecran)               #dessiner les terrains 
            dessiner_tirage(self,680,450,pos)            #dessiner les 4 premiers dominos de la liste
            dessiner_curs(self,70.8,34.3)                 # dessiner le curseur à la position (70.8,34.3)
        
            
    def options(self):                            # option du jeu pour controler le volume et le gaphique 
        while True:
            OPTIONS_MOUSE_POS = pg.mouse.get_pos()
            self.ecran.fill("white")
            
            OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=self.get_font(30), base_color="Black", hovering_color="Green")
            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.ecran)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.main_display_menu()
            pg.display.update()
            
    def main_display_menu(self):              # associer les fonctions play,option et quitter à leurs boutons  
        while True:
            self.ecran.blit(self.bg_img, (0, 0))

            MENU_MOUSE_POS = pg.mouse.get_pos()

            PLAY_BUTTON = Button(image=pg.image.load("assets/Play Rect.png"), pos=(640, 350), 
                                text_input="PLAY", font=self.get_font(60), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pg.image.load("assets/Options Rect.png"), pos=(640, 500), 
                                text_input="OPTIONS", font=self.get_font(60), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pg.image.load("assets/Quit Rect.png"), pos=(640, 650), 
                                text_input="QUIT", font=self.get_font(60), base_color="#d7fcd4", hovering_color="White")
            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.ecran)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pg.quit()
                        sys.exit()
            pg.display.update()
            
      
#-------------------- ecran globale   ----------------------------

img = pg.image.load('assets/main.jpg')               # importer l'image de l'arrière plan 
ecran = Ecran(img,Params.dim_ecran_x,                
                  Params.dim_ecran_y,
                  'Projet Kingdomino')

#---------------------------------------------

class Oriente:
    ''' conventions pour donner l'orientation d'un domino.
    Utilisation: if sens == Oriente.GD: '''
    GD = 0   # domino orienté Gauche à Droite
    HB = 1   # domino orienté Haut vers Bas
    DG = 2   # domino orienté Droite à Gauche
    BH = 3   # domino orienté Bas vers Haut
#------------------------------------------------------------------------------------------------------------------------------------------------    
def bonus (i,j):             # calculer le bonus d'une cellule jème dans un domino ième
    bonus=0
    for k in RL[i][j] :
        if k=="+" :
            bonus+=1
        else :
            continue
    return bonus

def domino_img (indice) :   # retourner l'image correspond au domino d'indice n à partir de la liste ld_img
    
        return ld_img[sort_list(Params.liste_dominos).index(RL[indice])]
    

class Cellule:             
    def __init__(self, numD=0 ,numC=0 ) :    # numéro de domino + numéro de la cellule
        
        #appel : CEL_ij = Cellule(i,j)  
        
        self._terrain = RL[numD][numC][0]  # prend la 1ere lettre de la cellule 
        self._bonus = bonus(numD,numC)     # fait appel a la fonction bonus qui calcul les pts d'une cellule définie par 
                                           #son numero 0 ou 1 et le numero du domino à qui elle appartient
        self._decompte = False    # utile pour calculer le score des zones
    def terrain(self):
        return self._terrain
    def bonus(self):
        return self._bonus
    def decompte(self):
        return self._decompte
    def set_decompte(self):
        self._decompte = True
    
class Domino:
    def __init__(self, numero = -1):
        self._numero = numero
        self._cellule = [Cellule(numero,0)
                         , Cellule(numero,1)]
        self._dom_img = domino_img (numero)
        
    def __getitem__(self, indice):   # implante l'indiçage: objet[indice]
        if isinstance(indice, int):   # implante l'indiçage par entier (pas par tranches)
            return self._cellule[indice]
        
    def numero(self):
        return self._numero
        

                                        #####      fonctions graphiques      ##########
    
    
# init musique---------------

def music():
    pg.mixer.init()
    pg.mixer.music.load("music/intro.mp3")
    pg.mixer.music.play(-1)
music()
#init graphique-----------------------

def init_graphiques():
    ecran.main_display_menu()
    
def message(ecran,texte):
    """ afficher un message à la position (61.5,30)  """
    ecran.cursor = (61.5,30)
    ecran.write("" * 8)  # efface ligne des messages
    ecran.write(texte)
    
# déclencher le curseur -------------
def dessiner_curs(ecran,x,y,pos=0):      
    '''indiquer l'ordre du jeu + dessiner le curseur dans la position (x,y) et le déplacer selon y   '''
    
    
    global liste_choix
    print("dessiner_curs actif !")
    
    pas=len(liste_choix[pos:pos+4])
    
    if pas < pos+1 :
        message(ecran,'joueur 1')       # ordre du jeu pour joueur 1
        
    print("liste_choix",liste_choix[pos:pos+4])
    ecran.cursor =(x,y)
    ecran.write('>>>')
    choix_domino(ecran,x,y,pos)                    # attendre que le joueur fasse son choix 
    ecran.cursor = (x,y)
    ecran.write(" - ")  # efface ligne des messages
    if y > 41 :
        y= 31
    if pas < 4 or ( (pas > 4 and pas < 8) ) :
        dessiner_curs(ecran,x,y+3.3,pos)           # récursivité de la fonction en changeant le y
                                                  # changement du position du curseur
        
#------------------------------------------------------   
def choix_domino(ecran,x,y,pos):          # choisir un domino en appuiant sur le bouton entrée ou bien quiter en appuiant
                                         # la flèche directionnelle vers le Bas (KEYDOWN)
    global liste_choix
    print("choix_domino actif !")
    pas = len(liste_choix[pos:pos+4])
    
    pg.event.clear()
    while True:
        event = pg.event.wait()
        if event.type == QUIT:  # toujours traiter action fermer la fenêtre de jeu
            exit()
            
        if (event.type == pg.KEYUP and         # si la touche ENTRÉE est appuie '''
               event.key == pg.K_RETURN) :
            
            domino_actif(x,y)                   
            
        if pas > pos+1 and pas < pos+3 :    # ordre du jeu pour joueur 2      
            message(ecran,'joueur 2' )
            ecran.cursor =(x,y)
        if pas == 4  :                    # si la longeur de la liste est égale à 4 (le choix est terminé)
            message(ecran,'        ' )
            jouer_tour(ecran,x,y,0)         # jouer le tour 0 
            ecran.cursor =(x,y)
            break
        if pas == 1 and pos==4  :            #si la longeur de la liste à partir de l'indice 4 est égale à 1 
            message(ecran,'        ' )
            jouer_tour(ecran,x,y,1)           # jouer le tour 1
            ecran.cursor =(x,y)
            return "pass"
        if (event.type == pg.KEYDOWN and event.key == pg.K_DOWN) :  # attendre relachement de touche en Bas
            break
        
#---------------------------------------------------------------
        
def domino_actif (x,y):    # en appuiant sur la touche d'entrée la fonction va ajouter l'indice du domino
                            # à la liste selon la position du curseur
    global liste_choix
    
    if y == 34.3 :
        liste_choix.append(0)
        return 0
    elif y >37.5 and y < 40 :
        liste_choix.append(1)
        return 1
    elif y > 40.8 and y < 44 :
        liste_choix.append(2)
        return 2
    elif y > 44 :
        liste_choix.append(3)
        return 3
    
#-------------------------------------------------------------    
def sort_list(l) :    # génère une liste res à partir d'une autre liste en ajoutant les élèments doublés une seule fois 
    res = [] 
    for i in l: 
        if i not in res: 
            res.append(i)
    return res

def dessiner_domino(self,x, y, domino, mode="normal"):    #  dessiner le domino en image dans la position (x,y) et selon le mode
    if mode == "normal" :
        self.ecran.blit(domino._dom_img,(x,y))
        
    if mode == "white_cover" :
        wht=pg.image.load('assets/LIST_DOMINO/white.png')
        wht=pg.transform.scale(wht, (90, 45))
        self.ecran.blit(wht,(x,y))
        
    if mode == "resize" :
        img=pg.transform.scale(domino._dom_img, (60, 30))
        self.ecran.blit(img,(x,y))
        
        
def dessiner_terrains(ecran,mode='ter_tab'):
    
    ''' dessiner les terrains, les chateaux et les
                    tables de dominos selon le mode choisi terrains+tables ou terrain '''
    
    Dx=Params.dim_ecran_x
    Dy=Params.dim_ecran_y
    Pas=abs(Params.dim_ecran_x-1280)
    castle=pg.image.load('assets/castle.png')
    castle=pg.transform.scale(castle, (30, 30))
    if mode == "ter_tab" or mode =="ter" :
        pg.draw.rect(ecran, (60, 50, 75), (Dx-1093-Pas, Dy-653-Pas, Dx-947, Dy-387))
        pg.draw.rect(ecran, (255, 255, 255), (Dx-1093-Pas, Dy-653-Pas, Dx-947, Dy-387),2)
        pg.draw.rect(ecran, (60, 50, 75), (Dx-533-Pas,Dy-653-Pas, Dx-947, Dy-387))
        pg.draw.rect(ecran, (255, 255, 255), (Dx-533-Pas,Dy-653-Pas, Dx-947, Dy-387),2)
        ecran.blit(castle, (Dx-940,Dy-500))
        ecran.blit(castle, (Dx-380,Dy-500))
    if mode =="ter_tab" :
        pg.draw.rect(ecran, (125, 80, 50), (Dx-630-Pas,Dy-250-Pas, Dx-1185, Dy-420))
        pg.draw.rect(ecran, (255, 255, 255), (Dx-630-Pas,Dy-250-Pas, Dx-1185, Dy-420),2)
        pg.draw.rect(ecran, (125, 80, 50), (Dx-860-Pas,Dy-250-Pas, Dx-1185, Dy-420))
        pg.draw.rect(ecran, (255, 255, 255), (Dx-860-Pas,Dy-250-Pas, Dx-1185, Dy-420),2)


def dessiner_tirage(self,x,y,pos):      # dessiner 4 dominos de la liste RL à partir de la position pos 
    for i in range (pos,pos+4) :
        y+=50
        dessiner_domino(ecran,x, y, Domino(i))
    #print('cellule :' , Dom.__getitem__(0)._terrain)
        
#---------------------------------------POSITIONS------------------------------------------
        
def limite(x,y,angl):                 # indiquer les frontières des terrains 
    v=(angl==0 or angl==180)
    if (x > 460 and v) or (x > 490 and not v):
        x= 190
    if x < 190 :
        if v : x= 460
        else : x = 490
    if (y > 370 and v) or (y > 340 and not v):
        y=70
    if y < 70 :
        if v : y= 370
        else : y = 340
    return [x,y]


def Pos_valide(x,y) :            # indiquer si la position de domino est valide ou pas avant de le poser 
    if ((x==280 and y == 220) or (x== 310 and (y in [190,220]))) :
        return True
    if ((x==340 and y == 160) or (y== 190 and (x in [310,340]))) :
        return True
    if ((x==340 and y == 250) or (y== 250 and (x in [310,340]))) :
        return True
    if ((x==370 and y == 220) or (y== 370 and (x in [190,220]))) :
        return True
    
#----------------------------------------------------------------
    
def placer_domino(self,domino):
    print("placer_domino actif !")
    clk = pg.time.Clock()
    running = True
    x=280
    y=160
    img =pg.transform.scale(domino._dom_img,(60,30))
    angl=0
    while running :
        mode ="normal"
        event = pg.event.wait()
        if event.type == QUIT:  # toujours traiter action fermer la fenêtre de jeu
            exit()
        if event.type == pg.KEYUP :
            if event.key == pg.K_SPACE :
                mode ="rotate"
            if event.key == pg.K_RETURN and Pos_valide(x,y):
                return [x,y]
            if event.key == pg.K_LEFT:
                x-=30
            if event.key == pg.K_RIGHT:
                x+=30
            if event.key == pg.K_UP:
                y-=30
            if event.key == pg.K_DOWN:
                y+=30
        x=limite(x,y,angl)[0]
        y=limite(x,y,angl)[1]
        if mode == 'normal' :
            dessiner_terrains(self.ecran,'ter')
            self.ecran.blit(img,(x,y))
        else :
            img = pg.transform.rotate(img,90)
            self.ecran.blit(img,(x,y))
            angl+=90
        pg.display.flip()
        clk.tick(60)
        
'''
def piocher_dominos(pile, nombre_rois):
 #récupérer le bon nombre de dominos pour ce tour, les trier par ordre de leur numéro
    l=preparer_dominos()[0:3]
    del (Rl[0:3])
'''
    
def pin_rois(ecran,x):                             # indiquer pour chaque domino le joueur qu'il la choisi
   for i in range(4) :
        ecran.cursor =(x-15,34.3+liste_choix[i]*3.3)
        if i < 2 :
            ecran.write('R1')
        else :
            ecran.write('R2')
            

def jouer_tour(ecran,x,y,tour=0):                   
    print("jouer_tour actif !" ,"tour ",tour)
    global pos
    global ls
    domino0 = Domino(liste_choix[0])
    domino1 = Domino(liste_choix[1])
    if tour==0 :
        event = pg.event.wait()
        if event.type == QUIT:  # toujours traiter action fermer la fenêtre de jeu
            exit()
        dessiner_tirage(ecran,x+319.2,y+405.8,0)
        dessiner_tirage(ecran,680,450,4)
        pin_rois(ecran,x)
        dessiner_domino(ecran,x+319.2,y+455.8,domino0,"white_cover")
        ls = placer_domino(ecran,domino0)
        dessiner_curs(ecran,x,y,4)

    if tour==1 :
        dessiner_domino(ecran,ls[0],ls[1],domino0,"resize")
        dessiner_domino(ecran,x+319.2,y+455.8+43.5,domino0,"white_cover")
        lss=placer_domino(ecran,domino1)
        dessiner_domino(ecran,ls[0],ls[1],domino1,"resize")
        dessiner_curs(ecran,x,y,4)
        
    if tour==2 :
        print("tour2")
        init_graphiques()
       
            
##### fonction principale


def kingdom():
    # initialisations
    init_graphiques()
    
    
if __name__ == "__main__":   # vrai si fichier exécuté et pas inclus comme module
    kingdom()
