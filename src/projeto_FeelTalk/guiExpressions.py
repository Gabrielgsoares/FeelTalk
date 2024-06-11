# Part of this file was generated with the help of Tkinter Designer developed by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# Definindo os caminhos de saída e ativos
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame1") 

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
def open_expressions_window():

    expressions_window = Tk()
    expressions_window.geometry("1001x561")
    expressions_window.configure(bg="#FFFFFF")
    
    # Centraliza a janela
    center_window(expressions_window)

    def set_surpreso():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        entry_1.insert("1.0", "SURPRESO")  # Insere o novo texto
        
    def set_triste():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        entry_1.insert("1.0", "TRISTE")  # Insere o novo texto

    def set_feliz():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        entry_1.insert("1.0", "FELIZ")  # Insere o novo texto
        
    def set_medo():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        entry_1.insert("1.0", "MEDO")  # Insere o novo texto
        
    def set_estressado():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        entry_1.insert("1.0", "ESTRESSADO")  # Insere o novo texto
        
    def set_apaixado():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        entry_1.insert("1.0", "APAIXONADO")  # Insere o novo texto
        
    def set_enjoado():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        entry_1.insert("1.0", "ENJOADO")  # Insere o novo texto
    
    def set_indignado():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        entry_1.insert("1.0", "INDIGNADO")  # Insere o novo texto
        
    def set_apagar():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        
    # Criando o canvas
    canvas = Canvas(
        expressions_window,
        bg="#FFFFFF",
        height=561,
        width=1001,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1001.0,
        561.0,
        fill="#73A5B1",
        outline=""
    )
    canvas.create_rectangle(
        0.0,
        0.0,
        1001.0,
        63.0,
        fill="#505050",
        outline=""
    )

    # Criando a entrada de texto
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        501.5,
        137.0,
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
        y=86.0,
        width=567.0,
        height=100.0
    )

    # Criando textos
    canvas.create_text(
        421.0,
        8.0,
        anchor="nw",
        text="Expressões",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 40 * -1)
    )

    canvas.create_text(
        160.0,
        335.0,
        anchor="nw",
        text="SURPRESO",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        371.0,
        335.0,
        anchor="nw",
        text="TRISTE",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        566.0,
        335.0,
        anchor="nw",
        text="FELIZ",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        771.0,
        334.0,
        anchor="nw",
        text="MEDO",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        745.0,
        498.0,
        anchor="nw",
        text="INDIGNADO",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        338.0,
        498.0,
        anchor="nw",
        text="APAIXONADO",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        147.0,
        498.0,
        anchor="nw",
        text="ESTRESSADO",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        548.0,
        498.0,
        anchor="nw",
        text="ENJOADO",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )
    
    # Criando botões
    button_image_medo = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_medo = Button(
        image=button_image_medo,
        borderwidth=0,
        highlightthickness=0,
        command=set_medo,
        relief="flat"
    )
    button_medo.place(
        x=750.0,
        y=233.0,
        width=94.0,
        height=95.0
    )


    button_image_config = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_config = Button(
        image=button_image_config,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_config clicked"),
        relief="flat"
    )
    button_config.place(
        x=20.0,
        y=98.0,
        width=77.0,
        height=77.0
    )

    button_image_erase = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_erase = Button(
        image=button_image_erase,
        borderwidth=0,
        highlightthickness=0,
        command=set_apagar,
        relief="flat"
    )
    button_erase.place(
        x=805.0,
        y=98.0,
        width=77.0,
        height=78.0
    )

    button_image_speak = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_speak = Button(
        image=button_image_speak,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_speak clicked"),
        relief="flat"
    )
    button_speak.place(
        x=125.0,
        y=98.0,
        width=77.0,
        height=77.0
    )

    button_image_feliz = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_feliz = Button(
        image=button_image_feliz,
        borderwidth=0,
        highlightthickness=0,
        command=set_feliz,
        relief="flat"
    )
    button_feliz.place(
        x=547.0,
        y=233.0,
        width=94.0,
        height=95.0
    )

    button_image_triste = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_triste = Button(
        image=button_image_triste,
        borderwidth=0,
        highlightthickness=0,
        command=set_triste,
        relief="flat"
    )
    button_triste.place(
        x=357.0,
        y=233.0,
        width=94.0,
        height=95.0
    )

    button_image_surpreso = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_surpreso = Button(
        image=button_image_surpreso,
        borderwidth=0,
        highlightthickness=0,
        command=set_surpreso,
        relief="flat"
    )
    button_surpreso.place(
        x=163.0,
        y=233.0,
        width=94.0,
        height=95.0
    )

    button_image_estressado = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_estressado = Button(
        image=button_image_estressado,
        borderwidth=0,
        highlightthickness=0,
        command=set_estressado,
        relief="flat"
    )
    button_estressado.place(
        x=163.0,
        y=397.0,
        width=94.0,
        height=95.0
    )

    button_image_apaixonado = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_apaixonado = Button(
        image=button_image_apaixonado,
        borderwidth=0,
        highlightthickness=0,
        command=set_apaixado,
        relief="flat"
    )
    button_apaixonado.place(
        x=357.0,
        y=397.0,
        width=94.0,
        height=95.0
    )

    button_image_enjoado = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_enjoado = Button(
        image=button_image_enjoado,
        borderwidth=0,
        highlightthickness=0,
        command=set_enjoado,
        relief="flat"
    )
    button_enjoado.place(
        x=547.0,
        y=397.0,
        width=94.0,
        height=95.0
    )

    button_image_indignado = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_indignado = Button(
        image=button_image_indignado,
        borderwidth=0,
        highlightthickness=0,
        command=set_indignado,
        relief="flat"
    )
    button_indignado.place(
        x=750.0,
        y=397.0,
        width=94.0,
        height=95.0
    )

    button_image_navigate_back = PhotoImage(
        file=relative_to_assets("button_12.png"))
    button_navigate_back = Button(
        image=button_image_navigate_back,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: navigate_to_home(expressions_window),
        relief="flat"
    )
    button_navigate_back.place(
        x=910.0,
        y=98.0,
        width=77.0,
        height=77.0
    )

    expressions_window.resizable(False, False)
    expressions_window.mainloop()
    
# Função para voltar para janela Home
def navigate_to_home(current_window):
    current_window.destroy()
    import guiHome
    guiHome.open_home_window()
