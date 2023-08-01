import sqlite3

connection = sqlite3.connect("GVNZO_Food.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        First_name TEXT,
        Last_name TEXT,
        Username TEXT,
        ID INTEGER,
        Phone_number INTEGER
);
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS address (
        ID INTEGER,
        Address_longitude FLOAT,
        Address_latitude FLOAT
);
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        ID INTEGER,
        Title TEXT,
        Address_destination TEXT,
        Date_time_order TEXT
);
""")
