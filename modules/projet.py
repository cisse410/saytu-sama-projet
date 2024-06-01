from datetime import datetime

from modules.strategy.notification_context import NotificationContext
from modules.strategy.notification_strategy import NotificationStrategy
from modules.equipe import Equipe
from modules.membre import Membre
from modules.tache import Tache
from modules.jalon import Jalon
from modules.risque import Risque
from modules.changement import Changement


class Projet:
    def __init__(self, nom: str, description: str, date_debut: datetime, date_fin: datetime):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.taches = []
        self.equipe = Equipe()
        self.budget = 0.0
        self.risques = []
        self.jalons = []
        self.version = 1
        self.changements = []
        self.chemin_critique = []
        self.notification_context = None

    def set_notification_strategy(self, strategy: NotificationStrategy) -> None:
        self.notification_context = NotificationContext(strategy)

    def ajouter_tache(self, tache: Tache) -> None:
        self.taches.append(tache)

    def ajouter_membre_equipe(self, membre: Membre) -> None:
        self.equipe.ajouter_membre(membre)

    def definir_budget(self, budget: float) -> None:
        self.budget = budget

    def ajouter_risque(self, risque: Risque) -> None:
        self.risques.append(risque)

    def ajouter_jalon(self, jalon: Jalon) -> None:
        self.jalons.append(jalon)

    def enregistrer_changement(self, description: str) -> None:
        changement = Changement(description, self.version, datetime.now())
        self.changements.append(changement)
        self.version += 1

    from datetime import datetime

    def generer_rapport_performance(self) -> str: 
        # Construction du header du rapport
        rapport = f"""\t\t#########################################################################\n
        ############# Rapport de Performance du Projet {self.nom} ##############\n
        #########################################################################\n\n"""
                     
        rapport += f"Date de génération : {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"

        # Section sur le progrès des tâches
        rapport += "## Progrès des Tâches:\n"
        for tache in self.taches:
            rapport += f"- {tache.nom}: {tache.statut}, Durée restante: {tache.date_fin - tache.date_debut}\n"

        # Adjusted Section on Delays Compared to the Plan
        rapport += "\n## Retards par rapport au Planning:\n"
        for tache in self.taches:
            # Assuming you want to check if the task is overdue, i.e., its end date is earlier than its start date
            if tache.date_fin < tache.date_debut:
                rapport += f"- {tache.nom} est en retard car sa date de fin ({tache.date_fin}) est antérieure à sa date de début ({tache.date_debut}).\n"

        # Section on Resource Usage
        rapport += "\n## Utilisation des Ressources:\n"
        rapport += f"- Budget utilisé: {self.budget}\n"
        rapport += f"- Nombre de membres de l'équipe: {len(self.equipe.membres)}\n"

        # Section on Identified Risks
        rapport += "\n## Risques Identifiés:\n"
        for risque in self.risques:
            rapport += f"- {risque.description}\n"
 
        return rapport


    
    def calculer_chemin_critique(self): 
        self.chemin_critique = [tache for tache in self.taches if tache.statut == "En cours"]

    def notifier(self, message: str, destinataires: list[Membre]) -> None:
        if self.notification_context:
            self.notification_context.notifier(message, destinataires)
