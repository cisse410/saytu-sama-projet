"""
Module NotificationContext
"""

import dataclasses

from modules.membre import Membre


@dataclasses.dataclass
class NotificationContext:
    """
    NotificationContext module
    """

    def __init__(self, strategy):
        """
        Init methode
        :param strategy:
        """
        self.strategy = strategy

    def notifier(self, message: str, destinataires: list[Membre]) -> None:
        """
        Emettre des notifications
        :param message:
        :param destinataires:
        :return:
        """
        for destinataire in destinataires:
            self.strategy.envoyer(message, destinataire)
