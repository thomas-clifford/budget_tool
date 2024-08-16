def create_sub_category_option_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SubCategoryOptions (
            id INTEGER PRIMARY KEY,
            name TEXT,
            parent_option_id INTEGER,
            FOREIGN KEY(parent_option_id) REFERENCES CategoryOptions(id)
        )
    ''')
    
def create_default_sub_category_options(cursor, parent_option_id):
    default_options = ["option1",
                   "option2",
                   "option3"]
    for option in default_options:
        cursor.execute('''
                    INSERT INTO SubCategoryOptions (name, parent_option_id)
                    VALUES (?, ?)
                ''', (option, parent_option_id))

def create_new_sub_category_option(cursor, name, parent_option_id):
    cursor.execute('''
                    INSERT INTO SubCategoryOptions (name, parent_option_id)
                    VALUES (?, ?)
                ''', (name, parent_option_id))
    
def get_sub_category_option_names(cursor, parent_option_id):
    cursor.execute("SELECT name FROM SubCategoryOptions WHERE parent_option_id=?", (parent_option_id,))
    return cursor.fetchall()