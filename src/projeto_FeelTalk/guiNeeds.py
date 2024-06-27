# Part of this file was generated with the help of Tkinter Designer developed by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# Definindo os caminhos de saída e ativos
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame2") 

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
def open_needs_window():

    needs_window = Tk()
    needs_window.geometry("1001x561")
    needs_window.configure(bg="#FFFFFF")
    
    # Centraliza a janela
    center_window(needs_window)

    def set_ajuda():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        entry_1.insert("1.0", "AJUDA")  # Insere o novo texto
        entry_1.tag_configure("big", font=("Helvetica", 24)) # Configura a fonte maior
        entry_1.tag_add("big", "1.0", "end") # Aplica a tag “big” a todo o texto
        
    def set_comida():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        entry_1.insert("1.0", "COMIDA")  # Insere o novo texto
        entry_1.tag_configure("big", font=("Helvetica", 24)) # Configura a fonte maior
        entry_1.tag_add("big", "1.0", "end") # Aplica a tag “big” a todo o texto

    def set_bebida():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        entry_1.insert("1.0", "BEBIDA")  # Insere o novo texto
        entry_1.tag_configure("big", font=("Helvetica", 24)) # Configura a fonte maior
        entry_1.tag_add("big", "1.0", "end") # Aplica a tag “big” a todo o texto
        
    def set_banheiro():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        entry_1.insert("1.0", "BANHEIRO")  # Insere o novo texto
        entry_1.tag_configure("big", font=("Helvetica", 24)) # Configura a fonte maior
        entry_1.tag_add("big", "1.0", "end") # Aplica a tag “big” a todo o texto
        
    def set_dor():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        entry_1.insert("1.0", "DOR")  # Insere o novo texto
        entry_1.tag_configure("big", font=("Helvetica", 24)) # Configura a fonte maior
        entry_1.tag_add("big", "1.0", "end") # Aplica a tag “big” a todo o texto
        
    def set_descanso():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        entry_1.insert("1.0", "DESCANSO")  # Insere o novo texto
        entry_1.tag_configure("big", font=("Helvetica", 24)) # Configura a fonte maior
        entry_1.tag_add("big", "1.0", "end") # Aplica a tag “big” a todo o texto
        
    def set_comunicacao():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        entry_1.insert("1.0", "COMUNICAÇÃO")  # Insere o novo texto
        entry_1.tag_configure("big", font=("Helvetica", 24)) # Configura a fonte maior
        entry_1.tag_add("big", "1.0", "end") # Aplica a tag “big” a todo o texto
    
    def set_atividade():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        entry_1.insert("1.0", "ATIVIDADE")  # Insere o novo texto
        entry_1.tag_configure("big", font=("Helvetica", 24)) # Configura a fonte maior
        entry_1.tag_add("big", "1.0", "end") # Aplica a tag “big” a todo o texto
        
    def set_apagar():
        entry_1.delete("1.0", "end")  # Limpa o conteúdo existente
        
    canvas = Canvas(
        needs_window,
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
        text="Necessidades",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 40 * -1)
    )

    canvas.create_text(
        180.0,
        335.0,
        anchor="nw",
        text="AJUDA",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        365.0,
        335.0,
        anchor="nw",
        text="COMIDA",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        564.0,
        335.0,
        anchor="nw",
        text="BEBIDA",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        751.0,
        335.0,
        anchor="nw",
        text="BANHEIRO",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        726.0,
        498.0,
        anchor="nw",
        text="COMUNICAÇÃO",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        352.0,
        498.0,
        anchor="nw",
        text="DESCANSO",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        189.0,
        498.0,
        anchor="nw",
        text="DOR",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )

    canvas.create_text(
        546.0,
        498.0,
        anchor="nw",
        text="ATIVIDADE",
        fill="#FFFFFF",
        font=("BebasNeue Regular", 20 * -1)
    )
    
    # Criando botões
    button_image_banheiro = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_banheiro = Button(
        image=button_image_banheiro,
        borderwidth=0,
        highlightthickness=0,
        command=set_banheiro,
        relief="flat"
    )
    button_banheiro.place(
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
        command=lambda: print("button_2 clicked"),
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
        width=76.0,
        height=76.0
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

    button_image_bebida = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_bebida = Button(
        image=button_image_bebida,
        borderwidth=0,
        highlightthickness=0,
        command=set_bebida,
        relief="flat"
    )
    button_bebida.place(
        x=547.0,
        y=233.0,
        width=94.0,
        height=95.0
    )

    button_image_comida = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_comida = Button(
        image=button_image_comida,
        borderwidth=0,
        highlightthickness=0,
        command=set_comida,
        relief="flat"
    )
    button_comida.place(
        x=357.0,
        y=233.0,
        width=94.0,
        height=95.0
    )

    button_image_ajuda = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_ajuda = Button(
        image=button_image_ajuda,
        borderwidth=0,
        highlightthickness=0,
        command=set_ajuda,
        relief="flat"
    )
    button_ajuda.place(
        x=163.0,
        y=233.0,
        width=94.0,
        height=95.0
    )

    button_image_dor = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_dor = Button(
        image=button_image_dor,
        borderwidth=0,
        highlightthickness=0,
        command=set_dor,
        relief="flat"
    )
    button_dor.place(
        x=163.0,
        y=397.0,
        width=94.0,
        height=95.0
    )

    button_image_descanso = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_descanso = Button(
        image=button_image_descanso,
        borderwidth=0,
        highlightthickness=0,
        command=set_descanso,
        relief="flat"
    )
    button_descanso.place(
        x=357.0,
        y=397.0,
        width=94.0,
        height=95.0
    )

    button_image_atividade = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_atividade = Button(
        image=button_image_atividade,
        borderwidth=0,
        highlightthickness=0,
        command=set_atividade,
        relief="flat"
    )
    button_atividade.place(
        x=547.0,
        y=397.0,
        width=94.0,
        height=95.0
    )

    button_image_comunicacao = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_comunicacao = Button(
        image=button_image_comunicacao,
        borderwidth=0,
        highlightthickness=0,
        command=set_comunicacao,
        relief="flat"
    )
    button_comunicacao.place(
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
        command=lambda: navigate_to_home(needs_window),
        relief="flat"
    )
    button_navigate_back.place(
        x=910.0,
        y=98.0,
        width=77.0,
        height=77.0
    )

    needs_window.resizable(False, False)
    needs_window.mainloop()
    
# Função para voltar para janela Home
def navigate_to_home(current_window):
    current_window.destroy()
    import guiHome
    guiHome.open_home_window()
