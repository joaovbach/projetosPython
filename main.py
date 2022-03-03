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

chats = ChatGeral()
demandas = DemandaGeral(manipulaBanco)
otimizacao = OtimizacaoGeral()

testeChats = [chats.encerraChat,chats.iniciaChat]
acoesDemandas = [demandas.criaDemanada, demandas.alocaDemanda]

cenario = [acoesDemandas[0]]


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    login.run(playwright, page)
    time.sleep(2)

    contador = 0
    while contador<len(cenario):
        cenario[contador](playwright, page)
        contador+=1
        print("foise")