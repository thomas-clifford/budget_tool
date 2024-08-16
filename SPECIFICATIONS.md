# What?

The automatic budgeting tool is a tool that accepts exported, csv bank statements and outputs the budgeting data for the month. It should be able to display data through infographics as well.

# Who?

USAA, Chase, and Discover [users] will be the first supported formats since that's what I have direct access to.

# How?

I'll use a Python csv parser to grab the data from the exported bank file. I'll have a folder for each type of bank. This way, the python parser can decide how to parse it. Then, the user will be prompted to determine what each transaction should be categorized. They should be able to add to existing categories, or create new ones. Finally, the data will be placed in a bank_data database. The process should also be able to handle duplicate data. This database should have tables for users, monthly transactions, and monthly summaries. An eventual goal will be to have a GUI for the user to interact with (login, upload csv files, determine categories, and view data)