import time

class CadastroMotoraRefac:
    def __init__(self) -> None:
        pass

    def cadastra(self, **kwargs):
        kwargs["pagina"].goto("https://feat-sm-89-sm-85.preview.matrixcargo.com.br/motoristas")
            # Click text=add_circle_outlineNovo Cadastro
        kwargs["pagina"].locator("text=add_circle_outlineNovo Cadastro").click()
        # expect(page).to_have_url("https://feat-sm-89-sm-85.preview.matrixcargo.com.br/motoristas/novo-motorista")
        # Click [placeholder="CPF"]
        kwargs["pagina"].locator("[placeholder=\"CPF\"]").click()
        # Fill [placeholder="CPF"]
        kwargs["pagina"].locator("[placeholder=\"CPF\"]").fill("999.999.999-99_")
        # Click [placeholder="E-mail"]
        kwargs["pagina"].locator("[placeholder=\"E-mail\"]").click()
        # Fill [placeholder="E-mail"]
        kwargs["pagina"].locator("[placeholder=\"E-mail\"]").fill("a@gmail.com")
        # Click [placeholder="Senha"]
        kwargs["pagina"].locator("[placeholder=\"Senha\"]").click()
        # Fill [placeholder="Senha"]
        kwargs["pagina"].locator("[placeholder=\"Senha\"]").fill("123")
        # Click [placeholder="Nome completo"]
        kwargs["pagina"].locator("[placeholder=\"Nome completo\"]").click()
        # Fill [placeholder="Nome completo"]
        kwargs["pagina"].locator("[placeholder=\"Nome completo\"]").fill("teste")
        # Click [placeholder="Celular"]
        kwargs["pagina"].locator("[placeholder=\"Celular\"]").click()
        # Fill [placeholder="Celular"]
        kwargs["pagina"].locator("[placeholder=\"Celular\"]").fill("(31) 9980-37245")
        # Click [placeholder="Data de nascimento"]
        kwargs["pagina"].locator("[placeholder=\"Data de nascimento\"]").click()
        # Fill [placeholder="Data de nascimento"]
        kwargs["pagina"].locator("[placeholder=\"Data de nascimento\"]").fill("27/11/2000_")
        # Click [placeholder="CEP"]
        kwargs["pagina"].locator("[placeholder=\"CEP\"]").click()
        # Fill [placeholder="CEP"]
        kwargs["pagina"].locator("[placeholder=\"CEP\"]").fill("81130-060_")
        # Click [placeholder="Logradouro"]
        kwargs["pagina"].locator("[placeholder=\"Endereço\"]").click()
        # Fill [placeholder="Logradouro"]
        kwargs["pagina"].locator("[placeholder=\"Endereço\"]").fill("teste")
        # Click [placeholder="Numero"]
        kwargs["pagina"].locator("[placeholder=\"Numero\"]").click()
        # Fill [placeholder="Numero"]
        kwargs["pagina"].locator("[placeholder=\"Numero\"]").fill("999")
        # Click [placeholder="Complemento"]
        kwargs["pagina"].locator("[placeholder=\"Complemento\"]").click()
        # Fill [placeholder="Complemento"]
        kwargs["pagina"].locator("[placeholder=\"Complemento\"]").fill("999")
        # Click text=EstadoEstado >> [data-testid="input"]
        kwargs["pagina"].locator("text=EstadoEstado >> [data-testid=\"input\"]").click()
        # Fill text=EstadoEstado >> [data-testid="input"]
        kwargs["pagina"].locator("text=EstadoEstado >> [data-testid=\"input\"]").fill("parana")
        # Click text=Paraná - PR
        kwargs["pagina"].locator("text=Paraná - PR").click()
        # Click [placeholder="Cidade"]
        kwargs["pagina"].locator("[placeholder=\"Cidade\"]").click()
        # Fill [placeholder="Cidade"]
        kwargs["pagina"].locator("[placeholder=\"Cidade\"]").fill("curitiba")
        # Click [placeholder="Bairro"]
        kwargs["pagina"].locator("[placeholder=\"Bairro\"]").click()
        # Fill [placeholder="Bairro"]
        kwargs["pagina"].locator("[placeholder=\"Bairro\"]").fill("capao raso")
        # Click [placeholder="RG"]
        kwargs["pagina"].locator("[placeholder=\"RG\"]").click()
        # Fill [placeholder="RG"]
        kwargs["pagina"].locator("[placeholder=\"RG\"]").fill("9999999")
        # Click [placeholder="CNH"]
        kwargs["pagina"].locator("[placeholder=\"CNH\"]").click()
        # Fill [placeholder="CNH"]
        kwargs["pagina"].locator("[placeholder=\"CNH\"]").fill("99999999")
        # Click text=CategoriaCategoria >> [aria-label="Open"]
        kwargs["pagina"].locator("text=CategoriaCategoria >> [aria-label=\"Open\"]").click()
        # Click li[role="option"]:has-text("AC")
        kwargs["pagina"].locator("li[role=\"option\"]:has-text(\"AC\")").click()
        # Click [placeholder="Vencimento"]
        kwargs["pagina"].locator("[placeholder=\"Vencimento\"]").click()
        # Fill [placeholder="Vencimento"]
        kwargs["pagina"].locator("[placeholder=\"Vencimento\"]").fill("20/11/2030_")
        # Click text=Tipo de MotoristaTipo de Motorista >> [aria-label="Open"]
        kwargs["pagina"].locator("text=Tipo de MotoristaTipo de Motorista >> [aria-label=\"Open\"]").click()
        # Click text=Frota Propria
        kwargs["pagina"].locator("text=Frota Propria").click()
        # Click text=Possui MOPPPossui MOPP >> [aria-label="Open"]
        kwargs["pagina"].locator("text=Possui MOPPPossui MOPP >> [aria-label=\"Open\"]").click()
        # Click text=Não
        kwargs["pagina"].locator("text=Não").click()

        time.sleep(10)