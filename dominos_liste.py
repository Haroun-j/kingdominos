from random import randint
import pygame as pg
from params import Params

pg.init()
width = 90
height = 45
continuer = True


#-------------------------------------------------------
CC=pg.image.load('assets/LIST_DOMINO/CC.png')
CC=pg.transform.scale(CC, (width, height))
BB=pg.image.load('assets/LIST_DOMINO/BB.png')
BB=pg.transform.scale(BB, (width, height))
EE=pg.image.load('assets/LIST_DOMINO/EE.png')
EE=pg.transform.scale(EE, (width, height))
PP=pg.image.load('assets/LIST_DOMINO/PP.png')
PP=pg.transform.scale(PP, (width, height))
MM=pg.image.load('assets/LIST_DOMINO/MM.png')
MM=pg.transform.scale(MM, (width, height))
#---------------------------------
BC=pg.image.load('assets/LIST_DOMINO/BC.png')
BC=pg.transform.scale(BC, (width, height))
CE=pg.image.load('assets/LIST_DOMINO/CE.png')
CE=pg.transform.scale(CE, (width, height))
CP=pg.image.load('assets/LIST_DOMINO/CP.png')
CP=pg.transform.scale(CP, (width, height))
CM=pg.image.load('assets/LIST_DOMINO/CM.png')
CM=pg.transform.scale(CM, (width, height))
BE=pg.image.load('assets/LIST_DOMINO/BE.png')
BE=pg.transform.scale(BE, (width, height))
BP=pg.image.load('assets/LIST_DOMINO/BP.png')
BP=pg.transform.scale(BP, (width, height))
#-------------------------------------------------------
BC_=pg.image.load('assets/LIST_DOMINO/BC+.png')
BC_=pg.transform.scale(BC_, (width, height))
C_E=pg.image.load('assets/LIST_DOMINO/C+E.png')
C_E=pg.transform.scale(C_E, (width, height))
C_P=pg.image.load('assets/LIST_DOMINO/C+P.png')
C_P=pg.transform.scale(C_P, (width, height))
C_M=pg.image.load('assets/LIST_DOMINO/C+M.png')
C_M=pg.transform.scale(C_M, (width, height))
C_F=pg.image.load('assets/LIST_DOMINO/C+F.png')
C_F=pg.transform.scale(C_F, (width, height))
B_C=pg.image.load('assets/LIST_DOMINO/B+C.png')
B_C=pg.transform.scale(B_C, (width, height))
B_E=pg.image.load('assets/LIST_DOMINO/B+E.png')
B_E=pg.transform.scale(B_E, (width, height))
B_P=pg.image.load('assets/LIST_DOMINO/B+P.png')
B_P=pg.transform.scale(B_P, (width, height))
CE_=pg.image.load('assets/LIST_DOMINO/CE+.png')
CE_=pg.transform.scale(CE_, (width, height))
BE_=pg.image.load('assets/LIST_DOMINO/BE+.png')
BE_=pg.transform.scale(BE_, (width, height))
CP_=pg.image.load('assets/LIST_DOMINO/CP+.png')
CP_=pg.transform.scale(CP_, (width, height))
P_E=pg.image.load('assets/LIST_DOMINO/P+E.png')
P_E=pg.transform.scale(P_E, (width, height))
CM_=pg.image.load('assets/LIST_DOMINO/CM+.png')
CM_=pg.transform.scale(CM_, (width, height))
PM_=pg.image.load('assets/LIST_DOMINO/PM+.png')
PM_=pg.transform.scale(PM_, (width, height))
CF_=pg.image.load('assets/LIST_DOMINO/CF+.png')
CF_=pg.transform.scale(CF_, (width, height))
#-------------------------------------------------------
CP__=pg.image.load('assets/LIST_DOMINO/CP++.png')
CP__=pg.transform.scale(CP__, (width, height))
EP__=pg.image.load('assets/LIST_DOMINO/EP++.png')
EP__=pg.transform.scale(EP__, (width, height))
CM__=pg.image.load('assets/LIST_DOMINO/CM++.png')
CM__=pg.transform.scale(CM__, (width, height))
PM__=pg.image.load('assets/LIST_DOMINO/PM++.png')
PM__=pg.transform.scale(PM__, (width, height))
CF__=pg.image.load('assets/LIST_DOMINO/CF++.png')
CF__=pg.transform.scale(CF__, (width, height))
MF__=pg.image.load('assets/LIST_DOMINO/MF++.png')
MF__=pg.transform.scale(MF__, (width, height))
#-------------------------------------------------------
CF___=pg.image.load('assets/LIST_DOMINO/CF+++.png')
CF___=pg.transform.scale(CF___, (width, height))

#--------------------------MAIN-----------------------------
def preparer_dominos():
    RndDomList=[]
    liste_dominos = Params.liste_dominos
    while (len(RndDomList) < 24) :
        rand = randint(0,47)
        if liste_dominos[rand] not in RndDomList :
            RndDomList.append(liste_dominos[rand])
        else :
            continue
    return RndDomList

ld_img = [CC,BB,EE,PP,MM,BC,CE,CP,CM,BE,BP,BC_,C_E,C_P,C_M,C_F,B_C,B_E,B_P,CE_,BE_,
                     CP_,P_E,CM_,PM_,CF_,CP__,EP__,CM__,PM__,CF__,MF__,CF___]
RL = preparer_dominos()


