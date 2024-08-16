import csv
from datetime import datetime
from transactions import *
from category import *
from sub_categories import *
from monthly_summaries import *

new_month_years = []

# Function to update the database from CSV
# TODO: Change parse functionality based on the bank. I suspect their CSVs will be formatted differently
def update_database_with_csv(cursor, filename, bank, user_id):
    with open(filename, newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # Get the month and year from the date row. We will update this table in the DB
            date = datetime.strptime(row['Date'], "%Y-%m-%d")
            # TODO: Ignoring future statements until I figure out what I want to do with them
            if date > datetime.now():
                continue
            
            
            
            # TODO: This is not how we handle debit vs credit. Determine the correct workaround
            debit_or_credit = "debit"
            if bank == "chase":
                debit_or_credit = "credit"
            
            # If the transaction already exists in the database, skip it.
            if transaction_exists(cursor, row, user_id):
                continue
            
            # Add transaction to db
            add_transaction_to_table(cursor, row, debit_or_credit, user_id)
            # Create monthly summary entry if one does not exist for the month
            add_monthly_summary(cursor, row['Date'], user_id)
            
            # Allow the user to determine the categories
            main_cat, sub_cat = change_category(cursor, row)
            monthly_summary_id = get_monthly_summary_id(cursor, row['Date'])
            add_category_to_table(cursor, main_cat, monthly_summary_id)
            add_subcategory_to_table(cursor, sub_cat, row['Amount'], monthly_summary_id, main_cat)
            




