import time

class ChatGeral:

    def __init__(self) -> None:
        pass

    def chatEmMassa(self):
        pass

    def iniciaChat(self, playwright, page):
        
        page.goto("https://ccomatrix-homologacao.matrixcargo.com.br/chats")
        page.click("button:has-text(\"Iniciar chat\")")
        page.click("text=Nome: ELIAS LENZ FERREIRA")
        with page.expect_navigation():
            page.click("button:has-text(\"Confirmar seleção\")")

        #page.click("#inputMessage")  
        page.fill("#inputMessage", "alo") 
        page.press("#inputMessage", "Enter")
        time.sleep(2)

    def encerraChat(self, playwright, page):
            
        page.goto("https://ccomatrix-homologacao.matrixcargo.com.br/chats")
        page.click("button:has-text(\"Meus chats\")")  
        page.click("text=ELIAS LENZ FERREIRA")        
        page.click("text=Marcar como resolvido >> div")        
        page.click("button:has-text(\"Confirmar\")")

