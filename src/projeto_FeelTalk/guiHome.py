# Part of this file was generated with the help of Tkinter Designer developed by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# Definindo os caminhos de saída e ativos
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0")  

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Função para calcular o meio da tela
def center_window(window, width=1001, height=561):
    # Calcula a posição x e y da janela
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

# Função para abrir a janela
def open_home_window():
    home_window = Tk()
    home_window.geometry("1001x561")
    home_window.configure(bg = "#FFFFFF")
    
    # Centraliza a janela
    center_window(home_window)

    # Criando o canvas
    canvas = Canvas(
        home_window,
        bg = "#FFFFFF",
        height = 561,
        width = 1001,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1001.0,
        561.0,
        fill="#73A5B1",
        outline="")

    canvas.create_rectangle(
        0.0,
        0.0,
        1001.0,
        63.0,
        fill="#505050",
        outline="")

    # Criando a entrada de texto
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        501.5,
        120.0,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=218.0,
        y=69.0,
        width=567.0,
        height=100.0
    )

    # Criando textos
    canvas.create_text(
        334.0,
        8.0,
        anchor="nw",
        text="O que deseja comunicar?",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 40 * -1)
    )

    canvas.create_text(
        105.0,
        307.0,
        anchor="nw",
        text="COMUNICAÇÃO",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        791.0,
        307.0,
        anchor="nw",
        text="EXPRESSÕES",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        420.0,
        458.0,
        anchor="nw",
        text="RESPOSTAS RÁPIDAS",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        581.0,
        307.0,
        anchor="nw",
        text="TECLADO",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        697.0,
        458.0,
        anchor="nw",
        text="PALAVRAS BASICAS",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        90.0,
        458.0,
        anchor="nw",
        text="SAUDAÇÕES E FORMALIDADES",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        336.0,
        307.0,
        anchor="nw",
        text="NECESSIDADES",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )
    
    # Criando botões
    button_image_expressoes = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_expressoes = Button(
        image=button_image_expressoes,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate_to_expressions(home_window),
        relief="flat"
    )
    button_expressoes.place(
        x=805.0,
        y=206.0,
        width=94.0,
        height=95.0
    )

    button_image_comunicacao = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_comunicacao = Button(
        image=button_image_comunicacao,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_comunicacao clicked"),
        relief="flat"
    )
    button_comunicacao.place(
        x=132.0,
        y=206.0,
        width=94.0,
        height=95.0
    )

    button_image_teclado = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_teclado = Button(
        image=button_image_teclado,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_teclado clicked"),
        relief="flat"
    )
    button_teclado.place(
        x=578.0,
        y=206.0,
        width=94.0,
        height=95.0
    )

    button_image_saudacoes_e_formalidades = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_saudacoes_e_formalidades = Button(
        image=button_image_saudacoes_e_formalidades,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_saudacoes_e_formalidades clicked"),
        relief="flat"
    )
    button_saudacoes_e_formalidades.place(
        x=185.0,
        y=357.0,
        width=94.0,
        height=95.0
    )

    button_image_respostas_rapidas = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_respostas_rapidas = Button(
        image=button_image_respostas_rapidas,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_respostas_rapidas clicked"),
        relief="flat"
    )
    button_respostas_rapidas.place(
        x=474.0,
        y=357.0,
        width=94.0,
        height=95.0
    )

    button_image_palavras_basicas = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_palavras_basicas = Button(
        image=button_image_palavras_basicas,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_palavras_basicas clicked"),
        relief="flat"
    )
    button_palavras_basicas.place(
        x=738.0,
        y=357.0,
        width=94.0,
        height=95.0
    )

    button_image_necessidade = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_necessidade = Button(
        image=button_image_necessidade,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_necessidade clicked"),
        relief="flat"
    )
    button_necessidade.place(
        x=362.0,
        y=206.0,
        width=94.0,
        height=95.0
    )

    button_image_speak  = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_speak  = Button(
        image=button_image_speak ,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_speak clicked"),
        relief="flat"
    )
    button_speak.place(
        x=125.0,
        y=81.0,
        width=77.0,
        height=77.0
    )

    button_image_erase = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_erase = Button(
        image=button_image_erase,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_erase clicked"),
        relief="flat"
    )
    button_erase.place(
        x=857.0,
        y=81.0,
        width=77.0,
        height=77.0
    )

    button_image_config = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_config = Button(
        image=button_image_config,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_config clicked"),
        relief="flat"
    )
    button_config.place(
        x=20.0,
        y=81.0,
        width=77.0,
        height=77.0
    )

    home_window.resizable(False, False)
    home_window.mainloop()

# Função para abrir para janela Expressões
def navigate_to_expressions(current_window):
    current_window.destroy()
    import guiExpressions
    guiExpressions.open_expressions_window()