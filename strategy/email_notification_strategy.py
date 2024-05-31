import notification_strategy
from ..modules import membre
class EmailNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: membre.Membre) -> None:
        print(f"Email envoyé à {destinataire.nom}: {message}")
