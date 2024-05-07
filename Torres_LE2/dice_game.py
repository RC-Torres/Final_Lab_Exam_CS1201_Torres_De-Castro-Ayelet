import random
import os



class Dicegame:
    def register(self):
        while True:
            try:
                username = input("Enter a username or leave blank to exit: ")
                password = input("Enter a password or leave blank to exit: ")
                if len(password) < 8:
                    print ("password must be at least 8 characters long")
                else:
                    print ("Account successfully registered")
                if len(username) < 4:
                    print ("Username must be at least 4 characters long")
                else:
                    print ("Account successfully registered")
            except ValueError:
                print ("invalid input")

    def load_scores():
        pass

    def save_scores():
        pass

    def play_game():
        print("1. Start Game")
        print("2. Top Scores")
        print("3. Log Out")

        choice = int(input("Enter the number of your choice: "))
        
        while True:
            if choice == 1:
                cpu_points = 0
                self.points = 0
                
                choice = input("Enter 'a' to play: ")

                if choice.lower == 'a':
                    user_choice = random.randint(1, 6)
                    CPU_choice = random.randint (1,6)

                    if CPU_choice < user_choice:
                        print("You win!")
                        self.points += 1
                    elif CPU_choice > user_choice:
                        print("You Lose!")
                        cpu_points += 1
                    elif CPU_choice == user_choice:
                        print("It's a tie!")

    def show_top_scores():s
        pass

    def logout():
        pass

    def menu():
        print("Welcome to Dice Game!")
        print("1. Register")
        print("2. Log in")
        print("3. Exit")

        choice = int(input("Enter the number of your choice: "))

        while True:
            if choice == 1:
                register()
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            else:
                print("Invalid input. Try Again.")

    

