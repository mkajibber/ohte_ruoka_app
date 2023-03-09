
import os
import sqlite3

dirname = os.path.dirname(__file__)

# connection = sqlite3.connect(os.path.join(dirname, "..", "data", "database.sqlite"))
# connection.row_factory = sqlite3.Row
path = os.path.join(dirname, "..", "data", "database.sqlite")
print()
print()
print()
print(path)
print()
print()
print()

def get_database_connection():
    pass
    # return connection
