class manager: 
    def load_user():
        pass

    def save_user():
        pass

    def validate_username():
        pass
    
    def validate_password():
        pass

    def login(self):
        pass

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
    

