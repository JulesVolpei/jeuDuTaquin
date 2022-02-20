import time


def verifieSiTrouve(dict, matrice):
    """
    :param dict: Dictionnaire des coups
    :param matrice: Matrice d'arrivée
    :return: False si la matricé d'arrivée n'est trouvée nul part
    """
    for key, value in dict.items():     # On va parcourir TOUTES les valeurs du dictionnaire pour vérifier si la matrice d'arrivée est présente
        for i in value:
            if matrice == i:
                # Si la matrice de la valeur est la matrice d'arrivée, on retourne sa clé
                return key
    # La matrice d'arrivée n'est pas présente
    return False

def transformeEnTuple(matrice):
    """
    :param matrice: Matrice quelconque
    :return: La matrice transformée en tuple
    """
    tpl = ()    #On commence par créer un premier tuple pour pouvoir y ajouter les autres
    for i in range(len(matrice)):
        ultTpl = ()
        for j in matrice[i]:    #On prend chaque liste quand la matrice
            tplTmp = (j,)   #Chaque élément dans la matrice est ajouté à un tuple
            ultTpl += tplTmp    #Tuple qui est lui-même ajouté à un tuple
        tpl += (ultTpl,)        #Avant d'être finalement ajouté à notre tuple de départ pour reformer une matrice
    return tpl
def determinerCoupsPossible(matrice):
    """
    :param matrice: Matrice de départ ou matrice obtenue
    :return: Permet de savoir où on peut bouger la case vide
    """
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            # On essaye de trouver où se trouve le 0 pour en extraire ses coordonnées
            if matrice[i][j] == 0:
                indice = (i, j)
                break
    # On va maintenant déterminer tous les coups possible
    # Premier cas où 0 se trouve dans la première liste
    if indice == (0, 0):
        return indice, [[0, 1], [1, 0]]
    if indice == (0, 1):
        return indice, [[0, 0], [0, 2], [1, 1]]
    if indice == (0, 2):
        return indice, [[0, 1], [1, 2]]
    # Second cas où 0 se trouve dans la deuxième liste
    if indice == (1, 0):
        return indice, [[0, 0], [2, 0], [1, 1]]
    if indice == (1, 1):
        return indice, [[0, 1], [2, 1], [1, 0], [1, 2]]
    if indice == (1, 2):
        return indice, [[0, 2], [1, 1], [2, 2]]
    #Troisème cas où 0 est dans la troisième liste
    if indice == (2, 0):
        return indice, [[1, 0], [2, 1]]
    if indice == (2, 1):
        return indice, [[2, 0], [1, 1], [2, 2]]
    if indice == (2, 2):
        return indice, [[2, 1], [1, 2]]

def afficherMat(matrice):
    """
    :param matrice: Une matrice quelconque
    :return: L'affiche de telle sorte à pouvoir voir les colonnes
    """
    for i in matrice:
        print(i)


def permute(matrice, objet, indiceCoup):
    """
    :param matrice: Matrice quelconque
    :param objet: La matrice avec l'indice de 0 et des coups possibles
    :param indiceCoup: Coup actuel
    :return: La nouvelle matrice une fois le 0 bougé
    """
    matrice[objet[0][0]][objet[0][1]], matrice[objet[1][indiceCoup][0]][objet[1][indiceCoup][1]] = matrice[objet[1][indiceCoup][0]][objet[1][indiceCoup][1]], matrice[objet[0][0]][objet[0][1]]
    return matrice


def creerLesMatricesDeNouveauxCoups(matriceDebut, objet):
    """
    :param matrice: Matrice obtenue
    :param objet: La matrice avec l'indice de 0 et des coups possibles
    :return: Une liste comportant les matrices des coups une fois fait
    """
    matriceTmp = []         #On va créer une copie de matriceDebut pour pouvoir le modifier librement
    for i in range(len(matriceDebut)):
        matriceTmp.append([])       # On ajoute une liste, correspondant à la liste de matriceDebut
        for j in range(len(matriceDebut[i])):
            matriceTmp[i].append(matriceDebut[i][j])    #On ajoute chaque coef

    matriceCoupsPossible = []       #On crée une matrice qui va stocker les matrices de coups possible

    # On définit le nombre de liste dans matriceCoupsPossible par le nombre de coups possible (assez logique gg Jules)
    for i in range(len(objet[1])):
        matriceCoupsPossible.append(permute(matriceTmp, objet, i))     #Chaque liste va permettre de stocker une nouvelle matrice avec le 0 changé
        #On utilise permute() avec la copie de matriceDebut pour pouvoir recréer une copie de matriceDebut après l'opération
        matriceTmp = []    # On recrée une copie pour pouvoir reprendre matriceDebut
        for i in range(len(matriceDebut)):
            matriceTmp.append([])
            for j in range(len(matriceDebut[i])):
                matriceTmp[i].append(matriceDebut[i][j])
    return matriceCoupsPossible



