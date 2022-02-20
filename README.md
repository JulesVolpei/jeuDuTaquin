# Jeu du taquin

Ce dépôt est le résultat d'un projet universitaire portant sur la vulgarisation scientifique en regroupant deux matières (l'informatique ainsi que les mathématiques).

Nous avons donc choisi, dans le cadre de ce projet, de créer un algorithme permettant de résoudre le jeu du taquin, célèbre jeu de puzzle.


## Les règles :

![jeuDuTaquin](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbUT0ouQECz9RcjwlwbY05sGlhkq_MHNfsYA&usqp=CAU)

Le jeu du taquin se présente sous la forme d'un puzzle avec un certain nombre de cases numérotées ainsi qu'une case vide. Nous nous sommes concentrés sur le jeu du taquin en 3 * 3, possédant ainsi 9 cases dont une vide.

Le but du jeu est simple : faire en sorte de remettre chaque chiffre à sa place (à la manière de l'image ci-dessus).
Pour se faire, nous allons d'abord réfléchir à un problème : *un puzzle est-il toujours réalisable ?*



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

### Auteurs :
 - Volpei Jules ( https://github.com/JulesVolpei )
 - Gonzales Andy( https://github.com/GonzalesAndy ) 
 - Leydier Elisée ( https://github.com/EliseeLeydier )
 - Canale Enzo ( https://github.com/eenzocl )
