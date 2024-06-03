<h2 style="text-decoration: underline; ,font-family: arial; color: #D3D3D3;" align="left">
    Avant Capture
</h2> 
<p align="center">
    <img style="width: 100%; background-position:center; background-size: cover; background-repeat: no-repeat;" align="center" src="./Captures images des  commandes/mypy-before.png" />
</p>

<h2 style="text-decoration: underline; ,font-family: arial; color: #D3D3D3;" align="left">
   Aprés Capture
</h2> 
<p align="center">
    <img style="width: 100%; background-position:center; background-size: cover; background-repeat: no-repeat;" align="center" src="./Captures images des  commandes/mypy-after.png" />
</p>
<a align="center" href="https://mypy-lang.org/">
    <h1 style="color: blue;font-family: arial;" >
        MYPY
    </h1>
</a>

<h2 style="text-decoration: underline; ,font-family: arial; color: #D3D3D3;" align="left">
    Analyse de la sortie du commande:
</h2> 

<p style="" align="left"> 

Analyse de la Sortie de la Commande `mypy`

Analyse Initiale du Code

Nous avons exécuté la commande `mypy` sur notre projet pour vérifier la conformité des types dans le code. Voici les résultats obtenus et les actions correctives entreprises.


**Première Exécution : Vérification Initiale**

Après avoir apporté des modifications au code, une nouvelle exécution de `mypy` sur `main.py` a révélé plusieurs erreurs :

Erreurs de typage détectées :
   ```plaintext
   (.venv) PS C:\Users\vPro\Desktop\licence3\semestre6\mesure_qualite\ssp> mypy .\main.py
   modules/tache.py:40: error: Need type annotation for "dependances" (hint: "dependances: list[<type>] = ...")  [var-annotated]
   modules/projet.py:37: error: Need type annotation for "taches" (hint: "taches: list[<type>] = ...")  [var-annotated]
   modules/projet.py:40: error: Need type annotation for "risques" (hint: "risques: list[<type>] = ...")  [var-annotated]
   modules/projet.py:41: error: Need type annotation for "jalons" (hint: "jalons: list[<type>] = ...")  [var-annotated]
   modules/projet.py:43: error: Need type annotation for "changements" (hint: "changements: list[<type>] = ...")  [var-annotated]
   modules/projet.py:44: error: Need type annotation for "chemin_critique" (hint: "chemin_critique: list[<type>] = ...")  [var-annotated]
   modules/projet.py:53: error: Incompatible types in assignment (expression has type "NotificationContext", variable has type "None")  [assignment]
   Found 7 errors in 2 files (checked 1 source file)
   ```

Problèmes Identifiés :

Annotations de type manquantes :
   - Plusieurs variables nécessitent des annotations de type explicites. Par exemple :
     ```plaintext
     modules/tache.py:40: error: Need type annotation for "dependances"
     modules/projet.py:37: error: Need type annotation for "taches"
     ```

Types incompatibles dans les affectations :
   - Une affectation de type incompatible a été détectée :
     ```plaintext
     modules/projet.py:53: error: Incompatible types in assignment
     ```

Actions Correctives et Améliorations Apportées

Ajout des annotations de type :
   - Nous avons ajouté les annotations de type pour les variables qui en avaient besoin. Par exemple :
     ```python
     dependances: list[Type] = []
     taches: list[Type] = []
     risques: list[Type] = []
     jalons: list[Type] = []
     changements: list[Type] = []
     chemin_critique: list[Type] = []
     ```

Correction des affectations de type :
   - Nous avons ajusté les affectations pour correspondre aux types attendus. Par exemple :
     ```python
     context: Optional[NotificationContext] = None
     if some_condition:
         context = NotificationContext()
     ```


**Deuxième Exécution : Après Modification du Code**

Vérification du fichier `main.py` :
   ```plaintext
   (.venv) PS C:\Users\vPro\Desktop\licence3\semestre6\mesure_qualite\ssp> mypy .\main.py
   Success: no issues found in 1 source file
   ```
   Aucune erreur n'a été détectée dans `main.py`, indiquant que ce fichier respecte les annotations de type.


Vérification du répertoire `modules` :
   ```plaintext
   (.venv) PS C:\Users\vPro\Desktop\licence3\semestre6\mesure_qualite\ssp> mypy .\modules\
   Success: no issues found in 14 source files
   ```
   Tous les fichiers dans le répertoire `modules` ont été analysés sans qu'aucune erreur de type ne soit détectée, ce qui est un bon indicateur de la qualité du typage dans ce répertoire.


Impact sur la Qualité du Code

Améliorations apportées :

Lisibilité accrue :
   - Les annotations de type rendent le code plus explicite, facilitant ainsi la compréhension du type de chaque variable.

Robustesse du code :
   - En corrigeant les types incompatibles, nous réduisons les risques d'erreurs d'exécution liées aux types incorrects.

Conformité aux standards :
   - En adhérant aux meilleures pratiques de typage en Python, notre code devient plus aligné avec les standards de la communauté, facilitant ainsi la collaboration et la maintenance future.

**Conclusion :**

L'utilisation de `mypy` comme outil d'analyse statique nous a permis d'identifier et de corriger des problèmes de typage. Ces corrections ont amélioré la qualité du code en termes de lisibilité, de robustesse et de conformité aux standards de typage Python.
</p>
