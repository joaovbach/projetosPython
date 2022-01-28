import sqlite3

banco = sqlite3.connect("banco.db")
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS ids (internalId, externalId)")
cursor.execute("INSERT INTO ids (internalId, externalId) VALUES (1,2)")
banco.commit()

teste = cursor.execute("SELECT * FROM ids").fetchall()
print(teste)
