<<<<<<< HEAD
from playwright.sync_api import Playwright, sync_playwright
import time

def run(playwright, page):
    print("alee")
    page.click("button:has-text(\"Demandas\")")
    print("aguardando")
    time.sleep(10000)
=======
import playwright

class criaDemanda:
    def __init__(self) -> None:
        print("criador de demanda instanciado")

    def status(self):
        print("criando demanda...")
>>>>>>> e61bbceabaf52ed0bd10f0c0bb89f4b9702786a7
