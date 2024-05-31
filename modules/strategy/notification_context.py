from modules.strategy.notification_strategy import NotificationStrategy
from modules.membre import Membre


class NotificationContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def notifier(self, message: str, destinataires: list[Membre]) -> None:
        for destinataire in destinataires:
            self.strategy.envoyer(message, destinataire)
