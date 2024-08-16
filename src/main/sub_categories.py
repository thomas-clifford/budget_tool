def create_sub_category_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SubCategories (
            id INTEGER PRIMARY KEY,
            name TEXT,
            amount REAL,
            monthly_summary_id INTEGER,
            parent_category_name TEXT,
            FOREIGN KEY(monthly_summary_id) REFERENCES MonthlySummary(id),
            FOREIGN KEY(parent_category_name) REFERENCES Categories(name)
        )
    ''')
    
def add_subcategory_to_table(cursor, sub_cat, amount, monthly_summary_id, parent_category_name):
    cursor.execute('''
                INSERT INTO SubCategories (name, amount, monthly_summary_id, parent_category_name)
                VALUES (?, ?, ?, ?)
            ''', (sub_cat, amount, monthly_summary_id, parent_category_name))
    return cursor.lastrowid