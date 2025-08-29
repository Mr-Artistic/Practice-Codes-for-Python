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