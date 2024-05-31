from modules.strategy.notification_strategy import NotificationStrategy
from modules.membre import Membre


class SMSNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: Membre) -> None:
        print(f"SMS envoyé à {destinataire.nom}: {message}")

