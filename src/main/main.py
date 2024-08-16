from users import *
from csv_parser import *
from monthly_summaries import *
from category import *
from sub_categories import *
from os import listdir, remove
from os.path import isfile, join
import os


def parse_csv_directories(path):
    return [f for f in listdir(path) if isfile(join(path, f))]
    
def create_tables(cursor):
    create_category_option_table(cursor)
    create_sub_category_option_table(cursor)
    create_transactions_table(cursor)
    create_monthly_summary_table(cursor)
    create_category_table(cursor)
    create_sub_category_table(cursor)
    

def main():
    bank_data_db = 'src/databases/bank_data.db'
    usaa_csv_path = 'src/csv-files/usaa/'
    chase_csv_path = 'src/csv-files/chase/'
    # TODO: Remove this line. Using it for testing
    os.remove(bank_data_db)

    
    conn = sqlite3.connect(bank_data_db) # Connect to user database
    cursor = conn.cursor()
    create_user_db(cursor) # Create the user table if it doesn't exist
    
    option = input("Login (1) or create a user (2): ")
    
    # TODO: Encrypt the passwords in the DB
    if option == '1':
        print("Logging in...")
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = login(cursor, username, password)
        
    else:
        print("Creating user. Please enter a username and password...")
        username = input("Enter username: ")
        password = input("Enter password: ")
        create_user(cursor, username, password)
    conn.commit()
    
    create_tables(cursor) # Create the tables if they don't exist

    # TODO: Grab the specific user's current bank transactions
    user_id = get_user_id(cursor, username)
    transactions = get_user_transactions(cursor, user_id)
    monthly_summaries = get_user_monthly_summaries(cursor, user_id)
    
    # Ask user what they want to do:
    option = ''
    while option != '3':
        option = input("Would you like to: input data (1), view data (2), exit (3): ")
        if option == '1':
            # TODO: Can we ask the user to confirm that the csv has been placed in the folder? The user also needs to be able to differentiate CSVs 
            # between debit and credit accounts. Debit accounts pay. Credit accounts get paid off. Maybe this can be done through user input which changes file names.
            print('Getting uploaded files...')
            usaa_files = parse_csv_directories(usaa_csv_path)
            chase_files = parse_csv_directories(chase_csv_path)
            # TODO separate the lists each into 2 separate lists of debit and credit. For now, we will hard code them
            usaa_debit_files = usaa_files
            usaa_credit_files = []
            chase_debit_files = []
            chase_credit_files = chase_files
            print('Reading the CSV files...')
            for usaa_debit_file in usaa_debit_files:
                update_database_with_csv(cursor, usaa_csv_path + usaa_debit_file, 'usaa', user_id)
            for usaa_credit_files in usaa_credit_files:
                update_database_with_csv(cursor, usaa_csv_path + usaa_credit_files, 'usaa', user_id)
            # for chase_debit_files in chase_debit_files:
            #     update_database_with_csv(cursor, chase_csv_path + chase_debit_files, 'chase', user_id)
            # for chase_credit_files in chase_credit_files:
            #     update_database_with_csv(cursor, chase_csv_path + chase_credit_files, 'chase', user_id)
            conn.commit()
        elif option == '2':
            # TODO: Implement a way to view the data.
            print('Stubbed')
        elif option != '3':
            print("Unknown option. Try again.")
    print("See ya!")
    
    # Close the connection to the database
    conn.close()
    
    
    
if __name__ == "__main__":
    main()