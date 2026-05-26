from playwright.sync_api import sync_playwright
import time

with sync_playwright() as pw:  
    navegador = pw.chromium.launch(headless=False)
    contexto = navegador.new_context()
    pagina = contexto.new_page()
    pagina.goto("https://hhbet34.com/")  # Replace with the actual URL of Tiguer
    time.sleep(1.5)
    pagina.get_by_role('textbox',  name= 'Digite o Número do Celular/E-' ).fill("remosoozomer")
    time.sleep(0.75)
    pagina.get_by_role("textbox", name="Insira a senha").fill("0.75234567a*")
    time.sleep(0.75)
    pagina.get_by_role("textbox", name="Confirmar senha").fill("0.75234567a*")
    time.sleep(0.75)
    pagina.get_by_role("textbox", name="Introduza o seu nome real").fill("zezinho")
    time.sleep(0.75)
    
    botao18 = pagina.get_by_text("Tenho mais de 18 anos, li e")
    if not botao18.is_checked():
        botao18.check()
    time.sleep(0.75)
    
    botaoRegistro = pagina.get_by_role("button", name="Registro")
    botaoRegistro.click(force=True)
    # with contexto.expect_page() as pagina2_info:
    #     botaoRegistro.click(force=True)
    # pagina2 = pagina2_info.value
    # print(pagina2)
    time.sleep(10)  # Wait for a while to see the page (optional)
    navegador.close()