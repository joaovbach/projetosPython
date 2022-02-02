<<<<<<< HEAD
import criademanda
from playwright.sync_api import Playwright, sync_playwright


def run(playwright, page):

    page.goto("https://ccomatrix-homologacao.matrixcargo.com.br/")
    page.click("[placeholder=\"Login\"]")

    page.fill("[placeholder=\"Login\"]", "joao.bach@matrixcargo.com.br")

    page.press("[placeholder=\"Login\"]", "Tab")

    page.fill("[placeholder=\"Senha\"]", "123")

    page.press("[placeholder=\"Senha\"]", "Enter")
    print("ois")
    criademanda.run(playwright,page)
=======
from playwright.sync_api import Playwright, sync_playwright
def run(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://ccomatrix-homologacao.matrixcargo.com.br/
    page.goto("https://ccomatrix-homologacao.matrixcargo.com.br/")
    page.click("[placeholder=\"Login\"]")
    # Fill [placeholder="Login"]
    page.fill("[placeholder=\"Login\"]", "joao.bach@matrixcargo.com.br")
    # Press Tab
    page.press("[placeholder=\"Login\"]", "Tab")
    # Fill [placeholder="Senha"]
    page.fill("[placeholder=\"Senha\"]", "123")
    # Press Enter
    page.press("[placeholder=\"Senha\"]", "Enter")
>>>>>>> e61bbceabaf52ed0bd10f0c0bb89f4b9702786a7
