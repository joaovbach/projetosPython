from multiprocessing.connection import wait
from playwright.sync_api import Playwright, sync_playwright

tipos = ["Frota Própria","Agregados","Terceiros"]
def run(playwright, page):

    page.goto("https://ccomatrix-homologacao.matrixcargo.com.br/chats")
    print("1-mensagem em massa")
    print("2-ininicar um novo chat")
    print("3-atender um chat")
    opcao = input("qual opcao deseja?")

    if opcao == '1':
        page.click("button:has-text(\"Mensagem em massa\")")
        for i in tipos:
            resposta = input(f"deseja mandar para os motoristas do tipo {i}? s/n")
            if resposta == 's':
                page.click(f"text={i}")

        titulo = input("digite o titulo da mensagem: ")
        page.fill("input[name=\"title\"]", titulo)

        mensagem = input("digite a mesagem que sera enviada: ")
        page.fill("textarea[name=\"message\"]", mensagem)

        page.click("button:has-text(\"confirmar envio\")")
    
    if opcao == '2':
        page.click("button:has-text(\"Iniciar chat\")")
        locaor = page.locator('[class="cardInfo"]')
        print(locaor.count())
        nome = input("digite o nome do motora: ")
        page.click(f"text=Nome: {nome}")
        page.click("button:has-text(\"Confirmar seleção\")")

    if opcao == '3':
        #sc-gtzUWE iGLlMy d-flex flex-row
        page.locator(f'[class$="flex-row"]:has-text("SERGIO ADRIANO SCOTTI") >> text="Atender chat"').click()
        #page.click("text=Assumir o chat")

        
        