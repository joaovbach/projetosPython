import sqlite3

banco = sqlite3.connect("banco.db")
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS ids (internalId, externalId)")
#cursor.execute("INSERT INTO ids (internalId, externalId) VALUES (1,2)")
#banco.commit()

def getNotExistExternal(external):
	if verifiNotExist(external)  == False:
		valores = cursor.execute("SELECT * FROM ids").fetchall()
		ultimoInternal = 0
		if len(valores) == 0:
			ultimoInternal = 1
		else:
			ultimoInternal = valores[len(valores)-1][0]+1

		cursor.execute(f"INSERT INTO ids(internalId, externalId) VALUES ({ultimoInternal},{external})")
		banco.commit()
	else:
		print("external id ja existente")

def verifiNotExist(external):
	valores = cursor.execute("SELECT * FROM ids")
	exists = []
	for i in valores:
		exists.append(i[1])

	if external in exists:
		return True
	else:
		return False


while 1:
	print("1- add external   2- imprime lista")
	opcao = input("digite a opcao")
	
	if opcao == '1':
		external = input("digite o external")
		getNotExistExternal(int(external))
	elif opcao == '2':
		print(cursor.execute("SELECT * FROM ids").fetchall())

	elif opcao == '3':
		cursor.execute("DELETE FROM ids WHERE internalId = 14")	
		banco.commit()


#getNotExistExternal(12)

#teste = cursor.execute("SELECT * FROM ids").fetchall()
#print(teste)
