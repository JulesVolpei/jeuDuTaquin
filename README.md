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

## Partie n°3
*Déterminer les coups possibles.*

Pour déterminer quel coup sont réalisables, on va d'abord parcourir `nouvelleMatrice` pour en saisir chaque matrice de coups non réalisés.
On en ensuite parcourir cette matrice pour en ressortir la coordonnée du 0 (*représentant la case vide*) dans la matrice ainsi que les différents coups réalisables.

### Savoir quels coups sont possibles

Pour déterminer quel coup sont réalisables, nous allons regarder la position du 0 dans notre puzzle. Prenons ce puzzle comme exemple :

```
| 5 | 2 | 1 |

| 6 | 8 | 4 |

| 7 | 3 | 0 |
```

On peut voir que le 0 est à l'indice `(2, 2)`, ses coordonnées sont donc dans un premier temps stockées dans une variable. 
On va ensuite procéder avec du cas par cas. Si 0 est à l'indice `(2, 2)`, les différents coups possibles sont : `[[1, 2], [2, 1]]`. Ces coups sont stockés dans une matrice.

Nous allons ensuite renvoyer un tuple nommé `objet` avec à l'indice 0 de ce dernier, les coordonnées de la case vide et à l'indice 1 ses déplacements possibles.

Une fois le tuple renvoyé, une fonction va se charger de créer une liste de matrice correspondant aux puzzles une fois les différents coups appliqués.

Après ces opérations, nous allons reprendre la matrice à l'origine de ces nouveaux coups pour la transformer en tuple de tuples et ainsi ajouter un nouveau couple clé / valeur à notre dictionnaire de coups.

À la fin de cette étape, nous allons rappeler la liste `matriceDejaFait` pour venir y ajouter la matrice à l'origine des coups pour en pas créer de doublons.

On réitère donc l'opération, calculant ainsi toutes les possiblitées possibles pour chaque nouveau puzzle avant de trouver dans une des valeurs d'une de nos clés la matrice : 

```
| 1 | 2 | 3 |

| 4 | 5 | 6 |

| 7 | 8 | 0 |
```

On compte également chaque fois que l'on crée de nouvelles clés dans notre dictionnaire, nous permettant d'en déduire le nombre d'étape nécessaire.

## Partie n° 4
(*Déterminer les coups à réaliser pour abouttir au résultat*).

Grâce à notre variable comptant le nombre d'opérations nécessaires, nous allons pouvoir remonter notre dictionnaire pour en déduire les coups à réaliser pour résoudre notre puzzle d'origine.

Pour se faire, nous créeons une nouvelle liste de matrices : `etape` qui va dans un premier temps ajouter comme premier élément notre matrice **d'arrivée**.
Nous allons ensuite prendre la clé comportant dans ses valeurs notre matrice d'arrivée et parcourir toutes les valeurs pour retrouver une clé possédant cette matrice comme valeur. 

On récupère cette nouvelle clé que l'on ajoute à notre liste de matrices et on réitère l'opération jusqu'à atteindre la valeur de notre compteur (*partie n°3*) pour venir y récupérer le tout premier coup joué menant à notre solution.

On commence donc par afficher le puzzle d'origine avant de parcourir **à l'envers** notre liste `etape`.

### Auteurs :
 - Volpei Jules ( https://github.com/JulesVolpei )
 - Gonzales Andy( https://github.com/GonzalesAndy ) 
 - Leydier Elisée ( https://github.com/EliseeLeydier )
 - Canale Enzo ( https://github.com/eenzocl )
