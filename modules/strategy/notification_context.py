from notification_strategy import NotificationStrategy
from ..modules import membre
class NotificationContext:
    def _init_(self, strategy: NotificationStrategy):
        self.strategy = strategy

    def notifier(self, message: str, destinataires: List[membre.Membre]) -> None:
        for destinataire in destinataires:
            self.strategy.envoyer(message, destinataire)