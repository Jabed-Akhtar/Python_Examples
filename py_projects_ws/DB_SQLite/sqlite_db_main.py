'''
# Data types in sqlite (only 5): NULL, INTEGER, REAL, TEXT, BLOB
# Primary key: rowid (cursor.execute("SELECT rowid, * FROM customers"))
# Where clause: cursor.execute("SELECT * FROM customers WHERE last_name LIKE 'La%'")
# Update records
'''

import sqlite3

#conn = sqlite3.connect(':memory:')      # to store data in database -> data won't be saved to any db file
conn = sqlite3.connect('customer.db')

# Create cursor
cursor = conn.cursor()

# Create a table
''' Done once
cursor.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    email text
)
""")
'''

# Inserting one value to the table
#cursor.execute("INSERT INTO customers VALUES ('Zaxx', 'Uni', 'zxx.uni@email.com')")

# Inserting one value to the table
#many_customers = [('West', 'Prasad', 'west.brown@email.com'), ('Bhanu', 'Man', 'bhanu.man11@email.com'), ('Sri', 'Lama', 'srilama@email.com')]
#cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)

# Query the db
cursor.execute("SELECT rowid, * FROM customers")
#print(cursor.fetchone()[0])
#cursor.fetchmany(2)
#print(cursor.fetchall())

items = cursor.fetchall()
#print(items)
print("Name" + "\t\t Email")
print("-----" + "\t\t ------")
for item in items:
    #print(item[0] + " " + item[1] + " \t " + item[2])
    print(item)

# where clause ===================================================
cursor.execute("SELECT * FROM customers WHERE last_name = 'Prasad'")
items = cursor.fetchall()
for item in items:
    print(item)

cursor.execute("SELECT * FROM customers WHERE last_name LIKE 'La%'")
items = cursor.fetchall()
for item in items:
    print(item)

# Update records ================================================
cursor.execute("""UPDATE customers SET last_name = 'Lamjung'
    WHERE first_name = 'Sri'
""")
conn.commit()
cursor.execute("SELECT * FROM customers")
items = cursor.fetchall()
for item in items:
    print(item)

# Commit our command
conn.commit()

# Close our connection
conn.close()
