import login
import criademanda
import time
from playwright.sync_api import Playwright, sync_playwright





    
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
                indice = input("escolha uma opcao")

                if indice == '1':
                    criademanda.run(playwright, page)
                    loginFeito = True
                    print("acabou")
                    main(True,0,True)
        else:
            browser.close()
    
    main(True,0,False)
                    
