from playwright.sync_api import Playwright, sync_playwright

tipos = ["Frota Própria","Agregados","Terceiros"]

def run(playwright, page):
    
    page.goto("https://ccomatrix-homologacao.matrixcargo.com.br/chats")
    
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