def create_category_option_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CategoryOptions (
            id INTEGER PRIMARY KEY,
            name TEXT,
            month_summary_id INTEGER,
            FOREIGN KEY(month_summary_id) REFERENCES MonthlySummaries(id)
        )
    ''')

def create_default_category_options(cursor, month_summary_id):
    # TODO: This should not be hard coded. The user should be allowed to choose this
    default_options = ["Housing",
                   "Transportation",
                   "Insurance",
                   "Food",
                   "Pets",
                   "Personal Care",
                   "Entertainment",
                   "Loans",
                   "Savings or Investments",
                   "Gifts or Donations"]
    for option in default_options:
        cursor.execute('''
                    INSERT INTO CategoryOptions (name, month_summary_id)
                    VALUES (?, ?)
                ''', (option, month_summary_id))

def create_new_category_option(cursor, name, monthly_summary_id):
    cursor.execute('''
                    INSERT INTO CategoryOptions (name, month_summary_id)
                    VALUES (?, ?)
                ''', (name, monthly_summary_id))

def get_category_option_names(cursor, month_summary_id):
    cursor.execute("SELECT name FROM CategoryOptions WHERE month_summary_id=?", (month_summary_id,))
    return cursor.fetchall()
    
def get_category_option_ids(cursor, month_summary_id):
    cursor.execute("SELECT id FROM CategoryOptions WHERE month_summary_id=?", (month_summary_id,))
    return cursor.fetchall()[0]

def get_category_option_id(cursor, name, month_summary_id):
    cursor.execute("SELECT id FROM CategoryOptions WHERE name=? AND month_summary_id=?", (name, month_summary_id,))
    return cursor.fetchone()[0]