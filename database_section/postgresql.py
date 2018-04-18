import psycopg2

def create_table():
    connection = psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur = connection.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')

    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur = connection.cursor()

    # cur.execute("INSERT INTO store VALUES ('%s', '%', '%')" % (item, quantity, price)) -- Works too
    cur.execute("INSERT INTO store VALUES (%s, %s', %s)", (item, quantity, price))

    connection.commit()
    connection.close()

def view():
    connection = psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur = connection.cursor()

    cur.execute("SELECT * FROM store")

    rows = cur.fetchall()
    connection.close()
    return rows

def delete(item):
    connection = psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur = connection.cursor()

    cur.execute("DELETE FROM store WHERE item=%s", (item,))

    connection.commit()
    connection.close()

def update(quantity, price, item):
    connection = psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur = connection.cursor()

    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))

    connection.commit()
    connection.close()

# create_table()
# insert("Apple", 10, 0.5)
# update(11, 6, "Water Glass")
# delete('Wine glass')
# print(view())