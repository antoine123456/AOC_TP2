
# Introduction
Pour commencer nous avons testé le code initial avec maqao. Le premier résultat nous à permis de voir que la fonction "linearSolver" était la plus coûteuse du programme. Les améliorations apportées pour palier ce problème se sont organisées comme suit :
- Ajout de **flags** de compilation
- Modification du **code** source
- Ajout de **librairies** (*non traité par manque de temps*)

# Améliorations apportés
## Ajout de **flags**
Les ajouts évidents ont pour but de demander le déroulement des courtes boucles avec *-funroll-loops*, cette optimisation est utile notament pour la boucle la plus interne de la fonction . Ensuite le flag *Ofast* a pour but de inliner les fonctions, vectoriser, propager les constantes, améliorer le scheduling et le pipelining, cependant le code est ainsi moins portable et plus dur à debugger. Cette optimisation ajout notement le calcul de "*1/c*" une seule fois avant le déroulement de la boucle.
Finalement *march=native* nous permet d'optimiser le code généré pour notre architecture et avoir des instructions assembleurs suplémentaires.


## Modification du **code**
Notre premier constat à été de limiter le nombre d'accès à la fonction *build_index* dans de corps des boucles, cela à été résolu en déclarant une seule fois la valeur accédée.

Ensuite on limite l'utilisation de build index à une seule fois par tour de boucle interne ce qui est permis en accédant à partir de l'index retourné aux lignes et colonnes pécédentes et suivante par une simple addition.

Avec l'aide de **Maqao** nous avons vu qu'il y avait trop de lecture/écriture cependant aucune amélioration ne nous a semblé possible.

Nous avons souhaité réduire les accès aux tableaux et aux appels de fonctions. Pour cela nous avons ajouté les mots-clés static et restrict sur la fonction *linearSolver* et sur les tableaux "*x*" et "*x0*" ce qui permet d'éviter des appels de fonctions et pour les tableaux être sûr qu'ils n'entrent pas en conflit.