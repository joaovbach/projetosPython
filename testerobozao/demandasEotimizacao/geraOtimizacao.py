import time

def run(playwright, page, externalids):
    page.goto("https://ccomatrix-homologacao.matrixcargo.com.br/optimizations")
    page.click("button:has-text(\"Adicionar nova otimização\")")
    #page.locator(f'[class$="card-header"]:has-text("31233333") >> :nth-match(span, 3)').click()
    for i in externalids:
        page.locator(f'[class$="card-header"]:has-text("(ext. {i})") >> :nth-match(span, 3)').click()

    time.sleep(2000)