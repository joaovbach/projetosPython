class OtimizacaoGeral:
    def __init__(self) -> None:
        pass

    def geraOtimizacao(**kwargs):
        kwargs['pagina'].goto("https://ccomatrix-homologacao.matrixcargo.com.br/optimizations")
        kwargs['pagina'].click("button:has-text(\"Adicionar nova otimização\")")
        #page.locator(f'[class$="card-header"]:has-text("31233333") >> :nth-match(span, 3)').click()
        for i in kwargs['listaExtIds']:
            kwargs['pagina'].locator(f'[class$="card-header"]:has-text("(ext. {i})") >> :nth-match(span, 3)').click()

            # Click button:has-text("Continuar")
        kwargs['pagina'].click("button:has-text(\"Continuar\")")
        # Click button:has-text("Avançar")
        kwargs['pagina'].click("button:has-text(\"Avançar\")")
        # Click text=Selecionar todas
        kwargs['pagina'].click("text=Selecionar todas")
        # Click button:has-text("Continuar")
        kwargs['pagina'].click("button:has-text(\"Continuar\")")
        # Click button:has-text("Otimizar")
        # with page.expect_navigation(url="https://ccomatrix-homologacao.matrixcargo.com.br/optimizations"):
        with kwargs['pagina'].expect_navigation():
            kwargs['pagina'].click("button:has-text(\"Otimizar\")")

        