from playwright.sync_api import Playwright, sync_playwright
from . import geraOtimizacao
import time

def run(playwright, page, bancodados):
    externals = []
    quantidade  = input("quantas demandas voce deseja criar?")
    for i in range(0,int(quantidade)):
        # Click div:nth-child(4) .sc-kfzAmx .sc-iUuytg svg
        page.click("div:nth-child(4) .sc-kfzAmx .sc-iUuytg svg")
        # assert page.url == "https://ccomatrix-homologacao.matrixcargo.com.br/demands"
        # Click button:has-text("Cadastrar nova demanda")
        page.click("button:has-text(\"Cadastrar nova demanda\")")
        # assert page.url == "https://ccomatrix-homologacao.matrixcargo.com.br/demands/new"
        # Click .sc-gJrzqj
        time.sleep(2)
        print("aguardando clicar no cliente")
        page.click(".sc-gJrzqj")
        print("clicou no cliente")
        # Click text=7D1BB818-5E11-45D2-BE4E-9B398D1B35F1Created with sketchtool.AAM DO BRASIL LTDANo
        page.click("text=7D1BB818-5E11-45D2-BE4E-9B398D1B35F1Created with sketchtool.AAM DO BRASIL LTDANo")
        # Click button:has-text("Confirmar seleção")
        page.click("button:has-text(\"Confirmar seleção\")")
        # Click input[name="external_id"]
        page.click("input[name=\"external_id\"]")
        # Fill input[name="external_id"]
        print("colocando exterrnal id")
        external = bancodados.retornaUmExternalIdInexistente()
        externals.append(str(external))
        print(external)
        page.fill("input[name=\"external_id\"]", str(external))
        # Press Tab
        page.press("input[name=\"external_id\"]", "Tab")
        # Fill input[name="description"]
        page.fill("input[name=\"description\"]", "1")
        # Press Tab
        page.press("input[name=\"description\"]", "Tab")
        # Fill input[name="cost_center"]
        page.fill("input[name=\"cost_center\"]", "1")
        # Press Tab
        page.press("input[name=\"cost_center\"]", "Tab")
        # Fill input[name="result_center"]
        page.fill("input[name=\"result_center\"]", "1")
        # Click .sc-gJrzqj
        page.click(".sc-gJrzqj")
        # Click text=7D1BB818-5E11-45D2-BE4E-9B398D1B35F1Created with sketchtool.1110015 GLUDAN GRUPP
        page.click("text=7D1BB818-5E11-45D2-BE4E-9B398D1B35F1Created with sketchtool.1110015 GLUDAN GRUPP")
        # Click button:has-text("Confirmar seleção")
        page.click("button:has-text(\"Confirmar seleção\")")
        # Click text=Data e hora de início Horário de atendimento flexível >> input

        # Fill text=Data e hora de início Horário de atendimento flexível >> input
        page.fill("text=Data e hora de início Horário de atendimento flexível >> input", bancodados.getDataValida(2))
        # Click [placeholder="Código"]
        page.click("[placeholder=\"Código\"]")
        # Fill [placeholder="Código"]
        page.fill("[placeholder=\"Código\"]", "1")
        # Click svg[role="img"]
        page.click("svg[role=\"img\"]")
        # Fill input[name="origin_stop_loads[0][0].weight"]
        page.fill("input[name=\"origin_stop_loads[0][0].weight\"]", "1")
        # Click input[name="origin_stop_loads[0][0].weight"]
        page.click("input[name=\"origin_stop_loads[0][0].weight\"]")
        # Press Tab
        page.press("input[name=\"origin_stop_loads[0][0].weight\"]", "Tab")
        # Fill input[name="origin_stop_loads[0][0].volume_m3"]
        page.fill("input[name=\"origin_stop_loads[0][0].volume_m3\"]", "1")
        # Press Tab
        page.press("input[name=\"origin_stop_loads[0][0].volume_m3\"]", "Tab")
        # Fill input[name="origin_stop_loads[0][0].value"]
        page.fill("input[name=\"origin_stop_loads[0][0].value\"]", "1")
        # Press Tab
        page.press("input[name=\"origin_stop_loads[0][0].value\"]", "Tab")
        # Fill input[name="origin_stop_loads[0][0].quantity"]
        page.fill("input[name=\"origin_stop_loads[0][0].quantity\"]", "1")
        # Press Tab
        page.press("input[name=\"origin_stop_loads[0][0].quantity\"]", "Tab")
        # Fill input[name="origin_stop_loads[0][0].description"]
        page.fill("input[name=\"origin_stop_loads[0][0].description\"]", "1")
        # Click .sc-gJrzqj
        page.click(".sc-gJrzqj")
        # Click text=7D1BB818-5E11-45D2-BE4E-9B398D1B35F1Created with sketchtool.3M DO BRASIL LTDA |
        page.click("text=7D1BB818-5E11-45D2-BE4E-9B398D1B35F1Created with sketchtool.3M DO BRASIL LTDA | ")
        # Click button:has-text("Confirmar seleção")
        page.click("button:has-text(\"Confirmar seleção\")")

        page.fill("div:nth-child(7) div:nth-child(2) .flex-column div .sc-jGVbCA .d-flex .react-datepicker-wrapper .react-datepicker__input-container .sc-gKsewC .sc-dlfnbm .sc-hKgILt .sc-fubCfw", bancodados.getDataValida(5))
        # Click button:has-text("Cadastrar nova demanda")
        # with page.expect_navigation(url="https://ccomatrix-homologacao.matrixcargo.com.br/demands"):
        with page.expect_navigation():
            page.click("button:has-text(\"Cadastrar nova demanda\")")
        #time.sleep(2)

    #opcao = input("voce deseja gerar uma otimizacao usando estas demandas?s/n")
    #if opcao == 's':
        #geraOtimizacao.run(playwright, page, [external])
    #else:
        #print("valeu ate a proxima!")

    geraOtimizacao.run(playwright, page, [external])
    # ---------------------
