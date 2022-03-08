import time

class ChatGeral:

    def __init__(self) -> None:
        pass

    def chatEmMassa(self):
        pass

    def iniciaChat(self, **kwargs):
        
        kwargs["pagina"].goto("https://ccomatrix-homologacao.matrixcargo.com.br/chats")
        kwargs["pagina"].click("button:has-text(\"Iniciar chat\")")
        kwargs["pagina"].click("text=Nome: ELIAS LENZ FERREIRA")
        with kwargs["pagina"].expect_navigation():
            kwargs["pagina"].click("button:has-text(\"Confirmar seleção\")")

        #page.click("#inputMessage")  
        kwargs["pagina"].fill("#inputMessage", "alo") 
        kwargs["pagina"].press("#inputMessage", "Enter")
        time.sleep(2)

    def encerraChat(self, **kwargs):
            
        kwargs["pagina"].goto("https://ccomatrix-homologacao.matrixcargo.com.br/chats")
        kwargs["pagina"].click("button:has-text(\"Meus chats\")")  
        kwargs["pagina"].click("text=ELIAS LENZ FERREIRA")        
        kwargs["pagina"].click("text=Marcar como resolvido >> div")        
        kwargs["pagina"].click("button:has-text(\"Confirmar\")")

