import notification_strategy
from ..modules import membre
class SMSNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: membre.Membre) -> None:
        print(f"SMS envoyé à {destinataire.nom}: {message}")

