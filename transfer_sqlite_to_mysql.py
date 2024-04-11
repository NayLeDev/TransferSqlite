import sqlite3
import pymysql
import time
import os

def typing_input(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.050)  
    try:
        user_input = input()
        return user_input
    except KeyboardInterrupt:
        return None


sqlite_filename = typing_input("Entrez le nom du fichier de la base de données SQLite : ")
if not sqlite_filename:
    print("Opération annulée.")
    exit()
if not os.path.exists(sqlite_filename):
    print("Le fichier SQLite spécifié n'existe pas.")
    exit()
try:
    sqlite_conn = sqlite3.connect(sqlite_filename)
    sqlite_cursor = sqlite_conn.cursor()
except sqlite3.Error:
    print("Connexion impossible à la base de données SQLite.")
    exit()


try:
    mysql_conn = pymysql.connect(
        host='idk.com',
        port=3306,
        user='u57_naygithub',
        password='naypassword',
        database='database'  # replace with your database informations
    )
    mysql_cursor = mysql_conn.cursor()
except pymysql.MySQLError:
    print("Connexion impossible.")
    exit()

sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = sqlite_cursor.fetchall()

for table in tables:
    table_name = table[0]
    print(f"Création de la table MySQL '{table_name}'...")
    sqlite_cursor.execute(f"SELECT * FROM {table_name}")
    rows = sqlite_cursor.fetchall()

    mysql_cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
    create_table_query = f"CREATE TABLE {table_name} ("
    sqlite_cursor.execute(f"PRAGMA table_info({table_name})")
    columns_info = sqlite_cursor.fetchall()
    for column_info in columns_info:
        column_name = column_info[1]
        column_type = column_info[2]
        create_table_query += f"{column_name} {column_type}, "
    create_table_query = create_table_query[:-2] + ");"
    mysql_cursor.execute(create_table_query)
    print(f"Table '{table_name}' créée avec succès.")

    print(f"Insertion des données dans la table '{table_name}'...")
    for row in rows:
        placeholders = ', '.join(['%s'] * len(row))
        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        mysql_cursor.execute(insert_query, row)
    print(f"Données insérées dans la table '{table_name}'.")

mysql_conn.commit()

sqlite_conn.close()
mysql_conn.close()
print("Le transfert de données de SQLite vers MySQL est terminé.")
