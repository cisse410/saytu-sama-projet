from modules.strategy.notification_strategy import NotificationStrategy
from modules.membre import Membre


class EmailNotificationStrategy(NotificationStrategy):
    def envoyer(self, message: str, destinataire: Membre) -> None:
        print(f"Email envoyé à {destinataire.nom}: {message}")
