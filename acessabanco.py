import sqlite3

#cursor.execute("INSERT INTO ids (internalId, externalId) VALUES (1,2)")
#banco.commit()
class pegaExternalId:
	banco = sqlite3.connect("banco.db")
	cursor = banco.cursor()

	def __init__(self):
		pass

	def getNotExistExternal(self, external):
		if verifiNotExist(external)  == False:
			valores = self.cursor.execute("SELECT * FROM ids").fetchall()
			ultimoInternal = 0
			if len(valores) == 0:
				ultimoInternal = 1
			else:
				ultimoInternal = valores[len(valores)-1][0]+1

			self.cursor.execute(f"INSERT INTO ids(internalId, externalId) VALUES ({ultimoInternal},{external})")
			self.banco.commit()
		else:
			print("external id ja existente")

	def verifiNotExist(self, external):
		valores = cursor.execute("SELECT * FROM ids")
		exists = []
		for i in valores:
			exists.append(i[1])

		if external in exists:
			return True
		else:
			return False

	def imprimeBanco(self):
		return self.cursor.execute("SELECT * FROM ids").fetchall()



#getNotExistExternal(12)

#teste = cursor.execute("SELECT * FROM ids").fetchall()
#print(teste)
