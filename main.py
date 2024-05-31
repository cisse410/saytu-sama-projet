from datetime import datetime
from modules.projet import Projet
from modules.equipe import Equipe
from modules.membre import Membre
from modules.tache import Tache
from modules.jalon import Jalon
from modules.risque import Risque
from modules.strategy.email_notification_strategy import EmailNotificationStrategy
from modules.strategy.sms_notification_strategy import SMSNotificationStrategy
from modules.strategy.push_notification_strategy import PushNotificationStrategy

if __name__ == '__main__':

    print("""
        
    ███████  █████  ██    ██ ████████ ██    ██     ███████  █████  ███    ███  █████       
    ██      ██   ██  ██  ██     ██    ██    ██     ██      ██   ██ ████  ████ ██   ██         
    ███████ ███████   ████      ██    ██    ██     ███████ ███████ ██ ████ ██ ███████         
         ██ ██   ██    ██       ██    ██    ██          ██ ██   ██ ██  ██  ██ ██   ██         
    ███████ ██   ██    ██       ██     ██████      ███████ ██   ██ ██      ██ ██   ██
    
                ██████  ██████   ██████       ██ ███████ ████████
                ██   ██ ██   ██ ██    ██      ██ ██         ██
                ██████  ██████  ██    ██      ██ █████      ██
                ██      ██   ██ ██    ██ ██   ██ ██         ██
                ██      ██   ██  ██████   █████  ███████    ██  
    """)
    # Création des membres de l'équipe
    membre1 = Membre("Alice", "Chef de projet")
    membre2 = Membre("Bob", "Développeur")
    membre3 = Membre("Charlie", "Analyste")

    # Création de l'équipe et ajout des membres
    equipe = Equipe()
    equipe.ajouter_membre(membre1)
    equipe.ajouter_membre(membre2)
    equipe.ajouter_membre(membre3)

    # Création du projet
    projet = Projet("Projet MQPL", "Développement d'une application de "
                                   "gestion de projet", datetime(2024, 6, 1),
                    datetime(2024, 12, 31))
    projet.ajouter_membre_equipe(membre1)
    projet.ajouter_membre_equipe(membre2)
    projet.ajouter_membre_equipe(membre3)
    projet.definir_budget(100000.0)

    # Création des tâches
    tache1 = Tache("Analyse des besoins", "Analyser les besoins du client",
                   datetime(2024, 6, 1), datetime(2024, 6, 15),
                   membre3, "En cours")
    tache2 = Tache("Développement", "Développer les fonctionnalités principales",
                   datetime(2024, 6, 16), datetime(2024, 9, 30),
                   membre2, "En attente")
    tache3 = Tache("Tests", "Réaliser les tests unitaires et d'intégration",
                   datetime(2024, 10, 1), datetime(2024, 11, 30),
                   membre2, "En attente")

    projet.ajouter_tache(tache1)
    projet.ajouter_tache(tache2)
    projet.ajouter_tache(tache3)

    # Ajout des dépendances
    tache2.ajouter_dependance(tache1)
    tache3.ajouter_dependance(tache2)

    # Ajout de jalons
    jalon1 = Jalon("Fin de l'analyse des besoins", datetime(2024, 6, 15))
    jalon2 = Jalon("Fin du développement", datetime(2024, 9, 30))

    projet.ajouter_jalon(jalon1)
    projet.ajouter_jalon(jalon2)

    # Ajout de risques
    risque1 = Risque("Retard de livraison", 0.3, "Moyen")
    risque2 = Risque("Bug critique", 0.1, "Élevé")

    projet.ajouter_risque(risque1)
    projet.ajouter_risque(risque2)

    # Enregistrement de changement
    projet.enregistrer_changement("Modification des spécifications fonctionnelles")

    # Notification par email
    projet.set_notification_strategy(EmailNotificationStrategy())
    projet.notifier("La tâche 'Analyse des besoins' est en cours.", projet.equipe.obtenir_membres())

    # Notification par SMS
    projet.set_notification_strategy(SMSNotificationStrategy())
    projet.notifier("La tâche 'Développement' est en attente.", projet.equipe.obtenir_membres())

    # Notification par Push
    projet.set_notification_strategy(PushNotificationStrategy())
    projet.notifier("La tâche 'Tests' est en attente.", projet.equipe.obtenir_membres())

    # Génération du rapport de performance
    rapport = projet.generer_rapport_performance()
    print(rapport)

    # Calcul du chemin critique (fictif)
    projet.calculer_chemin_critique()
