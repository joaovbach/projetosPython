import time
from otimizaoGeral import OtimizacaoGeral as oti
class DemandaGeral:
    
    def __init__(self, banco) -> None:
        self.bancodados = banco
        self.bancodados.criaTabela("valores",["internalId","externalId","data"])
        

    def criaDemanada(self, playwright, page):
        externals = []
        quantidade  = input("quantas demandas voce deseja criar?")
        for i in range(0,int(quantidade)):
            #AQUI ENTRA NA ABA DE DEMANDAS E VAI PARA CRIAR UMA NOVA DEMANDA
            page.click("div:nth-child(4) .sc-kfzAmx .sc-iUuytg svg")
            page.click("button:has-text(\"Cadastrar nova demanda\")")
            time.sleep(2)

            #AQUI VAI PREENCHER O CLIENTE
            print("aguardando clicar no cliente")
            page.click(".sc-gJrzqj")
            print("clicou no cliente")
            page.click("text=7D1BB818-5E11-45D2-BE4E-9B398D1B35F1Created with sketchtool.AAM DO BRASIL LTDANo")
            page.click("button:has-text(\"Confirmar seleção\")")

            #AQUI VAI PREENCHER ALGUNS DADOS DA DEMANDA, O EXTERNAL ID VAI SER FEITO UMA CHECAGEM NO BANCO DE DADOS PARA SEMPRE USAR UM ID INEXISTENTE
            page.click("input[name=\"external_id\"]")
            print("colocando exterrnal id")
            external = self.bancodados.retornaUmExternalIdInexistente()
            externals.append(str(external))
            print(external)
            page.fill("input[name=\"external_id\"]", str(external))
            page.press("input[name=\"external_id\"]", "Tab")
            page.fill("input[name=\"description\"]", "1")
            page.press("input[name=\"description\"]", "Tab")
            page.fill("input[name=\"cost_center\"]", "1")
            page.press("input[name=\"cost_center\"]", "Tab")
            page.fill("input[name=\"result_center\"]", "1")

            #AQUI VAI PREENCHER O PRIMEIRO PONTO DE COLETA
            page.click(".sc-gJrzqj")
            page.click("text=7D1BB818-5E11-45D2-BE4E-9B398D1B35F1Created with sketchtool.1110015 GLUDAN GRUPP")
            page.click("button:has-text(\"Confirmar seleção\")")

            #AQUI VAI COLOCAR A DATA DO PRIMEIRO PONTO DE COLETA
            page.fill("text=Data e hora de início Horário de atendimento flexível >> input", self.bancodados.getDataValida(2))

            #AQUI VAI PREENCHER OS DADOS DO PRIMEIRO PONTO DE COLETA
            page.click("[placeholder=\"Código\"]")
            page.fill("[placeholder=\"Código\"]", "1")
            page.click("svg[role=\"img\"]")
            page.fill("input[name=\"origin_stop_loads[0][0].weight\"]", "1")
            page.click("input[name=\"origin_stop_loads[0][0].weight\"]")
            page.press("input[name=\"origin_stop_loads[0][0].weight\"]", "Tab")
            page.fill("input[name=\"origin_stop_loads[0][0].volume_m3\"]", "1")
            page.press("input[name=\"origin_stop_loads[0][0].volume_m3\"]", "Tab")
            page.fill("input[name=\"origin_stop_loads[0][0].value\"]", "1")
            page.press("input[name=\"origin_stop_loads[0][0].value\"]", "Tab")
            page.fill("input[name=\"origin_stop_loads[0][0].quantity\"]", "1")
            page.press("input[name=\"origin_stop_loads[0][0].quantity\"]", "Tab")
            page.fill("input[name=\"origin_stop_loads[0][0].description\"]", "1")

            #AQUI VAI PREENCHER O PRIMEIRO PONTO DE ENTREGA
            page.click(".sc-gJrzqj")
            page.click("text=7D1BB818-5E11-45D2-BE4E-9B398D1B35F1Created with sketchtool.3M DO BRASIL LTDA | ")
            page.click("button:has-text(\"Confirmar seleção\")")

            #AQUI VAI PREENCHER O HORARIO DO PRIMEIRO PONTO DE ENTREGA
            page.fill("div:nth-child(7) div:nth-child(2) .flex-column div .sc-jGVbCA .d-flex .react-datepicker-wrapper .react-datepicker__input-container .sc-gKsewC .sc-dlfnbm .sc-hKgILt .sc-fubCfw", self.bancodados.getDataValida(5))
            with page.expect_navigation():
                page.click("button:has-text(\"Cadastrar nova demanda\")")

            oti.geraOtimizacao(oti, playwright, page, externals)
            

    def alocaDemanda(self, playwright, page):

        nome = "JOSE ANTONIO FRANCISCO"
        id = "453"

        page.goto('https://ccomatrix-homologacao.matrixcargo.com.br/optimizations')

        page.locator(f'[class$="card"]:has-text("(ext. {id})") >> svg[role=\"img\"]').click()

        page.locator(f'[class$="card"]:has-text("(ext. {id})") >> button:has-text(\"Alocar composição\")').click()

        page.fill("[placeholder=\"Buscar por nome do motorista, placa ou tipo de composição\"]", nome.upper())

        page.click("text=×CloseAlocar composiçãoSelecione uma composição (Listando apenas as que possuem  >> img")

        page.click(f"text=Motorista: {nome.upper()}")

        page.click("button:has-text(\"Confirmar seleção\")")