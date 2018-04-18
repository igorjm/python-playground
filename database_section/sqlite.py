import sqlite3

def create_table():
    connection = sqlite3.connect('lite.db')
    cur = connection.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')

    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = sqlite3.connect('lite.db')
    cur = connection.cursor()

    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))

    connection.commit()
    connection.close()

# insert("Coffe Cup", 6, 1.0)

def view():
    connection = sqlite3.connect('lite.db')
    cur = connection.cursor()

    cur.execute("SELECT * FROM store")

    rows = cur.fetchall()
    connection.close()
    return rows

def delete(item):
    connection = sqlite3.connect('lite.db')
    cur = connection.cursor()

    cur.execute("DELETE FROM store WHERE item=?", (item,))

    connection.commit()
    connection.close()

def update(quantity, price, item):
    connection = sqlite3.connect('lite.db')
    cur = connection.cursor()

    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))

    connection.commit()
    connection.close()

update(11, 6, "Water Glass")
# delete('Wine glass')
print(view())