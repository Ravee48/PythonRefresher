
users = [
    (0, 'Bob', 'Password'),
    (1, 'Rohan', 'awesome!213'),
    (2, 'Ravi', 'creative@321'),
    (3, 'Rahul', 'roman@321'),
]

username_mapping = {user[1]: user for user in users}

username_input = input('Enter user name : ')
userpassword_input = input('Enter user password : ')

_, name, password = username_mapping[username_input]

if userpassword_input == password:
    print('User do exists in the database :')
else:
    print('Invalid Username or Password : ')


