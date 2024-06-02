"""
Module EmailNotificationStrategy
"""

import dataclasses

from modules.strategy.notification_strategy import NotificationStrategy
from modules.membre import Membre


@dataclasses.dataclass
class EmailNotificationStrategy(NotificationStrategy):
    """
    Cette module permet de definir la strategie de notification par email
    """

    def envoyer(self, message: str, destinataire: Membre) -> None:
        """
        Cette methode est une redefinition de la methode envoyer
         definie dans la module NotificationStrategy
        :param message:
        :param destinataire:
        :return:
        """
        print(f"{message}")
