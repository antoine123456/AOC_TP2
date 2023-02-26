# Introduction
Ce projet vise à trouver et appliquer des optimisations sur les codes fournis. L'objectif principal de ces codes est de comparer des séquences d'ADN. Un script *gensesq* s'occupe de créer des suites ADN (`ATCG...`), et *mask* compare ces séquences en utilisant un opérateur logique `XOR`.

## Observation
Grâce à **maqao**, on peut voir que la fonction mask contenue dans le fichier *mask* constitue le plus grand goulot d'étranglement.

## Métriques
Afin d'évaluer les performances de nos améliorations, nous nous référons au temps d'exécution CPU, recueilli à l'aide de la fonction *clock_gettime*. Le débit est également déduit de la taille des données.

## Améliorations
Les changements sont réalisés en trois parties :

- Ajout de pragmas de compilation
- Modification du code, ajout de mots-clés
- Parallélisation
Chaque version cumule les améliorations précédentes.

### Version initiale
> __Performance obtenue : 35'126'482.667 ns__

### Ajout de pragmas de compilation
La plupart des flags usuels sont déjà appliqués à la compilation, notamment :

- march=native
- -Ofast
- -finline-functions
- -fopenmp
- -fopt-info-all=dist.gcc.optrpt
Parmi les ajouts cités précédemment, le compilateur est indiqué pour utiliser les optimisations spécifiques à l'architecture utilisée, de favoriser l'efficacité au temps de compilation, favoriser l'intégration des fonctions à l'endroit où elles sont appelées.

Nous pouvons ajouter le *pragma* **-funroll-loops**, limitant le nombre de sauts pour l'exécution des boucles (1 saut équivalent à 10 cycles de processeurs).

> __Performance obtenue : 31'372'243.667 ns__

### Modification du code, ajout de mots-clés
La première opération a été de limiter la taille de certaines valeurs *u64* en *u8* ou de `float` à `double`. J'ai par la suite ajouté des mots-clés permettant d'aligner la mémoire sur des blocs de 64 octets. Pour cela, nous utilisons ``posix_memalign``. Pour limiter la portée des fonctions ou variables, nous ajoutons le mot-clé ``static``. De même, pour éviter le partage de mémoire entre pointeurs, nous utilisons ``restrict``.

> __Performance obtenue : 29'716'514.677 ns__

### Parallélisation
Finalement, la boucle principale étant libre de toutes dépendances, nous pouvons simplement demander à *OpenMP* de partager la charge de travail entre plusieurs threads. Nous précisons quelle section paralléliser à l'aide du ``#pragma omp parallel for schedule(static)``. La directive ``schedule(static)`` indique au compilateur de répartir les itérations de la boucle for de manière équitable entre les threads. Cela signifie que chaque thread exécutera le même nombre d'itérations de la boucle ``for``.

> __Performance obtenue : 5'112'055.52 ns__


# V0


# V1 ajout de pramas de compilation
- funroll-loops

# v2 changements de types
- u64 -> u8
- doubles -> float

- ==> ajouter : static & const & inline & restrict 

# v3 ajout de parallelisation

$((100*2**20))


u8* const restric