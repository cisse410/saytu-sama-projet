          ███████  █████  ██    ██ ████████ ██    ██     ███████  █████  ███    ███  █████       
          ██      ██   ██  ██  ██     ██    ██    ██     ██      ██   ██ ████  ████ ██   ██         
          ███████ ███████   ████      ██    ██    ██     ███████ ███████ ██ ████ ██ ███████         
               ██ ██   ██    ██       ██    ██    ██          ██ ██   ██ ██  ██  ██ ██   ██         
          ███████ ██   ██    ██       ██     ██████      ███████ ██   ██ ██      ██ ██   ██
          
                         ██████  ██████   ██████       ██ ███████ ████████
                         ██   ██ ██   ██ ██    ██      ██ ██         ██
                         ██████  ██████  ██    ██      ██ █████      ██
                         ██      ██   ██ ██    ██ ██   ██ ██         ██
                         ██      ██   ██  ██████   █████  ███████    ██  

## Objectif du projet
<p>Dans l'optique de mettre en pratique nos connaissances en mesure qualité et performance logicielle, on est amené à mettre en place un système de gestion de projet en utilisant Python.</p>
Notre solution porte le nom de <b>"Saytu Sama Projet"</b>, une solution qui se veut performante autant que possible avec un code de qualité non discutable 😂 avec les bonnes pratiques de codage qui facilitera sans doute la maintenance du projet.

## Structure du projet</b>
![struct](https://github.com/cisse410/saytu-sama-projet/assets/80828135/e60570e5-2518-43dd-8428-5b7ab3368ad1)
Notre projet est organisé de la manière suivante :
-Le dossier principal se compose de 3 sous-dossiers (Documentation, Modules et Tests).
-Dans le dossier nommé ```Documentations```, nous avons le sous-dossier ```Captures images des  commandes``` où nous avons placé les captures d'écran des sorties des commandes, suivies des fichiers Markdown avec leurs analyses.
-Dans le dossier nommé ```modules```, nous trouvons les classes principales ainsi que le sous-dossier ```strategy```, contenant les fichiers liés au ```design pattern Strategy```
-Dans le dossier appelé ```tests```, nous avons simplement les classes de test qui testent toutes les méthodes de notre code à l'aide de la bibliothèque ```unittest```
 
## Fonctionnalités offertes par <b>Saytu Sama Projet</b>

- Ajouter des tâches, des membres d'équipe, des risques, des jalons et enregistrer des changements
- <p>Notifier les membres de l'équipe lors de l'ajout ou de la modification des éléments du projet.</p>
Les notifications sont gérées en utilisant le ```design pattern Strategy```. Elles peuvent être envoyer soit par mail soit par SMS.
- Générer un rapport des activités du projet.</p>

Concernant les test, nous avons utilisé la bibliothèque ```unittest``` offertes par python pour écrire nos classes de tests.</p>
Pour la mesure et la qualité du code, nous avons certaines bibliothèques tièrces comme: </p>
- ```flake8``` : Pour vérifier la conformité au convention de codage de PEP 8 </p>
- ```pylint``` : Pour identifier les erreurs de programmation, les conventions de codage non respectées </p>
- ```mypy``` : Pour vérifier le typage statique et détecte les erreurs de typage</p>
- ```coverage``` : Pour analyser la couverture du code de nos tests</p>
- ```vulture``` : Pour détecter les variables non utilisées dans notre code</p>
- ```black``` : Pour le reformatage automatique de notre code en respectant les conventions de PEP 8</p>
- ```radon``` : Pour la complexité cyclomatique et la structuration globale du code</p>
- ```pyflakes``` : Pour la vérifier les erreurs de syntaxe et les problèmes de style</p>

## Comment demarré le projet?
Pour lancer le projet en local, il suffit juste de cloner le projet dans un répertoire de votre choix en exécutant la commande :
```bash
git clone https://github.com/cisse410/saytu-sama-projet.git
```
 et ensuite l'ouvrir avec votre éditeur de code préféré.


## Projet réalisé par 
 - <a href="https://github.com/pape-medoune">Mouhamedoune FALL</a>
 - <a href="https://github.com/cisse410">Issakha CISSE</a>
