from playwright.sync_api import Playwright, sync_playwright



def run(playwright, page):
    print("iniciando login")
    # Go to https://ccomatrix-homologacao.matrixcargo.com.br/
    page.goto("https://ccomatrix-homologacao.matrixcargo.com.br/")
    # Click [placeholder="Login"]
    page.click("[placeholder=\"Login\"]")
    # Fill [placeholder="Login"]
    page.fill("[placeholder=\"Login\"]", "joao.bach@matrixcargo.com.br")
    # Press Tab
    page.press("[placeholder=\"Login\"]", "Tab")
    # Fill [placeholder="Senha"]
    page.fill("[placeholder=\"Senha\"]", "123")
    # Press Enter
    page.press("[placeholder=\"Senha\"]", "Enter")
    print("finalizando login")