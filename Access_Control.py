class Admin: # only one with password access
    def __init__(self, email, username, __password):
        self.access_level = "Admin"
        self.email = email
        self.username = username
        self.__password = __password

    def display_details(self, email, username):
            print(f"email: {self.email}"),
            print(f"username: {self.username}"),
            print(f"access_level: {self.access_level}")
        

    def login(self, email, username, __password):
            self.username = input("username: ") ,
            self.__password = input("password: ")
        

class Engineer(Admin): # Email & username access
    def __init__(self, email, username, __password):
        super().__init__(email, username, __password)
        self.access_level = "Engineer"

    def display_details(self, email, username):
        return super().display_details(email, username)
    
    def login(self, email, username, __password):
        return super().login(email, username, __password)
    


class User(Engineer): # No password access
    def __init__(self, email, username, __password):
        super().__init__(email, username, __password)
        self.access_level = "User"

    def display_details(self, email, username):
        return super().display_details(email, username)
    
    def login(self, email, username, __password):
        return super().login(email, username, __password)
    
u1 = User("someemail", "someusername", "somepassword")
u1.display_details()