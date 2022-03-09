from cmath import log
import this
from playwright.sync_api import Playwright, sync_playwright
from demandasEotimizacao import criaDemanda
import manipulaBanco
from chat import chatEmMassa
import login
from demandasEotimizacao import geraOtimizacao
from chatGeral import ChatGeral
from demandaGeral import DemandaGeral
import time
from otimizaoGeral import OtimizacaoGeral
from aceitaRota import AceitaRota

###VARIAVEIS DO KWARGS####################################################################################################################################################################################

#playwright = biblioteca
#page = pagina do navegador
#idOtimizacao = usado para identificar a itimizacao na aba de "otimizacoes geradas"
#extDemanda = usado para identificar uma demanda para gerar uma otimizacao, para aprovar uma rota
#idDemanda = usado para alocar uma demanda manualmente, encerrar uma demanda
#listaExtIds = usado para gerar uma otimizacao, passa o extarnalId das demandas que devem ser otimizadas
#mensagem = texto que sera enviar em acoes do chat
#titulo = titulo da mensagem em massa

####################################################################################################################################################################################

chats = ChatGeral()
demandas = DemandaGeral(manipulaBanco)
otimizacao = OtimizacaoGeral()
aceitaRota = AceitaRota()

testeChats = [chats.encerraChat,chats.iniciaChat, chats.chatEmMassa]
acoesDemandas = [demandas.criaDemanada, demandas.alocaDemanda]
rotas = [aceitaRota.aceitaRota]
cenario = [testeChats[2],acoesDemandas[0]]


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    login.run(playwright, page)
    time.sleep(2)

    contador = 0
    while contador<len(cenario):
        cenario[contador](lib = playwright, pagina = page, idOtimizacao = 0, extDemanda = 0, idDemanda = 9521, listaExtIds = [], mensagem = "mensagem", titulo = "titulo")
        contador+=1
        print("açao finalizada")