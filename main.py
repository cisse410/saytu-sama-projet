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

class RapportActivite:
    @staticmethod
    def generer(projet):
        rapport = "\n"
        rapport += f"Rapport d'activités du Projet '{projet.nom}':\n"
        rapport += f"Version: {projet.version}\n"
        rapport += f"Dates: {projet.date_debut.strftime('%Y-%m-%d')} à {projet.date_fin.strftime('%Y-%m-%d')}\n"
        rapport += f"Budget: {projet.budget} Unité Monétaire\n"
        rapport += "Équipe:\n"
        for membre in projet.equipe.obtenir_membres():
            rapport += f"- {membre.nom} ({membre.role})\n"
        rapport += "Tâches:\n"
        for tache in projet.taches:
            rapport += f"- {tache.nom} ({tache.date_debut.strftime('%Y-%m-%d')} à {tache.date_fin.strftime('%Y-%m-%d')}), "
            rapport += f"Responsable: {tache.responsable.nom}, Statut: {tache.statut}\n"
        rapport += "Jalons:\n"
        for jalon in projet.jalons:
            rapport += f"- {jalon.nom} ({jalon.date.strftime('%Y-%m-%d')})\n"
        rapport += "Risques:\n"
        for risque in projet.risques:
            rapport += f"- {risque.description} (Probabilité: {risque.probabilite}, Impact: {risque.impact})\n"
        rapport += "Chemin Critique:\n"
        for tache in projet.chemin_critique:
            rapport += f"- {tache.nom} ({tache.date_debut.strftime('%Y-%m-%d')} à {tache.date_fin.strftime('%Y-%m-%d')})\n" 
        projet.generer_rapport_performance() 
        return rapport

 

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
    
    print(f"""\t\t#########################################################################\n
        ################# Envoie des notifications aux membres ##################\n
        #########################################################################\n""")
    # Création des membres de l'équipe
    
    
    membre1 = Membre("Fatou", "Chef de projet")
    membre2 = Membre("Moussa", "Développeur")
    membre3 = Membre("Awa", "Analyste")

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
                   datetime(2024, 2, 1), datetime(2024, 12, 15),
                   membre3, "En cours")
    tache2 = Tache("Développement", "Développer les fonctionnalités principales",
                   datetime(2024, 2, 1), datetime(2024, 12, 15),
                   membre2, "En cours")
    tache3 = Tache("Tests", "Réaliser les tests unitaires et d'intégration",
                   datetime(2024, 5, 1), datetime(2024, 11, 30),
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
 

    # Calcul du chemin critique (fictif)
    projet.calculer_chemin_critique()
 
    
    print(f"""\n\t\t#########################################################################\n
        #################### Rapport du Projet {projet.nom} ######################\n
        #########################################################################\n""")
    rapport = RapportActivite.generer(projet)
    print(rapport)
    
    
    
    rapport_performance = projet.generer_rapport_performance()
    
    print(rapport_performance)