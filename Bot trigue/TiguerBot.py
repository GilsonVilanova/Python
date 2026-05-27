from playwright.sync_api import sync_playwright
import threading
import time
import customtkinter as ctk

# ---------- INTERFACE ----------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry("600x400")
janela.title("Tiguer Bot")

# ---------- FUNÇÃO DO BOT ----------
def iniciar_bot():
    pw = sync_playwright().start()
    navegador = pw.chromium.launch(headless=False)
    contexto = navegador.new_context()
    pagina = contexto.new_page()
    pagina.goto("https://hhbet34.com/")
    time.sleep(1.5)

    pagina.get_by_role('textbox', name='Digite o Número do Celular/E-').fill("remosoozomer")
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

    pagina.get_by_role("button", name="Registro").click(force=True)

    while navegador.is_connected():
        time.sleep(1)

    pw.stop()

# ---------- INICIA BOT EM THREAD SEPARADA ----------
def iniciar_em_thread():
    t = threading.Thread(target=iniciar_bot, daemon=True)
    t.start()

# ---------- BOTÃO ----------
botao_site = ctk.CTkButton(
    janela,
    text="Abrir site",
    command=iniciar_em_thread  # <- função, sem parênteses!
)

botao_site.pack(pady=50)

janela.mainloop()