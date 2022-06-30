import time

class ChatGeral:
    
    def __init__(self) -> None:
        self.tipos = ["Frota Propria","Agregados","Terceiros"]

    def chatEmMassa(self, **kwargs):
        kwargs["pagina"].goto("https://ccomatrix-homologacao.matrixcargo.com.br/chats")
        #kwargs["pagina"].click("span:has-text(\"Chat em massa\")")
        kwargs["pagina"].frame_locator("iframe").locator("text=forumChat em massa").click()
        for i in self.tipos:
            #resposta = input(f"deseja mandar para os motoristas do tipo {i}? s/n")
            #if resposta == 's':
            kwargs["pagina"].frame_locator("iframe").locator(f"text={i}").click()

        kwargs["pagina"].frame_locator("iframe").locator("text=TítuloTítulo >> input[type=\"text\"]").fill("titulo")
        kwargs["pagina"].frame_locator("iframe").locator("textarea").first.fill("mensagem")
        kwargs["pagina"].frame_locator("iframe").locator("button:has-text(\"Enviar\")").click()


    def iniciaChat(self, **kwargs):
        
        kwargs["pagina"].goto("https://ccomatrix-homologacao.matrixcargo.com.br/chats")
        kwargs["pagina"].frame_locator("iframe").locator("text=add_commentIniciar novo chat").click()
        #kwargs["pagina"].frame_locator("iframe").locator("[placeholder=\"Buscar por nome\\, CPF ou carteira de motorista\"]").fill("teste")
        #kwargs["pagina"].age.frame_locator("iframe").locator("[placeholder=\"Buscar por nome\\, CPF ou carteira de motorista\"]").press("Enter")
        kwargs["pagina"].frame_locator("iframe").locator("text=321").click()
        kwargs["pagina"].frame_locator("iframe").locator("div[role=\"dialog\"] div[role=\"button\"]:has-text(\"Documentos da Viagem\")").click()
        kwargs["pagina"].frame_locator("iframe").locator("text=add_commentIniciar um novo chat").click()
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

