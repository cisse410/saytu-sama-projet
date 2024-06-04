"""
Module Projet
"""

from dataclasses import dataclass
from datetime import datetime
from modules.strategy.notification_context import NotificationContext
from modules.strategy.notification_strategy import NotificationStrategy
from modules.equipe import Equipe
from modules.membre import Membre
from modules.tache import Tache
from modules.jalon import Jalon
from modules.risque import Risque
from modules.changement import Changement


@dataclass
class Projet:
    """
    Module qui permet de définir un projet
    """

    def __init__(
        self, nom: str, description: str, date_debut: datetime, date_fin: datetime
    ):
        """
        Initialisation d'un projet
        :param nom:
        :param description:
        :param date_debut:
        :param date_fin:
        """
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.taches: list[Tache] = []
        self.equipe = Equipe()
        self.budget = 0.0
        self.risques: list[Risque] = []
        self.jalons: list[Jalon] = []
        self.version = 1
        self.changements: list[Changement] = []
        self.chemin_critique: list[Tache] = []
        self.notification_context: NotificationContext = None

    def set_notification_strategy(self, strategy: NotificationStrategy):
        """
        Methode pour definir la methode de notification
        :param strategy:
        :return:
        """
        self.notification_context = NotificationContext(strategy)

    def ajouter_tache(self, tache: Tache) -> None:
        """
        Methode pour ajouter une tache a un projet
        :param tache:
        :return:
        """
        self.taches.append(tache)
        for membre in self.equipe.membres:
            print(f"Email envoyé à {membre.nom} : " f"Nouvelle tâche:  {tache.nom}")
        print("######")

    def ajouter_membre_equipe(self, membre: Membre) -> None:
        """
        Methode permettant d'ajouter un membre a une equipe
        :param membre:
        :return:
        """
        self.equipe.ajouter_membre(membre)

    def definir_budget(self, budget: float) -> None:
        """
        Methdode pour definir le budget du projet
        :param budget:
        :return:
        """
        self.budget = budget
        for membre in self.equipe.membres:
            print(
                f"Email envoyé à {membre.nom} :"
                f" Le budget du projet a été défini à :  {self.budget} FCFA"
            )
        print("######")

    def ajouter_risque(self, risque: Risque) -> None:
        """
        Methode qui permet d'ajout un risque a un projet
        :param risque:
        :return:
        """
        self.risques.append(risque)
        for membre in self.equipe.membres:
            print(
                f"Email envoyé à {membre.nom} : "
                f"Nouveau risque ajouté:  {risque.description}"
            )
        print("######")

    def ajouter_jalon(self, jalon: Jalon) -> None:
        """
        Methode pour ajouter
        :param jalon:
        :return:
        """
        self.jalons.append(jalon)
        for membre in self.equipe.membres:
            print(
                f"Email envoyé à {membre.nom} : " f"Nouveau jalon ajouté:  {jalon.nom}"
            )
        print("######")

    def enregistrer_changement(self, description: str) -> None:
        """
        Methode pour enregistrer les changements intervnus au cours du projet
        :param description:
        :return:
        """
        changement = Changement(description, self.version, datetime.now())
        self.changements.append(changement)
        self.version += 1
        for membre in self.equipe.membres:
            print(
                f"Email envoyé à {membre.nom} :"
                f" Changement enregistré: Changement de la portée du projet: "
                f"(version {self.version})"
            )
        print("######")

    def generer_rapport_performance(self) -> str:
        """
        Methode pour generer un rapport de performance d'un projet
        :return:
        """
        rapport = f"""\t\t\t\t\t###########################################\n
        ########### Rapport de Performance du Projet {self.nom} ###########\n
        \t\t\t###########################################\n\n\n"""

        rapport += (
            f"Date de génération : " f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        )

        rapport += "## Progrès des Tâches:\n"
        for tache in self.taches:
            rapport += (
                f"- {tache.nom}: "
                f"{tache.statut},"
                f" Durée restante: "
                f"{tache.date_fin - tache.date_debut}\n"
            )

        rapport += "\n## Retards par rapport au Planning:\n"
        for tache in self.taches:
            if tache.date_fin < tache.date_debut:
                rapport += (
                    f"- {tache.nom} est en "
                    f"retard car sa date de fin ({tache.date_fin})"
                    f"est antérieure à sa "
                    f"date de début ({tache.date_debut}).\n"
                )

        rapport += "\n## Utilisation des Ressources:\n"
        rapport += f"- Budget utilisé: {self.budget}\n"
        rapport += f"- Nombre de membres de " f"l'équipe: {len(self.equipe.membres)}\n"

        rapport += "\n## Risques Identifiés:\n"
        for risque in self.risques:
            rapport += f"- {risque.description}\n"

        return rapport

    def calculer_chemin_critique(self):
        """
        Methode pour determiner le chemin critique d'un projet
        :return:
        """
        self.chemin_critique = [
            tache for tache in self.taches if tache.statut == "En cours"
        ]

    def notifier(self, message: str, destinataires: list[Membre]) -> None:
        """
        Methode pour envoyer une notification
        :param message:
        :param destinataires:
        :return:
        """
        if self.notification_context:
            self.notification_context.notifier(message, destinataires)
