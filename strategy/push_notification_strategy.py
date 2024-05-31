import notification_strategy
from ..modules import membre
class PushNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: membre.Membre) -> None:
        print(f"Notification Push envoyée à {destinataire.nom}: {message}")