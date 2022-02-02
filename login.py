import criademanda
from playwright.sync_api import Playwright, sync_playwright
#import selecioneAutomacoes


def run(playwright, page):
    print("fazendo login")
    page.goto("https://ccomatrix-homologacao.matrixcargo.com.br/")
    page.click("[placeholder=\"Login\"]")

    page.fill("[placeholder=\"Login\"]", "joao.bach@matrixcargo.com.br")

    page.press("[placeholder=\"Login\"]", "Tab")

    page.fill("[placeholder=\"Senha\"]", "123")

    page.press("[placeholder=\"Senha\"]", "Enter")
    print("login finalizado")
    #selecioneAutomacoes.avisos("login finalizado")

