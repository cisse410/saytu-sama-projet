from ..strategy import notification_strategy
from ..strategy import notification_context
from tache import Tache
from membre import Membre
from jalon import Jalon
from risque import Risque
from equipe import Equipe
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

    def set_notification_strategy(self, strategy: notification_strategy.NotificationStrategy) -> None:
        self.notification_context = notification_context.NotificationContext(strategy)

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

    def generer_rapport_performance(self) -> str:
        # Méthode fictive pour générer un rapport
        return "Rapport de performance"

    def calculer_chemin_critique(self) -> None:
        # Méthode fictive pour calculer le chemin critique
        pass

    def notifier(self, message: str, destinataires: List[Membre]) -> None:
        if self.notification_context:
            self.notification_context.notifier(message, destinataires)