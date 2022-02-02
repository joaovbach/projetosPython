import login
import criademanda
import time

from playwright.sync_api import Playwright, sync_playwright



 
while 1:
    print("1-fazer login")
    opcao = input("digite a opcao")
    if opcao == '1':
        print("oisdikosajhasdkjhaskojdhaslkjdhaskljdhaskdjhasjkdh")
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            login.run(playwright, page)

