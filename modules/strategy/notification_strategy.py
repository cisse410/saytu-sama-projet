from abc import ABC, abstractmethod
from modules.membre import Membre


class NotificationStrategy(ABC):
    @staticmethod
    def envoyer(self, message: str, destinataire: Membre) -> None:
        raise NotImplementedError
