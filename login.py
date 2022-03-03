from playwright.sync_api import Playwright, sync_playwright



def run(playwright, page):
    print("iniciando login")
    
    page.goto("https://ccomatrix-homologacao.matrixcargo.com.br/")#entra na pagina
    
    page.click("[placeholder=\"Login\"]")
    
    page.fill("[placeholder=\"Login\"]", "joao.bach@matrixcargo.com.br")#preenche o nome do usuario
    
    page.press("[placeholder=\"Login\"]", "Tab")
    
    page.fill("[placeholder=\"Senha\"]", "123")#preenche a senha do usuario
    
    page.press("[placeholder=\"Senha\"]", "Enter")#finaliza o login
    print("finalizando login")