from multiprocessing.connection import wait
from playwright.sync_api import Playwright, sync_playwright

def run(playwright, page, id):

     #page.locator('[class$="card"]').click()
     page.goto('https://ccomatrix-homologacao.matrixcargo.com.br/optimizations')
     #nome = input('digite o nome do motora')
     nome = "LAURINDO DO ROCIO MOLINARI"
     #id = input('digite o extarnalId da demanda')

     page.locator(f'[class$="card"]:has-text("(ext. {id})") >> svg[role=\"img\"]').click()

     page.locator(f'[class$="card"]:has-text("(ext. {id})") >> button:has-text(\"Alocar composição\")').click()

     page.fill("[placeholder=\"Buscar por nome do motorista, placa ou tipo de composição\"]", nome.upper())

     page.click("text=×CloseAlocar composiçãoSelecione uma composição (Listando apenas as que possuem  >> img")

     page.click(f"text=Motorista: {nome.upper()}")

     page.click("button:has-text(\"Confirmar seleção\")")
     
     
     #page.click("svg[role=\"img\"]")