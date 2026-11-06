import os
import re

from repository.users_repository import get_coach,get_users, create_user, delete_user
from repository.subscription_repository import get_subscription, create_subscription, delete_subscription
from repository.training_repository import get_training, create_training, delete_training
from repository.followcourse_repository import get_followcourse
from db.db import Database

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[37m'
    RESET = '\033[0m'


def afficher_table_generique(headers, lignes):
    """
    Affiche n'importe quelle table SQL de manière propre et alignée.
    
    :param headers: Liste des noms de colonnes (ex: ["ID", "Email", "Nom", "Abo"])
    :param lignes: Liste de tuples/listes de données (provenant du fetchall de votre DB)
    """
    if not headers:
        print("Aucune colonne à afficher.")
        return

    # 1. Calcul dynamique de la largeur max pour chaque colonne (minimum 10 caractères)
    largeurs = [len(h) for h in headers]
    for ligne in lignes:
        for i, cellule in enumerate(ligne):
            longueur_texte = len(str(cellule)) if cellule is not None else 4 # "None"
            if longueur_texte > largeurs[i]:
                largeurs[i] = longueur_texte
                
    # Ajoute une petite marge de sécurité de 2 espaces à chaque colonne
    largeurs = [w + 2 for w in largeurs]

    # 2. Construction de la ligne de séparation (ex: +------+---------------+---+)
    separateur = "+" + "+".join("-" * w for w in largeurs) + "+"

    # 3. Affichage des en-têtes
    print(separateur)
    ligne_entete = "|" + "|".join(f" {headers[i]:<{largeurs[i]-1}}" for i in range(len(headers))) + "|"
    print(ligne_entete)
    print(separateur)

    # 4. Affichage des lignes de données
    for ligne in lignes:
        ligne_texte = "|"
        for i, cellule in enumerate(ligne):
            valeur = str(cellule) if cellule is not None else "NULL"
            ligne_texte += f" {valeur:<{largeurs[i]-1}}|"
        print(ligne_texte)

    # 5. Fermeture du tableau
    print(separateur)
    

if __name__ == "__main__":
    continue_app = True
    db = Database()
    

    while continue_app:
            os.system('cls')
            print(f"Welcome to {bcolors.OKCYAN}Super Fitness 🏋️")  
            print()  
            print(f"{bcolors.HEADER}{"(1) Get all users":<30}")
            print(f"{"(2) Create user":<30}")
            print(f"{"(3) Delete user":<30}")
            print(f"{"(4) Get all subscription":<30}")
            print(f"{"(5) Create subscription":<30}")
            print(f"{"(6) Delete subscription":<30}")
            print(f"{"(7) Course training":<30}")
            print(f"{"(71) List Coach":<30}")
            print(f"{"(8) Create Course training":<30}")
            print(f"{"(9) Delete Course training":<30}")
            print(f"{"(10) get all follow course":<30}")
            print(f"{"(Q) Quit":<30}")
            print()
            #getint / getstr
            choice = input(f"{bcolors.WHITE}Votre choix > ")
            
            match choice.lower():
                case "1":
                    colonnes_users = ["ID", "Email", "Firstname", "Subscription", "Role"]
                    donnee_users = get_users()
                    afficher_table_generique(colonnes_users, donnee_users)                    
                    input(">")      
                case "2":
                    
                    while True:
                        email=input("Enter email:")
                        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                        if re.match(pattern,email):
                            break
                        else:
                            print("Incorrect email")
                    
                    
                    last_name=input("Enter name:")
                    lerole=input("Enter role:")                
                    colonnes_subscription = ["ID", "Type", "Price", "Weeks"]
                    donnee_subscription = get_subscription()
                    afficher_table_generique(colonnes_subscription, donnee_subscription)                      
                    abo=input("Type d'abonnement (ID):")
                    id=create_user(email,last_name,lerole,abo)
                    print(f"User has been created with ID: {id}")              
                    input(">")      
                    
                case "3":
                    colonnes_users = ["ID", "Email", "Firstname", "Subscription", "Role"]
                    donnee_users = get_users()
                    afficher_table_generique(colonnes_users, donnee_users)   
                    id = input("User to delete, give the ID > ")
                    rows_count = delete_user(id)
                    print(f"{rows_count} row(s) deleted")
                    input(">")      
                    
                case "4":
                    colonnes_subscription = ["ID", "Type", "Price", "Weeks"]
                    donnee_subscription = get_subscription()
                    afficher_table_generique(colonnes_subscription, donnee_subscription)                       
                    input(">")      
                
                case "5":
                    type=input("Enter Type :")
                    price=input("Enter Price :")
                    duree=input("Enter #Week :")
                    id=create_subscription(type, price, duree)
                    print(f"The new subscription has already been created {id}")              
                    input(">")  
                case "6":
                    colonnes_subscription = ["ID", "Type", "Price", "Weeks"]
                    donnee_subscription = get_subscription()
                    afficher_table_generique(colonnes_subscription, donnee_subscription)                               
                    print("-----------------------")
                    id = input("Entrez l'id de la subscription à supprimer : ")
                    rows_count = delete_subscription(id)
                    print(f"{rows_count} lignes modifié")
                    input(">")
                    
                case "7":
                    colonnes_training = ["ID", "Description", "Start Hour", "End Hour", "Day", "Last Name"]
                    donnee_training = get_training()
                    afficher_table_generique(colonnes_training, donnee_training)           
                    input(">")          
                    
                case "71":
                    colonnes_coach = ["ID", "Email", "Last Name"]
                    donnee_coach = get_coach()
                    afficher_table_generique(colonnes_coach, donnee_coach)  
                    input(">")                       
                    
                case "8":                    
                    colonnes_coach = ["ID", "Email", "Last Name"]
                    donnee_coach = get_coach()
                    afficher_table_generique(colonnes_coach, donnee_coach)  
                    print("-----------------------")
                    coach = input("Coach selected ID: > ")
                    description=input("Enter description :")
                    hour_start=input("Enter start hour :").zfill(2)                                   
                    min_start=input("Entre les min de départ :").zfill(2)                                   
                    hour_end=input("Entre l'heure de fin :").zfill(2)                                   
                    min_end=input("Entre les min de fin :").zfill(2)                                   
                    
                    day=input("Enter the day (0: Sunday,...) :")
                    input(">")                 
                    id=create_training(description, hour_start+':'+min_start, hour_end+':'+min_end, day, coach)
                    print(f"The new subscription has already been created {id}")              
                    input(">") 
                    
                case "9":
                    colonnes_training = ["ID", "Description", "Start Hour", "End Hour", "Day", "Last Name"]
                    donnee_training = get_training()
                    afficher_table_generique(colonnes_training, donnee_training)   
                    print("-----------------------")
                    id = input("Entrez l'id de la subscription à supprimer : ")
                    rows_count = delete_training(id)
                    print(f"{rows_count} lignes modifié")
                    input(">")     
                    
                case "10":
                    colonnes_followcourse = ["Nom", "Course Taken", "Start", "End", "Day"]
                    donnee_followcourse = get_followcourse()
                    afficher_table_generique(colonnes_followcourse, donnee_followcourse)   
                    input(">")                                                                
                                    
                                        
                case "q":
                    continue_app = False
            
    db.close()
    