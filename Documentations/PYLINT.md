<h2 style="text-decoration: underline; ,font-family: arial; color: #D3D3D3;" align="left">
    Avant Capture (1)
</h2> 
<p align="center">
    <img style="width: 100%; background-position:center; background-size: cover; background-repeat: no-repeat;" align="center" src="./Captures images des  commandes/pylint-before-1.png" />
</p>

<h2 style="text-decoration: underline; ,font-family: arial; color: #D3D3D3;" align="left">
    Avant Capture (2)
</h2> 
<p align="center">
    <img style="width: 100%; background-position:center; background-size: cover; background-repeat: no-repeat;" align="center" src="./Captures images des  commandes/pylint-before-2.png" />
</p>
<h2 style="text-decoration: underline; ,font-family: arial; color: #D3D3D3;" align="left">
    Avant Capture main.py
</h2> 
<p align="center">
    <img style="width: 100%; background-position:center; background-size: cover; background-repeat: no-repeat;" align="center" src="./Captures images des  commandes/pylint-main-before.png" />
</p>

<h2 style="text-decoration: underline; ,font-family: arial; color: #D3D3D3;" align="left">
   Aprés Capture
</h2> 
<p align="center">
    <img style="width: 100%; background-position:center; background-size: cover; background-repeat: no-repeat;" align="center" src="./Captures images des  commandes/pylint-main-after.png" />
</p>
<a align="center" href="https://mypy-lang.org/">
    <h1 style="color: blue;font-family: arial; " >
        PYLINT
    </h1>
</a>

<h2 style="  font-family: arial; color: #D3D3D3;" align="left">
    Analyse de la sortie du commande:
</h2> 

<p style="" align="left">
Avant l'utilisation d'outils de formatage et de vérification de code, plusieurs incohérences et erreurs de style étaient présentes dans le projet, comme le montrent les résultats de l'analyse PyLint.
Analyse des Modules (pylint-before-1.png)

L'analyse PyLint sur les modules de notre projet a révélé plusieurs types de problèmes récurrents :

    Manque de Docstrings :
        Modules : Tous les modules analysés manquent de docstrings.
        Classes : Toutes les classes manquent de docstrings.
        Fonctions : Les fonctions et méthodes manquent également de docstrings.

    Nombre Insuffisant de Méthodes Publiques :
        Les classes dans modules.changement, modules.jalon et modules.membre ont trop peu de méthodes publiques.

    Nombre Excessif d'Attributs d'Instance :
        La classe dans modules.projet possède trop d'attributs d'instance.

Ces problèmes montrent un manque général de documentation dans le code et certaines violations des bonnes pratiques de conception des classes.
Analyse du Fichier Principal (pylint-main-before.png)

L'analyse PyLint sur main.py avant les corrections a révélé les problèmes suivants :

    Lignes Trop Longues :
        Plusieurs lignes dépassent la limite de 100 caractères.

    Manque de Docstrings :
        Le module, les classes, et les fonctions manquent de docstrings.

    Redéfinition de Noms :
        Les noms projet et rapport sont redéfinis par rapport à une portée externe.

    Nombre Insuffisant de Méthodes Publiques :
        Une classe a trop peu de méthodes publiques.

    Concatenation de Chaînes :
        Utilisation incorrecte de f-strings et de concaténation implicite de chaînes.

Ces problèmes indiquent des incohérences dans la longueur des lignes de code, des redéfinitions de variables et une utilisation inappropriée des chaînes de caractères, en plus du manque de documentation.
Actions Correctives et Améliorations Apportées

Suite à l'analyse initiale, des outils de formatage et de vérification de code ont été utilisés pour améliorer la qualité du code :
Utilisation de black pour le Formatage Automatique

L'exécution de black sur le projet a produit les résultats suivants :

    Fichiers Reformatés :
        Un fichier (modules/strategy/sms_notification_strategy.py) a été reformaté automatiquement.
        Les autres fichiers respectaient déjà les conventions de style de black.

Utilisation de flake8 pour la Vérification des Erreurs de Style

En plus de black, flake8 a été utilisé pour détecter les erreurs de style et les importations inutilisées.
Impact sur la Qualité du Code

L'application des outils de formatage et de vérification a eu les impacts suivants :

    Conformité Automatique aux Standards :
        black applique automatiquement les conventions PEP 8, garantissant ainsi que le code respecte les standards de la communauté Python sans nécessiter une intervention manuelle.

    Lisibilité Améliorée :
        Le code uniformément formaté est plus facile à lire et à naviguer, ce qui est particulièrement bénéfique pour les équipes de développement travaillant sur le même projet.

    Réduction des Conflits de Fusion :
        Avec un format de code cohérent, les risques de conflits de fusion liés au style sont réduits, facilitant ainsi la collaboration entre les développeurs.

Résultats Post-Correction (pylint-main-after.png)

L'analyse PyLint après corrections a montré une amélioration notable :

    Note de Qualité : La note globale est passée de 7.94/10 à 10.00/10.
    Réduction des Erreurs : Les erreurs de ligne trop longue, les redéfinitions de noms, et les problèmes de concaténation de chaînes ont été corrigés.
    Docstrings : Bien que certaines docstrings manquent encore, une amélioration a été notée dans la documentation des modules, classes, et fonctions.

En conclusion, l'utilisation combinée de black et flake8, suivie des corrections identifiées par PyLint, a permis de renforcer la qualité du code en le rendant plus lisible, plus maintenable et conforme aux meilleures pratiques de la communauté Python. Ces outils ont aidé à identifier et à corriger les problèmes de style de manière efficace, améliorant ainsi la qualité globale du code.
</p>
