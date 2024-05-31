from modules.membre import Membre
from modules.strategy.notification_strategy import NotificationStrategy


class PushNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: Membre) -> None:
        print(f"Notification Push envoyée à {destinataire.nom}: {message}")
