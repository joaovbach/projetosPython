import time

class AceitaRota:
    def __init__(self) -> None:
        pass

    def aceitaRota(**kwargs):
        kwargs['page'].goto("https://ccomatrix-homologacao.matrixcargo.com.br/optimizations")
        #page.click("[text^='Otimizações geradas']")
        kwargs['page'].click('span:has-text("Otimizações geradas")')
        kwargs['page'].click(f'div:has-text({kwargs["idOtimizacao"]}) >> svg[role=\"img\"]')
        kwargs['page'].click("button:has-text(\"Visualizar Resultados\")")
        kwargs['page'].click(f'div:has-text("(Ext. {kwargs["idDemanda"]})")>>svg[role=\"img\"]')
        kwargs['page'].click("text=Aceitar Rota")
        kwargs['page'].click("button:has-text(\"Confirmar\")")

        time.sleep(5)