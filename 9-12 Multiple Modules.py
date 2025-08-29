from Module_User import User, Admin

user1 = User('John', 'Doe', gender='male', age=22, privilege='create post')
admin = Admin(first_name='Sumiet', last_name='Talekar', privilege='add user')

user1.privilege.add_privilege('create page')
admin.privilege.add_privilege('delete user')

user1.show_user_privileges()
print()
admin.show_user_privileges()