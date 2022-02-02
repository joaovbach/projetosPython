from playwright.sync_api import Playwright, sync_playwright
import time

def run(playwright, page):
    print("alee")
    page.click("button:has-text(\"Demandas\")")
    print("aguardando")
    time.sleep(10000)
