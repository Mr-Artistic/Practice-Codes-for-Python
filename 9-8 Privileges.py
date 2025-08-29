class Privileges:

    def __init__(self, privileges):
        """Initializes Privileges List and stores privileges."""
        self.privileges = [privileges]

    def add_privilege(self, privilege):
        """Adds a privilege to the user."""
        self.privileges.append(privilege)

    def show_privileges(self):
        """Shows the privileges list."""
        print(f"{self.privileges}")

class User:

    def __init__(self, first_name, last_name, privilege, **kwargs):
        """Initializes a user object and stores data."""
        self.first_name = first_name
        self.last_name = last_name
        self.privilege = Privileges(privilege)
        self.gender = kwargs.get('gender')
        self.age = kwargs.get('age')
        self.email = kwargs.get('email')
        self.phone_number = kwargs.get('phone_number')

    def describe_user(self):
        """Describes the user details."""
        print(f"My first name is {self.first_name}")
        print(f"My last name is {self.last_name}")
        if self.gender is not None:
            print(f"I am a {self.gender}")
        if self.age is not None:
            print(f"My age is {self.age}")
        if self.email is not None:
            print(f"My email is {self.email}")
        if self.phone_number is not None:
            print(f"My phone number is {self.phone_number}")
        print()

    def greet_user(self):
        """Greets the user."""
        print(f"Hi {self.first_name} {self.last_name}! Welcome back!")

    def show_user_privileges(self):
        """Shows user privilege(s)."""
        print(f"The user {self.first_name} {self.last_name} has these privileges:")
        self.privilege.show_privileges()

class Admin(User):

    def __init__(self, first_name, last_name, privilege, **kwargs):
        """Initializes an Admin object and stores data."""
        super().__init__(first_name, last_name, privilege, **kwargs)

user1 = User('John', 'Doe', gender='male', age=22, privilege='create post')
admin = Admin(first_name='Sumiet', last_name='Talekar', privilege='add user')

user1.privilege.add_privilege('create page')
admin.privilege.add_privilege('delete user')

user1.show_user_privileges()
print()
admin.show_user_privileges()