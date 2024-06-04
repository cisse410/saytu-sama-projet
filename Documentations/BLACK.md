# Documentation de BLACK

<h2 style="text-decoration: underline; ,font-family: arial; color: #D3D3D3;" align="left">
    Capture d'écran de la sortie du commande BLACK :
</h2> 
<p align="center">
    <img style="width: 100%; background-position:center; background-size: cover; background-repeat: no-repeat;" align="center" src="./Captures images des  commandes/black capture.jpeg" />
</p>
<a align="center" href="https://pypi.org/project/black/">
    <h1 style="color: blue;font-family: arial;"  >
        BLACK
    </h1>
</a>

<h2 style="text-decoration: underline; ,font-family: arial; color: #D3D3D3;" align="left">
    Analyse de la sortie du commande:
</h2> 

<p style="" align="left">
Analyse Initiale du Code

Avant l'utilisation de l'outil de formatage automatique black, notre projet avait certaines incohérences de style de code, même après l'utilisation de flake8 pour détecter les erreurs de style et les importations inutilisées. Pour uniformiser le format du code et s'assurer qu'il respecte les conventions PEP 8 de manière cohérente, nous avons décidé d'exécuter black sur notre projet.


**Exécution de l'Outil black**

L'exécution de black sur le répertoire .\modules\ a produit les résultats suivants :

- Fichiers Reformatés :
        Un fichier a été reformaté automatiquement : modules/strategy/sms_notification_strategy.py.
- Le reste des fichiers (13) sont restés inchangés car ils respectaient déjà les conventions de style prises en charge par black.

**Actions Correctives et Améliorations Apportées**

L'utilisation de black a permis les améliorations suivantes :

**Uniformisation du Format du Code :**
        Le fichier sms_notification_strategy.py a été automatiquement reformaté pour s'aligner sur les normes de style de black. 

**Amélioration de la Lisibilité et de la Maintenabilité :**
        En appliquant un format de code cohérent sur l'ensemble du projet, notre code devient plus facile à lire et à comprendre pour tous les développeurs.
        Cela aide également à éviter les conflits de style lors des révisions de code, car tous les développeurs suivent automatiquement les mêmes règles de formatage.

Impact sur la Qualité du Code

Les améliorations apportées par black ont les impacts suivants :

**Conformité Automatique aux Standards :** black applique automatiquement les conventions PEP 8, garantissant ainsi que notre code respecte les standards de la communauté Python sans nécessiter une intervention manuelle.

**Lisibilité Améliorée :** Notre code uniformément formaté est plus facile à lire et à naviguer, ce qui est particulièrement bénéfique pour les équipes de développement travaillant sur le même projet.
    Réduction des Conflits de Fusion : Avec un format de code cohérent, les risques de conflits de fusion liés au style sont réduits, facilitant ainsi la collaboration entre les développeurs.

En conclusion, l'utilisation de black en complément de flake8 a permis de renforcer la qualité de notre code en le rendant plus lisible, plus maintenable et conforme aux meilleures pratiques de la communauté Python. Ces outils nous ont aidés à identifier et à corriger les problèmes de style de manière efficace, améliorant ainsi la qualité globale de notre code.
</p>
