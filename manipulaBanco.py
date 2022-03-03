import sqlite3
import random
from datetime import date

banco = sqlite3.connect("banco.db")
cursor = banco.cursor()

def criaTabela(nome, colunas):
    column = ",".join(colunas)
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {nome}({column})")
    banco.commit()


def retornaUmExternalIdInexistente():
    ids = cursor.execute("SELECT externalId FROM valores").fetchall()
    external = random.randint(2,100)
    if len(ids) == 0:
        cursor.execute(f"INSERT INTO valores VALUES(1,{external},1/1/1)")
        banco.commit()

    else:
        jaTem = True
        while jaTem == True:
            externalid = random.randint(2,10000)
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
    dia = int(date.today().strftime("%d"))
    mes = int(date.today().strftime("%m"))
    ano = int(date.today().strftime("%Y"))

    diaFinal = ""
    mesFinal = ""

    dia += incremento

    if dia>30:
        dia = 1
        mes+=1

    if dia<10:
        diaFinal = "0"+str(dia)
    else:
        diaFinal = str(dia)

    if mes<10:
        mesFinal = "0"+str(mes)
    else:
        mesFinal = str(mes)
    
    return str(str(diaFinal) + "/" + str(mesFinal) + "/" + str(ano) + " " + "20:00_")

