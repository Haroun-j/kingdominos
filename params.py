class Params:
    ''' paramètres du jeu : seulement des variables de classe, pas de méthodes
        ni de variables d'instances/objets
        exemple d'utilisation: pile_dominos = Params.dominos'''
    # couleurs utiles définies en RGB sur [0,255]
    couleurs_utiles = {
        'champ'   : (198, 175, 15),
        'bois'    : (52, 122, 48),
        'pature'  : (135, 220, 69),
        'marais'  : (154, 182, 135),
        'filon'   : (170, 110, 90),
        'eau'     : (80, 115, 224),
        'chateau' : (255, 255, 255),
        'interdit': (0, 0, 0),
        'autorisé': (100, 100, 100),
        'rouge'   : (213, 11, 11),
        'bleu'    : (11, 11, 240),
        'blanc'   : (255, 255, 255),
        'noir'    : (0, 0, 0)
    }
    # couleur associées aux types de terrain des cellules
    couleur = {
        'i': couleurs_utiles['interdit'],
        'a': couleurs_utiles['autorisé'],
        '#': couleurs_utiles['chateau'],
        'C': couleurs_utiles['champ'],
        'E': couleurs_utiles['eau'],
        'P': couleurs_utiles['pature'],
        'M': couleurs_utiles['marais'],
        'F': couleurs_utiles['filon'],
        'B': couleurs_utiles['bois'],
    }
    # liste des dominos du jeu comme nuplets d'abbréviations de terrains avec
    # chaque bonus marqué comme "+": ces nuplets devront être traduits en objets Domino
    liste_dominos = [
        ("C", "C"), ("C", "C"), ("B", "B"), ("B", "B"), ("B", "B"), ("B", "B"),
        ("E", "E"), ("E", "E"), ("E", "E"), ("P", "P"), ("P", "P"), ("M", "M"),
        ("B", "C"), ("C", "E"), ("C", "P"), ("C", "M"), ("B", "E"), ("B", "P"),
        ("B", "C+"), ("C+", "E"), ("C+", "P"), ("C+", "M"), ("C+", "F"), ("B+", "C"),
        ("B+", "C"), ("B+", "C"), ("B+", "C"), ("B+", "E"), ("B+", "P"), ("C", "E+"),
        ("C", "E+"), ("B", "E+"), ("B", "E+"), ("B", "E+"), ("B", "E+"), ("C", "P+"),
        ("P+", "E"), ("C", "M+"), ("P", "M+"), ("C", "F+"), ("C", "P++"), ("E", "P++"),
        ("C", "M++"), ("P", "M++"), ("C", "F++"), ("M", "F++"), ("M", "F++"), ("C", "F+++")
        ]
    # nombre et répartitions des rois # 4 rois, 2 pour joueur 0, 2 pour joueur 1
    nombre_rois = (4, (2, 2))  
    # dimensions pour tracer les terrains des joueurs
    taille_terrain = 11  # taille du côté de la zone de jeu en nombre de cellules
    taille_cellule = (20, 10)  # taille (x,y) cellule de zone de jeu en caracteres
    dim_ecran_x = 1280
    dim_ecran_y = 720
    # ligne où afficher les infos sans pause
    lig_info = (taille_terrain - 2) * taille_cellule[1] + 2
    # ligne où afficher les messages avec pause
    lig_message = (taille_terrain + 8) * taille_cellule[1] + 4