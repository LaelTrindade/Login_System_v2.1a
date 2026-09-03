import customtkinter as ctk
from PIL import Image
from config.paths import ASSETS_IMAGES

def register_frame(parent):

    parent.grid_rowconfigure(0, weight = 1)
    parent.grid_columnconfigure(0, weight = 1)

    frame_1 = ctk.CTkFrame(master = parent,
        width = 550,
        height = 450,
        corner_radius = 20,
        fg_color = '#FFFFFF',
        bg_color = '#745983'
    )

    frame_1Aux = ctk.CTkFrame(frame_1,
        width = 280,
        height = 400,
        corner_radius = 20,
        fg_color = 'transparent'
    )

    frame_1.grid_rowconfigure(0, weight = 1),
    frame_1.grid_columnconfigure(0, weight = 0)

    frame_1Aux.grid(row = 0, column = 0, sticky = 'nsw', padx = (10, 0), pady = 20)

    img = ctk.CTkImage(
        light_image = Image.open(ASSETS_IMAGES/'register_screen_image_3.png'),
        dark_image = Image.open(ASSETS_IMAGES/'register_screen_image_3.png'),
        size = ((250, 320))
    )

    label_img = ctk.CTkLabel(frame_1Aux,
        text = '',
        image = img
    )

    label_img.grid(row = 0, column = 0, sticky = 'nsew', padx = 5, pady = (60, 0))

    frame_2 = ctk.CTkFrame(frame_1,
        width = 280,
        height = 380,
        corner_radius = 20,
        border_width = 1,
        border_color = '#BFBFBF',
        fg_color = '#FFFFFF'
    )

    frame_2.grid(row = 0, column = 1, sticky = 'nsew', padx = (20, 0), pady = 15)

    label_title = ctk.CTkLabel(frame_2,
        width = 0,
        height = 0,
        text = 'Vamos começar?',
        font = ('Inter', 24, 'bold')
    )

    frame_2.grid_propagate(False)

    frame_2.grid_rowconfigure(0, weight = 0)
    frame_2.grid_columnconfigure(0, weight = 1)

    label_title.grid(row = 0, column = 0, sticky = 'n', padx = 5, pady = (30, 0), columnspan = 2)

    label_subtitle = ctk.CTkLabel(frame_2,
        width = 0,
        height = 0,
        text = 'Crie sua conta e tenha acesso a todos \nos recursos da plataforma.',
        font = ('DejaVu Sans Condensed', 10)
    )

    label_subtitle.grid(row = 1, column = 0, sticky = 'n', padx = 5, pady = 0, columnspan = 2)

    label_1 = ctk.CTkLabel(frame_2,
        width = 0,
        height = 0,
        text = 'Nome',
        font = ('Inter', 12, 'bold')
    )

    label_1.grid(row = 2, column = 0, sticky = 'nw', padx = (25, 0), pady = (20, 0))

    entry_1 = ctk.CTkEntry(frame_2,
        width = 100,
        height = 20,
        border_width = 1,
        corner_radius = 5,
        font = ('DejaVu Sans Condensed', 10)
    )

    entry_1.grid(row = 3, column = 0, sticky = 'nw', padx = (25, 0))

    label_2 = ctk.CTkLabel(frame_2,
        width = 0,
        height = 0,
        text = 'Sobrenome',
        font = ('Inter', 12, 'bold')
    )

    label_2.grid(row = 2, column = 1, sticky = 'nw', padx = (0, 25), pady = (20, 0))

    entry_2 = ctk.CTkEntry(frame_2,
        width = 100,
        height = 20,
        border_width = 1,
        corner_radius = 5,
        font = ('DejaVu Sans Condensed', 10)
    )

    entry_2.grid(row = 3, column = 1, sticky = 'nw', padx = (0, 25))

    label_3 = ctk.CTkLabel(frame_2,
        width = 0,
        height = 0,
        text = 'E-mail',
        font = ('Inter', 12, 'bold')
    )

    label_3.grid(row = 4, column = 0, sticky = 'nw', padx = 25, pady = (5, 0))

    entry_3 = ctk.CTkEntry(frame_2,
        width = 250,
        height = 20,
        border_width = 1,
        corner_radius = 5,
        font = ('DejaVu Sans Condensed', 10)
    )

    entry_3.grid(row = 5, column = 0, sticky = 'nw', padx = 25, columnspan = 2)

    label_4 = ctk.CTkLabel(frame_2,
        width = 0,
        height = 0,
        text = 'Senha',
        font = ('Inter', 12, 'bold')
    )

    label_4.grid(row = 6, column = 0, sticky = 'nw', padx = 25, pady = (5, 0))

    entry_4 = ctk.CTkEntry(frame_2,
        width = 250,
        height = 20,
        show = '•',
        border_width = 1,
        corner_radius = 5,
        font = ('DejaVu Sans Condensed', 10)
    )

    entry_4.grid(row = 7, column = 0, sticky = 'nw', padx = 25, columnspan = 2)

    label_5 = ctk.CTkLabel(frame_2,
        width = 0,
        height = 0,
        text = 'Confirmar senha',
        font = ('Inter', 12, 'bold')
    )

    label_5.grid(row = 8, column = 0, sticky = 'nw', padx = 25, pady = (5, 0))

    entry_5 = ctk.CTkEntry(frame_2,
        width = 250,
        height = 20,
        show = '•',
        border_width = 1,
        corner_radius = 5,
        font = ('DejaVu Sans Condensed', 10)
    )

    entry_5.grid(row = 9, column = 0, sticky = 'nw', padx = 25, columnspan = 2)

    checkbox_var = ctk.BooleanVar(value = False)
    checkbox = ctk.CTkCheckBox(frame_2,
        checkbox_width = 10,
        checkbox_height = 10,
        text = 'Concordo com os Termos e Condições de Uso.',
        font = ('DejaVu Sans Condensed', 9),
        fg_color = '#5d3452',
        hover_color = '#754363',
        variable = checkbox_var
    )

    checkbox.grid(row = 10, column = 0, sticky = 'nw', padx = 28, columnspan = 2)

    button_register = ctk.CTkButton(frame_2,
        width = 150,
        height = 25,
        text = 'Registrar-se',
        font = ('Inter', 12, 'bold'),
        corner_radius = 10,
        text_color = 'white',
        fg_color = '#5d3452',
        hover_color = '#754363',
        cursor = 'hand2'
    )

    button_register.grid(row = 11, column = 0, sticky = 'n', padx = 20, pady = (10, 0), columnspan = 2)

    label_6 = ctk.CTkLabel(frame_2,
        text = ('─'*19, 'ou', '─'*19),
        font = ('Inter', 10),
        width = 0,
        height = 0
    )

    label_6.grid(row = 12, column = 0, sticky = 'nsew', padx = 25, pady = (15, 0), columnspan = 2)

    img_2 = ASSETS_IMAGES/'google_logo.jpg'

    button_image_1 = ctk.CTkImage(
        dark_image = Image.open(img_2),
        light_image = Image.open(img_2),
        size = (15, 15)
    )

    button_1 = ctk.CTkButton(frame_2,
        width = 250,
        height = 25,
        text = 'Entrar com Google',
        font = ('Inter', 12),
        corner_radius = 10,
        fg_color = 'transparent',
        hover_color = '#F0F0F0',
        border_color = 'gray',
        text_color = 'black',
        border_width = 1,
        image = button_image_1
    )

    button_1.grid(row = 13, column = 0, padx = 20, pady = (15, 0), sticky = 'nsew', columnspan = 2)

    img_3 = ASSETS_IMAGES/'facebook_logo.jpeg'

    button_image_2 = ctk.CTkImage(
        dark_image = Image.open(img_3),
        light_image = Image.open(img_3),
        size = (15, 15)
    )

    button_2 = ctk.CTkButton(frame_2,
        width = 250,
        height = 25,
        text = 'Entrar com Facebook',
        font = ('Inter', 12),
        corner_radius = 10,
        fg_color = 'transparent',
        hover_color = '#F0F0F0',
        border_color = 'gray',
        text_color = 'black',
        border_width = 1,
        image = button_image_2
    )

    button_2.grid(row = 14, column = 0, sticky = 'nsew', padx = 20, pady = (5, 0), columnspan = 2)

    button_3 = ctk.CTkButton(frame_1Aux,
        width = 24,
        height = 24,
        corner_radius = 12,
        font = ('Inter', 14, 'bold'),
        text_color = 'white',
        fg_color = '#5d3452',
        hover_color = '#754363',
        border_spacing = 0,
        cursor = 'hand2',
        text = '«'
    )

    button_3.grid(row = 0, column = 0, sticky = 'nw', padx = 5, pady = 5)

    frame_1.retornar_button = button_3
    frame_1.registrar_button = button_register

    frame_1.entry_nome = entry_1
    frame_1.entry_sobrenome = entry_2
    frame_1.entry_email = entry_3
    frame_1.entry_senha = entry_4
    frame_1.entry_confirmar_senha = entry_5

    frame_1.checkbox_var = checkbox_var

    frame_1.google_button = button_1
    frame_1.facebook_button = button_2

    return frame_1