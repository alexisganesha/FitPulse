import os

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
            print(f"{"(8) Create Course training":<30}")
            print(f"{"(9) Delete Course training":<30}")
            print(f"{"(10) get all follow course":<30}")
            print(f"{"(Q) Quit":<30}")
            print()
            #getint / getstr
            choice = input(f"{bcolors.WHITE}Votre choix > ")
            
            match choice.lower():
                case "1":
                    print(f"{'ID':<20}{'Email':<40}{'Firstname':<20}{'Abonnement':<20}")
                    print(f"="*100)
                    headers = [("ID", 20), ("Email", 40), ("Firstname", 20), ("Abonnement", 20)]
                    row_str = ""
                    
                    for user in get_users():
                        for i,element in enumerate(user):
                            print(f"{element:<{headers[i][1]}}", sep="", end="")
                        print("\n")                
                    print(row_str)
                    input(">")      
                case "2":
                    email=input("Entrez l'email :")
                    last_name=input("Entre le nom :")
                    lerole=input("Entre le rôle :")
                    id=create_user(email,last_name,lerole)
                    print(f"l'utilisateur a bien été créé avec l'id {id}")              
                    input(">")      
                    
                case "3":
                    print("-----------------------")
                    for v in get_users():
                        print(v)
                    print("-----------------------")
                    id = input("Entrez l'id de l'utilisateur à supprimer : ")
                    rows_count = delete_user(id)
                    print(f"{rows_count} lignes modifié")
                    input(">")      
                    
                case "4":
                    for v in get_subscription():
                        print(v)
                    print("-----------------------")
                    input(">")      
                
                case "5":
                    type=input("Entrez le type :")
                    price=input("Entre le prix :")
                    duree=input("Entre la durée en semaine :")
                    id=create_subscription(type, price, duree)
                    print(f"The new subscription has already been created {id}")              
                    input(">")  
                case "6":
                    print("-----------------------")
                    for v in get_subscription():
                        print(v)
                    print("-----------------------")
                    id = input("Entrez l'id de la subscription à supprimer : ")
                    rows_count = delete_subscription(id)
                    print(f"{rows_count} lignes modifié")
                    input(">")
                    
                case "7":
                    for v in get_training():
                        print(v)
                    print("-----------------------")
                    input(">")          
                    
                case "8":
                    for v in get_coach():
                        print(v)
                    print("-----------------------")
                    coach = input("Coach choisi ID: > ")
                    description=input("Entrez la description :")
                    hour_start=input("Entre l'heure de départ :").zfill(2)                                   
                    min_start=input("Entre les min de départ :").zfill(2)                                   
                    hour_end=input("Entre l'heure de fin :").zfill(2)                                   
                    min_end=input("Entre les min de fin :").zfill(2)                                   
                    
                    day=input("Entre la journée (0: dimanche,...) :")
                    input(">")                 
                    id=create_training(description, hour_start+':'+min_start, hour_end+':'+min_end, day, coach)
                    print(f"The new subscription has already been created {id}")              
                    input(">") 
                    
                case "9":
                    print("-----------------------")
                    for v in get_training():
                        print(v)
                    print("-----------------------")
                    id = input("Entrez l'id de la subscription à supprimer : ")
                    rows_count = delete_training(id)
                    print(f"{rows_count} lignes modifié")
                    input(">")     
                    
                case "10":
                    for v in get_followcourse():
                        print(v)
                    print("-----------------------")
                    input(">")                                                                
                                    
                                        
                case "q":
                    continue_app = False
            
    db.close()
    