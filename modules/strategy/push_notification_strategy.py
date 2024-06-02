"""
Module PushNotificationStrategy
"""

import dataclasses

from modules.membre import Membre
from modules.strategy.notification_strategy import NotificationStrategy


@dataclasses.dataclass
class PushNotificationStrategy(NotificationStrategy):
    """
    Module PushNotificationStrategy
    """

    def envoyer(self, message: str, destinataire: Membre) -> None:
        """
        Cette methode est une redefinition de la methode
        envoyer definie dans la module NotificationStrategy
        :param message:
        :param destinataire:
        :return:
        """
        print(f"Notification Push envoyée à {destinataire.nom}: {message}")
