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
    navegador = pw.firefox.launch(headless=False, args=["--window-position=0,0", "--window-size=150,300",
                                                         "--app=https://hhbet34.com"])
    contexto = navegador.new_context(viewport={"width": 150, "height": 300})
    pagina = contexto.new_page()
    pagina.goto("https://hhbet34.com/")
    time.sleep(2.0)

    pagina.get_by_role("button", name="Confimar").click(force=True)
    time.sleep(0.75)
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

#---------- INICIA BOT EM THREAD SEPARADA ----------
# def iniciar_em_thread():
#     t = threading.Thread(target=iniciar_bot, daemon=True)
#     t.start()

def iniciar_varias_abas(quantidade: int):
    for i in range(1, quantidade + 1): #definiu o i como 1 inicialmente
        t = threading.Thread(target=iniciar_bot, daemon=True)
        t.start()
        time.sleep(1)  # Pequena pausa entre o início de cada thread

label = ctk.CTkLabel(janela, text="Quantas instâncias?", font=("Arial", 14))
label.pack(pady=15)

entrada = ctk.CTkEntry(janela, placeholder_text="Ex: 3", width=100)
entrada.pack(pady=5)

def ao_clicar():
    try:
        quantidade = int(entrada.get())
        botao_site.configure(text=f"Abrindo {quantidade} ", state="disabled")  # Desabilita o botão para evitar múltiplos cliques
        t = threading.Thread(target=iniciar_varias_abas, args=(quantidade,), daemon=True)
        t.start()
    except ValueError:
        label.configure(text="Por favor, insira um número válido.")



# ---------- BOTÃO ----------

botao_site = ctk.CTkButton(
    janela,
    text="Abrir site",
    command=ao_clicar  # <- função, sem parênteses!
)

botao_site.pack(pady=50)




janela.mainloop()