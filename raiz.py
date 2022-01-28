from acessabanco import pegaExternalId

ex = pegaExternalId()

while 1:
	print("1- adicionar um externalid no banco    2- imprimir os dados do banco de external id")
	opcao = input("digite sua opcao")
	if opcao == '1':
		id = input("digite o external id")
		ex.getNotExistExternal(int(id))
	elif opcao == '2':
		print(ex.imprimeBanco())
