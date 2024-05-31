from ..membre import Membre 

class NotificationStrategy:
    def envoyer(self, message: str, destinataire: Membre) -> None:
        raise NotImplementedError