import sql
import datetime

print(datetime.datetime.now())
sql.create_table_sql()

## FUNCTIONS ########################

def print_in_list(ls:list):
    for x in ls:
        print(x)

def add_expense(expense_name:str, expense_amount:int, expense_desc:str, expense_category:str, expense_date:str):
    
    sql.add_expense_sql()

def get_expenses():
    pass

def update_expense():
    pass

def delete_expense():
    pass

def backup_expenses_csv():
    pass

def backup_expenses_text():
    pass

def restore_expenses():
    pass


## MAINLOOP #########################
def mainloop():
    command = ""

    if command == "1": # Add expense
        pass

    elif command == "2": # Read expense / expense list
        pass
    elif command == "2": # Update expense
        pass
    elif command == "2": # Delete Expense
        pass
    elif command == "2": # Backup to csv or plaintext
        pass
    elif command == "2": # Restore backup
        pass
    else: 
        pass


## MAINLOOP-END ######################

if __name__ == "__main__":
    mainloop()