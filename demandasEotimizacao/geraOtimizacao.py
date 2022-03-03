import time

def run(playwright, page, externalids):
    page.goto("https://ccomatrix-homologacao.matrixcargo.com.br/optimizations")
    page.click("button:has-text(\"Adicionar nova otimização\")")
    #page.locator(f'[class$="card-header"]:has-text("31233333") >> :nth-match(span, 3)').click()
    for i in externalids:
        page.locator(f'[class$="card-header"]:has-text("(ext. {i})") >> :nth-match(span, 3)').click()

        # Click button:has-text("Continuar")
    page.click("button:has-text(\"Continuar\")")
    # Click button:has-text("Avançar")
    page.click("button:has-text(\"Avançar\")")
    # Click text=Selecionar todas
    page.click("text=Selecionar todas")
    # Click button:has-text("Continuar")
    page.click("button:has-text(\"Continuar\")")
    # Click button:has-text("Otimizar")
    # with page.expect_navigation(url="https://ccomatrix-homologacao.matrixcargo.com.br/optimizations"):
    with page.expect_navigation():
        page.click("button:has-text(\"Otimizar\")")

    time.sleep(2000)