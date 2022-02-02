import login
<<<<<<< HEAD
import criademanda
import time

from playwright.sync_api import Playwright, sync_playwright



=======
from playwright.sync_api import Playwright, sync_playwright

#login.run(sync_playwright())
>>>>>>> e61bbceabaf52ed0bd10f0c0bb89f4b9702786a7
 
while 1:
    print("1-fazer login")
    opcao = input("digite a opcao")
    if opcao == '1':
<<<<<<< HEAD
        print("oisdikosajhasdkjhaskojdhaslkjdhaskljdhaskdjhasjkdh")
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            login.run(playwright, page)

=======
        with sync_playwright() as playwright:
            login.run(playwright)
>>>>>>> e61bbceabaf52ed0bd10f0c0bb89f4b9702786a7
