# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 13:39:23 2022

@author: uif25757
"""

import sqlite3

conn = sqlite3.connect('employees.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
#         first text,
#         last text,
#         pay integer
#         )""")

# c.execute("INSERT INTO employees VALUES ('Jab', 'Akh', 5000)")

c.execute("SELECT * FROM employees WHERE last='Akh'")

print(c.fetchone())

conn.commit()

conn.close()