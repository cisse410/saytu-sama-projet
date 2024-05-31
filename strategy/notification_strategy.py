from ..modules import membre

class NotificationStrategy:
    def envoyer(self, message: str, destinataire: membre.Membre) -> None:
        raise NotImplementedError