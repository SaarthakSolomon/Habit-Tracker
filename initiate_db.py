import questionary
import sqlite3
import hashlib
import User

def launch_db():
    from os.path import abspath, dirname, join
    db_path = join(dirname(abspath(__file__)),'main_db.db')

    connection = sqlite3.connect(db_path)
    c = connection.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS users ( firstname text, lastname text, username text PRIMARY KEY, password text)")
    c.execute("CREATE TABLE IF NOT EXISTS habits ( habit_name text, owner text, category text, periodicity text, datetime_of_creation datetime)")
    c.execute("CREATE TABLE IF NOT EXISTS progress ( habit_name text, periodicity text, owner text, datetime_of_completion datetime)")

    connection.commit()
    connection.close()

def register_user():
    firstname = questionary.text("What is your first name?",
                                 validate= lambda text: True if len(text)>0 and text.isalpha() else "Please enter a First Name using only letters.").ask()
    lastname = questionary.text("What is your last name?",
                                 validate= lambda text: True if len(text)>0 and text.isalpha() else "Please enter a Last Name using only letters.").ask()
    username = questionary.text("Username",
                                validate= lambda text: True if len(text)>0 and text.isalnum() else "Please enter a username with only alphanumeric characters.").ask()
    password = questionary.password('Password',
                                    validate = lambda text: True if len(text) >= 4 and text.isalnum() else "Your password must be atleast 4 characters long.").ask()
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    new_user = User.UserClass(firstname, lastname, username, password)
    user = get_user(username)
    if user:
        print("\nUsername not available. Try another.")
        register_user()
    else:
        new_user.store_in_db()
        print("\nRegistration Successful!\n")

def get_user(username):
    from os.path import abspath, dirname, join
    db_path = join(dirname(abspath(__file__)),'main_db.db')

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    list_of_users = cursor.fetchall()

    if len(list_of_users) > 0:
        firstname, lastname, username, password = list_of_users[0]
        user = User.UserClass(firstname, lastname, username , password)
        return user
    else:
        return None
    
def login():
    user_name = questionary.text("Enter your username: ").ask()
    user = get_user(user_name)
    if user:
        check_password(user.password)
        return user
    else:
        print("\nInvalid username.\n")
        login()

def check_password(password):
    password_input = questionary.password("Enter your password: ").ask()
    password_input = hashlib.sha256(password_input.encode('utf-8')).hexdigest()
    if password_input == password:
        print("\nLogin successful!\n")
    else:
        print("\nPassword incorrect. Try again!\n")
        check_password(password)