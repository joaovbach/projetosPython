from multiprocessing.connection import wait
from playwright.sync_api import Playwright, sync_playwright
import time
import dados

def run(playwright, page):
    print("entrando na aba de demandas")
    page.goto('https://ccomatrix-homologacao.matrixcargo.com.br/demands')
    
    page.click("button:has-text(\"Cadastrar nova demanda\")")
    page.click(".sc-QplWO")
    print(dados.clientes())
    indice = input("selecione um deles")
    page.click("text="+dados.clientes()[int(indice)])
    page.click("button:has-text(\"Confirmar seleção\")")


    page.fill("input[name=\"external_id\"]", "1")
    page.fill("input[name=\"description\"]", "1")
    page.fill("input[name=\"cost_center\"]", "1")
    page.fill("input[name=\"result_center\"]", "1")

    page.click(".col-lg-9 div:nth-child(4) div .sc-fkubWd .sc-dHntBn .sc-QplWO")#CLICA PARA ESCOLHER PONTO DE PARADA
    print(dados.pontosDeParada())
    indice2 = input("selecione um ponto de parada")
    page.click("text="+dados.pontosDeParada()[int(indice2)])
    page.click("button:has-text(\"Confirmar seleção\")")
    page.fill("text=Data e hora de início Horário de atendimento flexível >> input", "02/02/2022 20:00_")
    page.fill("[placeholder=\"Código\"]", "1")
    
    page.click("svg[role=\"img\"]")
    page.fill("input[name=\"origin_stop_loads[0][0].weight\"]", "1")
    page.fill("input[name=\"origin_stop_loads[0][0].volume_m3\"]", "1")
    page.fill("input[name=\"origin_stop_loads[0][0].value\"]", "1")
    page.fill("input[name=\"origin_stop_loads[0][0].quantity\"]", "1")
    page.fill("input[name=\"origin_stop_loads[0][0].description\"]", "1")

    page.click("div:nth-child(7) div .sc-fkubWd .sc-dHntBn .sc-QplWO")#CLICA PARA ESCOLHER PONTO DE ENTREGA
    print(dados.pontosDeEntrega())
    indice3 = input("escolha um ponto de entrega")
    page.click("text="+dados.pontosDeEntrega()[int(indice3)])
    page.click("button:has-text(\"Confirmar seleção\")")
    page.fill("div:nth-child(7) div:nth-child(2) .flex-column div .sc-jGVbCA .d-flex .react-datepicker-wrapper .react-datepicker__input-container .sc-gKsewC .sc-dlfnbm .sc-hKgILt .sc-fubCfw", "03/02/2022 21:00_")

    page.click("button:has-text(\"Cadastrar nova demanda\")")

    print("cadastro de demanda finalizado")



