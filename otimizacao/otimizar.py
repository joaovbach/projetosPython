from playwright.sync_api import Playwright, sync_playwright

def run(playwright, page,ids):
    page.goto("https://ccomatrix-homologacao.matrixcargo.com.br/optimizations")
    page.click("button:has-text(\"Adicionar nova otimização\")")
    #page.locator(f'[class$="card-header"]:has-text("31233333") >> :nth-match(span, 3)').click()
    for i in ids:
        page.locator(f'[class$="card-header"]:has-text("(ext. {i})") >> :nth-match(span, 3)').click()
