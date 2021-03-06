
from demandas import criademanda
import time
from demandas import alocaDemanda
from chat import chat
from playwright.sync_api import Playwright, sync_playwright
from otimizacao import otimizar

from login import login


    
print("iniciando")
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    def main(runforever, tela, loginFeito):



        if runforever == True:
            if tela == 0 and loginFeito == False:

                login.run(playwright, page)
                loginFeito = True
                main(True,0,True)

            if tela == 0 and loginFeito == True:
                print("1-criar uma demanda")
                print("2-alocar uma demanda")
                print("3-chat")
                print("4-otimizacao")
                indice = input("escolha uma opcao")

                if indice == '1':
                    criademanda.run(playwright, page)
                    loginFeito = True
                    print("acabou")
                    main(True,0,True)

                if indice == '2':
                    alocaDemanda.run(playwright, page,1)
                    main(True,0,True)

                if indice == '3':
                    main(True,0,True)

                if indice == '4':
                    otimizar.run(playwright, page,[])
                    main(True,0,True)
        else:
            browser.close()
    
    main(True,0,False)
                    
