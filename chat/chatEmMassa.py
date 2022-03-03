from playwright.sync_api import Playwright, sync_playwright

tipos = ["Frota Própria","Agregados","Terceiros"]

def run(playwright, page):
    
    page.goto("https://ccomatrix-homologacao.matrixcargo.com.br/chats")#acessa a aba de chats
    
    page.click("button:has-text(\"Mensagem em massa\")")#clica na opcao para enviar um chat em massa
    
    for i in tipos:#seleciona os tipos de motoristas que vao receber a mensagem em massa
        
        #resposta = input(f"deseja mandar para os motoristas do tipo {i}? s/n")
        #if resposta == 's':
                #page.click(f"text={i}")
        page.click(f"text={i}")

    #titulo = input("digite o titulo da mensagem: ")
    #page.fill("input[name=\"title\"]", titulo)
    page.fill("input[name=\"title\"]", "teste")

    #mensagem = input("digite a mesagem que sera enviada: ")
    #page.fill("textarea[name=\"message\"]", mensagem)
    page.fill("textarea[name=\"message\"]", "ola")

    page.click("button:has-text(\"confirmar envio\")")