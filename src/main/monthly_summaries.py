from datetime import datetime
from category_options import *
from sub_category_options import *

# TODO: Create the monthly summary table
def create_monthly_summary_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS MonthlySummaries (
            id INTEGER PRIMARY KEY,
            month TEXT,
            year TEXT,
            categories TEXT,
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES Users(id)
        )
    ''')

def add_monthly_summary(cursor, date, user_id):
    date_cap = datetime.strptime(date, "%Y-%m-%d")
    month = date_cap.strftime("%B")
    year = date_cap.year
    if not month_exists(cursor, month, year):
        cursor.execute('''
                    INSERT INTO MonthlySummaries (month, year, user_id)
                    VALUES (?, ?, ?)
                ''', (month, year, user_id))
        # TODO: Allow the user to create a template of categories.
        # This keeps the user from having to recreate the same categories each time a new month begins.
        monthly_summary_id = get_monthly_summary_id(cursor, date)
        create_default_category_options(cursor, monthly_summary_id)
        default_category_ids = get_category_option_ids(cursor, monthly_summary_id)
        for id in default_category_ids:
            create_default_sub_category_options(cursor, id)
        return True
    return False    

def month_exists(cursor, month, year):
    cursor.execute("SELECT count(*) FROM MonthlySummaries WHERE month=? AND year=?", (month, year))
    data = cursor.fetchone()[0]
    if data == 0:
        return False
    return True
    
def get_user_monthly_summaries(cursor, user_id):
    cursor.execute("SELECT * FROM MonthlySummaries WHERE user_id=?", (user_id,))
    return cursor.fetchall()

def get_monthly_summary_id(cursor, date):
    date_cap = datetime.strptime(date, "%Y-%m-%d")
    month = date_cap.strftime("%B")
    year = date_cap.year
    cursor.execute("SELECT * FROM MonthlySummaries WHERE month=? AND year=?", (month, year))
    data = cursor.fetchone()
    if data:
        return data[0]
    return None
    
# TODO: Get monthly summary table data
def get_monthly_summary_data(cursor, table_name):
    return

def get_sub_categories(cursor, table_name):
    return

# TODO: These categories should come from the options tables
def change_category(cursor, row):
    print("Date:", row['Date'])
    print("Description:", row['Description'])
    print("Original Description:", row['Original Description'])
    print("Category:", row['Category'])
    print("Amount:", row['Amount'])
    print("Status:", row['Status'])
    
    monthly_summary_id = get_monthly_summary_id(cursor, row['Date'])
    categories = get_category_option_names(cursor, monthly_summary_id)
    
    print("What category should this transaction go under?")
    i=1
    for category in categories:
        print(category[0], i)
        i+=1
    choice = input("***NEW CATEGORY*** (0): ")
    if choice == '0':
        # TODO: Implement method
        name = input("What is the name of the new category?: ")
        main_cat = create_new_category_option(cursor, name, monthly_summary_id)
    else:
        main_cat = categories[int(choice)-1][0]
    
    category_id = get_category_option_id(cursor, main_cat, monthly_summary_id)
    sub_categories = get_sub_category_option_names(cursor, category_id)
    i=1
    for category in sub_categories:
        print(category[0], i)
        i+=1
    choice = input("***NEW CATEGORY*** (0): ")
    if choice == '0':
        # TODO: Implement method
        name = input("What is the name of the new category?: ")
        sub_cat = create_new_sub_category_option(cursor, name, category_id)
    else:
        sub_cat = sub_categories[int(choice)-1][0]
    return main_cat, sub_cat
    