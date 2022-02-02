import criademanda
from playwright.sync_api import Playwright, sync_playwright


def run(playwright, page):

    page.goto("https://ccomatrix-homologacao.matrixcargo.com.br/")
    page.click("[placeholder=\"Login\"]")

    page.fill("[placeholder=\"Login\"]", "joao.bach@matrixcargo.com.br")

    page.press("[placeholder=\"Login\"]", "Tab")

    page.fill("[placeholder=\"Senha\"]", "123")

    page.press("[placeholder=\"Senha\"]", "Enter")
    print("finalizando login")
    criademanda.run(playwright,page)

