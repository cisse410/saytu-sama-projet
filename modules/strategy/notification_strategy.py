"""
Module NotificationStrategy
"""

import dataclasses
from abc import ABC, abstractmethod
from modules.membre import Membre


@dataclasses.dataclass
class NotificationStrategy(ABC):
    """
    Ce module est une interface qui permet de definir la methode
    a utiliser pour envoyer des notifications
    """

    @abstractmethod
    def envoyer(self, message: str, destinataire: Membre) -> None:
        """
        Cette methode est utilisee pour envoyer des notifications
        :param message:
        :param destinataire:
        :return:
        """
        raise NotImplementedError
