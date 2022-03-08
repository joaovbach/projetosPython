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

chats = ChatGeral()
demandas = DemandaGeral(manipulaBanco)
otimizacao = OtimizacaoGeral()
aceitaRota = AceitaRota()

testeChats = [chats.encerraChat,chats.iniciaChat]
acoesDemandas = [demandas.criaDemanada, demandas.alocaDemanda]
rotas = [aceitaRota.aceitaRota]
cenario = [acoesDemandas[0]]


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    login.run(playwright, page)
    time.sleep(2)

    contador = 0
    while contador<len(cenario):
        cenario[contador](lib = playwright, pagina = page, idOtimizacao = 0, extDemanda = 0, idDemanda = 9521,listaExtIds = [])
        contador+=1
        print("foise")