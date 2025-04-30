import sqlite3

conn = sqlite3.connect("main.db")
cur = conn.cursor()

## SQL ##############################
def create_table_sql():
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS expense (
                id  INTEGER PRIMARY KEY,
                name    TEXT    NOT NULL,
                amount  INTEGER NOT NULL,
                description TEXT,
                category TEXT,
                date TEXT NOT NULL
    )""")

def get_expenses_byid_sql(expense_id):
    """get expense by id

    Args:
        expense_id (int): expense id

    Returns:
        list: return one item
    """
    cur.execute("SELECT * FROM expense WHERE id = ?", (expense_id, ))
    return cur.fetchone()

def get_expenses_bycategory_sql(expense_category):
    """get expenses by category

    Args:
        expense_category (str): expense category

    Returns:
        list: all the expense in a list
    """
    cur.execute("SELECT * FROM expense WHERE category = ?", (expense_category, ))
    return cur.fetchall()

def get_expenses_sql():
    """Get all expenses

    Returns:
        list: all expenses in a list
    """
    cur.execute("SELECT * FROM expense")
    return cur.fetchall()

def add_expense_sql(expense_id:int, expense_name:str, expense_amount:int, expense_desc:str, expense_category:str, expense_date:str):
    """add an expense item

    Args:
        expense_id (int): the expense id
        expense_name (str): expense name
        expense_amount (int): amount of expense
        expense_desc (str): expense description (optional)
        expense_category (str): category ex: primary, secondary, foods, bills
        expense_date (str): date of the expense
    """
    cur.execute("INSERT INTO expense (id, name, amount, description, category, date) VALUES (?, ?, ?, ?, ?, ?)", (expense_id, expense_name, expense_amount, expense_desc, expense_category, expense_date))
    conn.commit()

def remove_expense_sql(expense_id):
    """remove an expense with a given id

    Args:
        expense_id (int): expense id
    """
    cur.execute("DELETE FROM expense WHERE id = ?", (expense_id, ))
    conn.commit()

def update_expense_sql(expense_id, expense_name, expense_amount, expense_desc, expense_category, expense_date):
    cur.execute("""UPDATE expense
                SET id = ?, name = ?, amount = ?, description = ?, category = ?, date = ?
                WHERE id = ?""", (expense_id, expense_name, expense_amount, expense_desc, expense_category, expense_date, expense_id))
