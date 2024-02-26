import sqlite3


## VARIABLES ########################
conn = sqlite3.connect("main.db")
cur = conn.cursor()

## SQL ##############################
def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXIST expense (
                id  INTEGER PRIMARY KEY,
                name    TEXT    NOT NULL,
                amount  INTEGER NOT NULL,
                description TEXT
    )""")

def get_expenses():
    pass
def add_expense():
    pass

def remove_expense():
    pass

def update_expense():
    pass

## FUNCTIONS ########################

## INTERFACE ########################

def main():
    pass

## MAINLOOP ##########################

if __name__ == "__main__":
    main()