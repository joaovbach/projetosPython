import time

class ChatGeral:
    
    def __init__(self) -> None:
        self.tipos = ["Frota Própria","Agregados","Terceiros"]

    def chatEmMassa(self, **kwargs):
        kwargs["pagina"].goto("https://ccomatrix-homologacao.matrixcargo.com.br/chats")
        #kwargs["pagina"].click("span:has-text(\"Chat em massa\")")
        kwargs["pagina"].frame_locator("iframe").locator("text=forumChat em massa").click()
        for i in self.tipos:
            #resposta = input(f"deseja mandar para os motoristas do tipo {i}? s/n")
            #if resposta == 's':
            kwargs["pagina"].click(f"text={i}")

        kwargs["pagina"].fill("input[name=\"title\"]", kwargs["titulo"])
        kwargs["pagina"].fill("textarea[name=\"message\"]", kwargs["mensagem"])
        kwargs["pagina"].click("button:has-text(\"confirmar envio\")")

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

