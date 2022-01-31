import login
from playwright.sync_api import Playwright, sync_playwright

#login.run(sync_playwright())
 
while 1:
    print("1-fazer login")
    opcao = input("digite a opcao")
    if opcao == '1':
        with sync_playwright() as playwright:
            login.run(playwright)