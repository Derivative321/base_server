import openpyxl

user_database_file = openpyxl.load_workbook("user_data_base.xlsx")
user_database = user_database_file["Sheet1"]
database_next_row = user_database.max_row + 1

USERNAME_COLUMN = 1
EMAIL_COLUMN = 2
PASSWORD_COLUMN = 3
PERMISSIONS_COLUMN = 4
USER_ID_COLUMN = 5
