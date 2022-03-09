import time
from otimizaoGeral import OtimizacaoGeral as oti
class DemandaGeral:
    
    def __init__(self, banco) -> None:
        self.bancodados = banco
        self.bancodados.criaTabela("valores",["internalId","externalId","data"])
        

    def criaDemanada(self, **kwargs):
        externals = []
        quantidade  = input("quantas demandas voce deseja criar?")
        for i in range(0,int(quantidade)):
            #AQUI ENTRA NA ABA DE DEMANDAS E VAI PARA CRIAR UMA NOVA DEMANDA
            kwargs['pagina'].click("div:nth-child(4) .sc-kfzAmx .sc-iUuytg svg")
            kwargs['pagina'].click("button:has-text(\"Cadastrar nova demanda\")")
            time.sleep(2)

            #AQUI VAI PREENCHER O CLIENTE
            print("aguardando clicar no cliente")
            #try:
                #kwargs['pagina'].locator(f'[class$="complete_row"]:>>input').click()
                #print("apertei")
            #except:
                #print("nao encontrei")
            #try:
                #kwargs['pagina'].click(".sc-gJrzqj")
            #except:
                #kwargs['pagina'].click(".sc-fVfVBW")
            teste = kwargs['pagina'].locator('[class$="complete_row"]>>[placeholder="Selecionar cliente"]')
            #print("aaaalo", teste)
            #kwargs["pagina"].locator('[placeholder="Selecionar cliente"]').click()
            #kwargs['pagina'].click(".sc-gJrzqj")
            teste.click(force=True)
            
            print("clicou no cliente")
            kwargs['pagina'].click("text=7D1BB818-5E11-45D2-BE4E-9B398D1B35F1Created with sketchtool.AAM DO BRASIL LTDANo")
            kwargs['pagina'].click("button:has-text(\"Confirmar seleção\")")

            #AQUI VAI PREENCHER ALGUNS DADOS DA DEMANDA, O EXTERNAL ID VAI SER FEITO UMA CHECAGEM NO BANCO DE DADOS PARA SEMPRE USAR UM ID INEXISTENTE
            kwargs['pagina'].click("input[name=\"external_id\"]")
            print("colocando exterrnal id")
            external = self.bancodados.retornaUmExternalIdInexistente()
            externals.append(str(external))
            print(external)
            kwargs['pagina'].fill("input[name=\"external_id\"]", str(external))
            kwargs['pagina'].press("input[name=\"external_id\"]", "Tab")
            kwargs['pagina'].fill("input[name=\"description\"]", "1")
            kwargs['pagina'].press("input[name=\"description\"]", "Tab")
            kwargs['pagina'].fill("input[name=\"cost_center\"]", "1")
            kwargs['pagina'].press("input[name=\"cost_center\"]", "Tab")
            kwargs['pagina'].fill("input[name=\"result_center\"]", "1")

            #AQUI VAI PREENCHER O PRIMEIRO PONTO DE COLETA
            #kwargs['pagina'].click(".sc-gJrzqj")
            teste2 = kwargs['pagina'].locator('[class$="complete_row"]>>[name="origin_demand_stops[0].address_id"]')
            teste2.click(force=True)
            kwargs['pagina'].click("text=7D1BB818-5E11-45D2-BE4E-9B398D1B35F1Created with sketchtool.1110015 GLUDAN GRUPP")
            kwargs['pagina'].click("button:has-text(\"Confirmar seleção\")")

            #AQUI VAI COLOCAR A DATA DO PRIMEIRO PONTO DE COLETA
            kwargs['pagina'].fill("text=Data e hora de início Horário de atendimento flexível >> input", self.bancodados.getDataValida(2))

            #AQUI VAI PREENCHER OS DADOS DO PRIMEIRO PONTO DE COLETA
            kwargs['pagina'].click("[placeholder=\"Código\"]")
            kwargs['pagina'].fill("[placeholder=\"Código\"]", "1")
            kwargs['pagina'].click("svg[role=\"img\"]")
            kwargs['pagina'].fill("input[name=\"origin_stop_loads[0][0].weight\"]", "1")
            kwargs['pagina'].click("input[name=\"origin_stop_loads[0][0].weight\"]")
            kwargs['pagina'].press("input[name=\"origin_stop_loads[0][0].weight\"]", "Tab")
            kwargs['pagina'].fill("input[name=\"origin_stop_loads[0][0].volume_m3\"]", "1")
            kwargs['pagina'].press("input[name=\"origin_stop_loads[0][0].volume_m3\"]", "Tab")
            kwargs['pagina'].fill("input[name=\"origin_stop_loads[0][0].value\"]", "1")
            kwargs['pagina'].press("input[name=\"origin_stop_loads[0][0].value\"]", "Tab")
            kwargs['pagina'].fill("input[name=\"origin_stop_loads[0][0].quantity\"]", "1")
            kwargs['pagina'].press("input[name=\"origin_stop_loads[0][0].quantity\"]", "Tab")
            kwargs['pagina'].fill("input[name=\"origin_stop_loads[0][0].description\"]", "1")

            #AQUI VAI PREENCHER O PRIMEIRO PONTO DE ENTREGA
            #kwargs['pagina'].click(".sc-gJrzqj")
            teste3 = kwargs['pagina'].locator('[class$="complete_row"]>>[name="destination_demand_stops[0].address_id"]')
            teste3.click(force=True)
            kwargs['pagina'].click("text=7D1BB818-5E11-45D2-BE4E-9B398D1B35F1Created with sketchtool.3M DO BRASIL LTDA | ")
            kwargs['pagina'].click("button:has-text(\"Confirmar seleção\")")

            #AQUI VAI PREENCHER O HORARIO DO PRIMEIRO PONTO DE ENTREGA
            kwargs['pagina'].fill("div:nth-child(7) div:nth-child(2) .flex-column div .sc-jGVbCA .d-flex .react-datepicker-wrapper .react-datepicker__input-container .sc-gKsewC .sc-dlfnbm .sc-hKgILt .sc-fubCfw", self.bancodados.getDataValida(5))
            with kwargs['pagina'].expect_navigation():
                kwargs['pagina'].click("button:has-text(\"Cadastrar nova demanda\")")

            oti.geraOtimizacao(otimi = oti,lib = kwargs["lib"],pagina = kwargs["pagina"], listaExtIds = externals)
            

    def alocaDemanda(self, **kwargs):

        nome = "JOSE ANTONIO FRANCISCO"
        id = "453"

        kwargs['pagina'].goto('https://ccomatrix-homologacao.matrixcargo.com.br/optimizations')

        kwargs['pagina'].locator(f'[class$="card"]:has-text("(ext. {kwargs["idDemanda"]})") >> svg[role=\"img\"]').click()

        kwargs['pagina'].locator(f'[class$="card"]:has-text("(ext. {kwargs["idDemanda"]})") >> button:has-text(\"Alocar composição\")').click()

        kwargs['pagina'].fill("[placeholder=\"Buscar por nome do motorista, placa ou tipo de composição\"]", nome.upper())

        kwargs['pagina'].click("text=×CloseAlocar composiçãoSelecione uma composição (Listando apenas as que possuem  >> img")

        kwargs['pagina'].click(f"text=Motorista: {nome.upper()}")

        kwargs['pagina'].click("button:has-text(\"Confirmar seleção\")")