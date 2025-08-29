class User:
    def __init__(self, first_name, last_name, **kwargs):
        """Initializes a user object and stores data."""
        self.first_name = first_name
        self.last_name = last_name
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



user1 = User('John', 'Doe', gender='male', age=22)
user2 = User('Abraham', 'Lincoln', gender='male', age=82)
user3 = User('Aishwarya', 'Rai', gender='female', age=44, phone_number='555-1212', email='aishu@dummy.com')

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()
