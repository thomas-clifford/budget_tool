def create_transactions_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Transactions (
            id INTEGER PRIMARY KEY,
            date TEXT,
            description TEXT,
            amount REAL,
            credit_or_debit TEXT,
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES Users(id)
        )
    ''')

def get_user_transactions(cursor, user_id):
    cursor.execute("SELECT * FROM Transactions WHERE user_id=?", (user_id,))
    return cursor.fetchall()

def transaction_exists(cursor, row, user_id):
    cursor.execute("SELECT * FROM Transactions WHERE date=? AND description=? AND amount=? AND user_id=?", 
                   (row['Date'], row['Description'], row['Amount'], user_id))
    return len(cursor.fetchall()) > 0
    

def add_transaction_to_table(cursor, row, credit_or_debit, user_id):
    cursor.execute('''
                INSERT INTO Transactions (date, description, amount, credit_or_debit, user_id)
                VALUES (?, ?, ?, ?, ?)
            ''', (row['Date'], row['Description'], row['Amount'], credit_or_debit, user_id))
    return cursor.lastrowid

