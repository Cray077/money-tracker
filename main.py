import sqlite3


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
    cur.execute("SELECT * FROM expense WHERE id = ?", (expense_id, ))
    return cur.fetchone()

def get_expenses_bycategory(expense_category):
    cur.execute("SELECT * FROM expense WHERE category = ?", (expense_category, ))
    return cur.fetchall()

def get_expenses_full():
    cur.execute("SELECT * FROM expense")
    return cur.fetchall()

def add_expense(expense_id, expense_name, expense_amount, expense_desc, expense_category, expense_date):
    cur.execute("INSERT INTO expense (id, name, amount, description, category, date) VALUES (?, ?, ?, ?, ?, ?)", (expense_id, expense_name, expense_amount, expense_desc, expense_category, expense_date))
    conn.commit()

def remove_expense(expense_id):
    cur.execute("")

def update_expense():
    pass

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


    print_in_list(get_expenses_full())

## MAINLOOP ##########################

if __name__ == "__main__":
    main()