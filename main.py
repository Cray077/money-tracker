import sqlite3
import datetime


## VARIABLES ########################
conn = sqlite3.connect("main.db")
cur = conn.cursor()

## SQL ##############################
def create_table():
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS expense (
                id  INTEGER PRIMARY KEY,
                name    TEXT    NOT NULL,
                amount  INTEGER NOT NULL,
                description TEXT,
                category TEXT,
                date TEXT NOT NULL
    )""")

def get_expenses_byid(expense_id):
    """get expense by id

    Args:
        expense_id (int): expense id

    Returns:
        list: return one item
    """
    cur.execute("SELECT * FROM expense WHERE id = ?", (expense_id, ))
    return cur.fetchone()

def get_expenses_bycategory(expense_category):
    """get expenses by category

    Args:
        expense_category (str): expense category

    Returns:
        list: all the expense in a list
    """
    cur.execute("SELECT * FROM expense WHERE category = ?", (expense_category, ))
    return cur.fetchall()

def get_expenses():
    """Get all expenses

    Returns:
        list: all expenses in a list
    """
    cur.execute("SELECT * FROM expense")
    return cur.fetchall()

def add_expense(expense_id, expense_name, expense_amount, expense_desc, expense_category):
    """add an expense item

    Args:
        expense_id (int): the expense id
        expense_name (str): expense name
        expense_amount (amount): amount of expense
        expense_desc (str): expense description (optional)
        expense_category (str): category ex: primary, secondary, foods, bills
    """
    current_date = datetime.datetime.now()
    cur.execute("INSERT INTO expense (id, name, amount, description, category, date) VALUES (?, ?, ?, ?, ?, ?)", (expense_id, expense_name, expense_amount, expense_desc, expense_category, current_date))
    conn.commit()

def remove_expense(expense_id):
    """remove an expense with a given id

    Args:
        expense_id (int): expense id
    """
    cur.execute("DELETE FROM expense WHERE id = ?", (expense_id, ))
    conn.commit()

def update_expense(expense_id, expense_name, expense_amount, expense_desc, expense_category):

    current_date = datetime.datetime.now()
    
    cur.execute("""UPDATE expense
                SET id = ?, name = ?, amount = ?, description = ?, category = ?, date = ?
                WHERE id = ?""", (expense_id, expense_name, expense_amount, expense_desc, expense_category, current_date, expense_id))

## FUNCTIONS ########################

def print_in_list(ls:list):
    for x in ls:
        print(x)

## INTERFACE ########################


## MAINLOOP #########################
def main():
    create_table()
    # add_expense(3, "oil change", 50000, "", "needs", "5-3-2024")
    # add_expense(4, "electric bill", 100000, "", "needs", "5-3-2024")
    # add_expense(5, "pop ice", 5000, "", "wants", "9-3-2024")
    # add_expense(6, "tax", 10000, "", "needs", "11-3-2024")


    # print_in_list(get_expenses_full())

## MAINLOOP ##########################

if __name__ == "__main__":
    main()