def remonterDict(dict, cle, matriceEtape, cmpt):
    """
    :param dict: Dictionnaire des coups
    :param cle: Clé avec la valeur correspondant à la matrice d'arrivée
    :param matriceEtape: Matrice qui va répertorier les différentes étapes nécessaires
    :param cmpt: Nombre de coups nécessaires pour compléter le puzzle
    :return: La matrice avec tous les coups nécessaires
    """
    siBreak = False
    for i in range(cmpt):
        for key in dict.keys():
            for j in range(len(dict[key])):
                if cle == transformeEnTuple(dict[key][j]):
                    matriceEtape.append(dict[key][j])
                    cle = key
                    siBreak = True
                    break
            if siBreak:
                siBreak = False
                break
    return matriceEtape

def main():
    matriceDepart = [[0, 1, 2],
                     [3, 4, 5],
                     [6, 7, 8]]        #On commence par créer notre matrice de départ
    #matriceDepart = melanger(matriceDepart)     #On mélange cette fameuse matrice
    objet = determinerCoupsPossible(matriceDepart)
    dictCoups = {}
    dictCoups[transformeEnTuple(matriceDepart)] = creerLesMatricesDeNouveauxCoups(matriceDepart, objet)     #On met les premiers coups avec la matrice de départ
    print('Working progress ...')
    nbrCoups = 0
    while(True):
        #On commence par vérifier si on a trouvé la matrice d'arrivée ou non
        if not verifieSiTrouve(dictCoups, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]) == False:
            cleFin = verifieSiTrouve(dictCoups, [[1, 2, 3], [4, 5, 6], [7, 8, 0]])
            print('DONE !')
            print("Réalisable en : ", nbrCoups, " coups.")
            break

        #On va maintenant essayer de savoir si une matrice dans les valeurs n'a pas été faite en tant que clé (en gros que c'est un nouveau coup)
        nouvelleMatrice = []
        matriceDejaFaite = []       # Liste de matrice déjà présentes dans le dictionnaire
        for key, value in dictCoups.items():    #On va parcourir les clés et éléments du dictionnaire
            for i in range(len(value)):
                if not value[i] in matriceDejaFaite:      #Si une des matrices dans les valeurs a déjà une clé crée, on next
                    nouvelleMatrice.append(value[i])        #Sinon, c'est un nouveau coup possible et on l'ajoue à nouvelleMatrice

        for i in range(len(nouvelleMatrice)):       #On parcours ensuite nouvelleMatrice
            objet = determinerCoupsPossible(nouvelleMatrice[i])
            dictCoups[transformeEnTuple(nouvelleMatrice[i])] = creerLesMatricesDeNouveauxCoups(nouvelleMatrice[i], objet)
            matriceDejaFaite.append(nouvelleMatrice[i])

        nbrCoups += 1

    # On va remonter le dictionnaire pour pouvoir trouver les différentes étapes nécessaires pour le résoudre
    etape = []      #On crée une matrice avec les différentes étapes nécessaires pour résoudre le puzzle
    etape.append([[1, 2, 3], [4, 5, 6], [7, 8, 0]])     #On lui fait d'abord apprendre l'arrivée car on va parcourir etape à l'envers
    etape = remonterDict(dictCoups, cleFin, etape, nbrCoups)
    for i in range(len(etape)):
        afficherMat(etape[len(etape) - (1 + i)])    #Parcours à l'envers
        time.sleep(1)       #On génère une attente de 1 seconde entre chaque affichage pour avoir une petite représentation visuelle
        print(" ")




if __name__ == '__main__':
    main()