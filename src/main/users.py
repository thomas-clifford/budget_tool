import sqlite3

def create_user_db(cursor):
    # Check if the table exists, if not, create it
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                        id INTEGER PRIMARY KEY,
                        username TEXT,
                        password TEXT
                        transactions TEXT
                    )''')

def login(cursor, username, password):
    cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    user = cursor.fetchone()
    if not user:
        print("User with that username doesn't exist. Please try again.")
        username = input("Enter username: ")
        password = input("Enter password: ")
        login(cursor, username, password)

    if user:
        if user[2] == password:
            print("Login successful.")
        else:
            print("Invalid password. Please try again.")
            username = input("Enter username: ")
            password = input("Enter password: ")
            login(cursor, username, password)


def user_exists(cursor, username):
    # Check if the username already exists
    cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    existing_user = cursor.fetchone()
    if existing_user:
        return True
    return False

def get_user_id(cursor, username):
    cursor.execute("SELECT id FROM Users WHERE username=?", (username,))
    return cursor.fetchone()[0]

# Function to create a user in the database
def create_user(cursor, username, password):
    # Insert the new user into the database
    if user_exists(cursor, username):
        print("User with that username already exists. Please use another one or login.")
        return
    cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
    print("User created successfully.")
