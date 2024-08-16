def create_category_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Categories (
            id INTEGER PRIMARY KEY,
            name TEXT,
            sub_categories TEXT,
            month_summary_id INTEGER,
            FOREIGN KEY(month_summary_id) REFERENCES MonthlySummaries(id)
        )
    ''')

def add_category_to_table(cursor, main_cat, month_summary_id):
    cursor.execute('''
                INSERT INTO Categories (name, sub_categories, month_summary_id)
                VALUES (?, ?, ?)
            ''', (main_cat, "", month_summary_id))
    return cursor.lastrowid