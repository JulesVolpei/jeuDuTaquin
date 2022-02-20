# Jeu du taquin

Ce dépôt est le résultat d'un projet universitaire portant sur la vulgarisation scientifique en regroupant deux matières (l'informatique ainsi que les mathématiques).

Nous avons donc choisi, dans le cadre de ce projet, de créer un algorithme permettant de résoudre le jeu du taquin, célèbre jeu de puzzle.


## Les règles :

![jeuDuTaquin](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbUT0ouQECz9RcjwlwbY05sGlhkq_MHNfsYA&usqp=CAU)

Le jeu du taquin se présente sous la forme d'un puzzle avec un certain nombre de cases numérotées ainsi qu'une case vide. Nous nous sommes concentrés sur le jeu du taquin en 3 * 3, possédant ainsi 9 cases dont une vide.

Le but du jeu est simple : faire en sorte de remettre chaque chiffre à sa place (à la manière de l'image ci-dessus).

Notre algorithme est divisé en quatres parties majeurs : 
- Savoir si un puzzle est réalisable
- Savoir si un coup est déjà fait
- Déterminer les autres coups possibles
- Afficher les différentes étapes

## Partie n°1
*Déterminer si un puzzle est réalisable ou non.*


* ### Principe d'inversion :

Prenons comme exemple le jeu du taquin ci-dessous :

```
| 1 | 5 | 7 |

| 8 |   | 6 |

| 3 | 2 | 4 |
```
Pour déterminer si ce puzzle est faisable ou non, nous allons prendre chaque nombre **mal placé** et compter le nombre de chiffre mal placés inférieur à ce dernier. 
Une fois le nombre d'inversion d'un nombre fait, on ne le compte plus pour les prochains calculs. **(1)**
Un puzzle est réalisable uniquement si son nombre d'inversions est un **chiffre pair**. **(2)**

*1* --> Le chiffre 1 est bien placé, on ne s'en occupe donc pas.

*5* --> **3**, **4**, **2** sont mal placés. Son nombre d'inversion est : 3 (car il y a 3 chiffres mal placés).

*7* --> **6**, **4**, **3**, **2** sont mal placés. Son nombre d'inversion est : 4 (on ne compte pas **5**, revoir **(1)**).

*8* --> **6**, **4**, **3**, **2** sont mal placés. Son nombre d'inversion est : 4.

*6* --> **3**, **4**, **2** sont mal placés. Son nombre d'inversion est : 3.

*3* --> **2** est mal placé. Son nombre d'inversion est : 1.

*2* --> `None` (aucun chiffre plus petit que 2 est mal placé).

*4* --> `None` ( aucun chiffre, revoir **(1)** ).

La somme des inversions est donc égal à 15, un chiffre impair. Or, si l'on se revient au point **(2)**, ce puzzle est donc impossible à résoudre.

## Partie n°2
*Savoir si un coup est déjà présent.*

Dans notre algorithme, les coups à partir de notre puzzle de départ sont effectués en dehors de notre boucle principale.
Les coups sont stockés de cette manière dans un dictionnaire :

```py
{ ( tuple(matriceRepresentantLePuzzle) ) : [ [coup n°1] ... ] }
```

Notre puzzle est traduit sous forme de matrice. Malheureusement, une matrice ne peut pas être considéré comme une clé dans un dictionnaire.
Nous avons donc transformé cette matrice en un tuple de tuple car les tuples peuvent être utilisés comme clé.

La valeur de la clé est une liste composée des matrices représentant les différents coups possibles.

Pour savoir quel coup faire, on crée deux matrices : `nouvelleMatrice` - `matriceDejaFait`.

À chaque coup réalisé (*partie n°3*) on va stocker ce coup dans `matriceDejaFait`. 
Pour déterminer quel coup faire, on va parcourir chaque valeur dans le dictionnaire pour savoir si elle est dans `matriceDejaFait`, sinon on l'ajoute dans `nouvelleMatrice`.

### Auteurs :
 - Volpei Jules ( https://github.com/JulesVolpei )
 - Gonzales Andy( https://github.com/GonzalesAndy ) 
 - Leydier Elisée ( https://github.com/EliseeLeydier )
 - Canale Enzo ( https://github.com/eenzocl )
