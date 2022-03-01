from cmath import log
from playwright.sync_api import Playwright, sync_playwright
from demandasEotimizacao import criaDemanda
import manipulaBanco
from chat import chatEmMassa
import login

manipulaBanco.criaTabela("valores",["internalId","externalId","data"])

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    login.run(playwright, page)
    print("login finalizado")

    print("1-criar demanda")
    print("2- chat em massa")
    opcao = input("selecione o que voce deseja")
    
    if opcao == '1':
        criaDemanda.run(playwright,page,manipulaBanco)
    if opcao == '2':
        chatEmMassa.run(playwright, page)