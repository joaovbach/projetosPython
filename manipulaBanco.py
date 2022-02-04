from pickle import FALSE
import sqlite3
import random
from datetime import date


banco = sqlite3.connect("banco.db")
cursor = banco.cursor()

def criaTabela(nome,colunas):
    column = ",".join(colunas)
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {nome}({column})")


def retornaUmExternalIdInexistente():
    ids = cursor.execute("SELECT externalId FROM valores").fetchall()
    external = random.randint(2,100)
    if len(ids) == 0:
        cursor.execute(f"INSERT INTO valores VALUES(1,{external},1/1/1)")
        banco.commit()

    else:
        jaTem = True
        while jaTem == True:
            externalid = random.randint(2,100)
            allExternals = []

            for i in ids:
                allExternals.append(i[0])
            

            if externalid in allExternals:
                #print(f"o external id:{externalid} ja existe")
                jaTem=True
            else:
                #print(f"o external id: {externalid} nao existe no banco")
                cursor.execute(f"INSERT INTO valores VALUES(1,{externalid},1/1/1)")
                banco.commit()
                jaTem=False
                return externalid
    
def getDataValida(incremento):
    dia = date.today().strftime("%d")
    mes = date.today().strftime("%m")
    ano = date.today().strftime("%Y")
    
    


#criaTabela("valores",["indice","externalId","dataDeCriacao"])
#print(retornaUmExternalIdInexistente())
getDataValida(0)