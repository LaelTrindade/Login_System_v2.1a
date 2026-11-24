import customtkinter as ctk
from PIL import Image
from src.config.paths import ASSETS_IMAGES


def login_frame(parent):

    frame_1 = ctk.CTkFrame(master = parent,
        width = 350,
        height = 420,
        corner_radius = 20,
        fg_color = '#FFFFFF',
        bg_color = '#b49ab5'
    )

    parent.grid_rowconfigure(0, weight = 1)
    parent.grid_columnconfigure(0, weight = 1)

    frame_1.pack_propagate(False)

    img_1 = ASSETS_IMAGES/'Havenix_logo.png'

    image_1 = ctk.CTkImage(
        dark_image = Image.open(img_1),
        light_image = Image.open(img_1),
        size = ((100, 25))
    )

    label_img1 = ctk.CTkLabel(master = frame_1,
        text = '',
        image = image_1
    )

    label_img1.place(relx = 0.5, rely = 0.11, anchor = 'center')

    label_1 = ctk.CTkLabel(master = frame_1,
        text = 'Bem-vindo de volta!',
        font = ('Inter', 22, 'bold')
    )

    label_1.pack(pady = (70, 2))

    label_2 = ctk.CTkLabel(master = frame_1,
        text = 'Faça login para aproveitar ofertas incríveis.',
        font = ('DejaVu Sans Condensed', 10),
        width = 0,
        height = 0
    )

    label_2.pack()

    img_2 = ASSETS_IMAGES/'google_logo.jpg'

    button_image_1 = ctk.CTkImage(
        dark_image = Image.open(img_2),
        light_image = Image.open(img_2),
        size = (15, 15)
    )

    button_1 = ctk.CTkButton(frame_1,
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

    button_1.pack(pady = (20, 0))

    img_3 = ASSETS_IMAGES/'facebook_logo.jpeg'

    button_image_2 = ctk.CTkImage(
        dark_image = Image.open(img_3),
        light_image = Image.open(img_3),
        size = (15, 15)
    )

    button_2 = ctk.CTkButton(frame_1,
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

    button_2.pack(pady = (5, 0))

    label_3 = ctk.CTkLabel(frame_1,
        text = ('─'*19, 'ou', '─'*19),
        font = ('Inter', 10)
    )

    label_3.pack(pady = (10, 0))

    label_4 = ctk.CTkLabel(master = frame_1,
        text = 'Login',
        font = ('Inter', 10),
        width = 0,
        height = 0
    )

    label_4.pack(padx = 52, pady = (5, 0), anchor = 'w')

    entry_1 = ctk.CTkEntry(master = frame_1,
        width = 250,
        height = 20,
        border_width = 1,
        corner_radius = 5,
        font = ('DejaVu Sans Condensed', 10)
    )

    entry_1.pack(pady = (1, 0))

    label_5 = ctk.CTkLabel(master = frame_1,
        text = 'Senha',
        font = ('Inter', 10),
        width = 0,
        height = 0
    )

    label_5.pack(padx = 52, pady = (5, 0), anchor = 'w')

    entry_2 = ctk.CTkEntry(master = frame_1,
        width = 250,
        height = 20,
        border_width = 1,
        corner_radius = 5,
        font = ('DejaVu Sans Condensed', 10),
        show = '•'
    )

    entry_2.pack(pady = (1, 0))

    label_6 = ctk.CTkLabel(master = frame_1,
        text = 'Esqueci minha senha',
        font = ('Inter', 10, 'underline'),
        width = 0,
        height = 0,
        cursor = 'hand2'
    )

    label_6.pack(padx = 52, pady = (2, 0), anchor = 'e',)

    button_3 = ctk.CTkButton(frame_1,
        width = 150,
        height = 25,
        corner_radius = 10,
        text = 'Login',
        font = ('Inter', 14, 'bold'),
        text_color = 'white',
        cursor = 'hand2',
        fg_color = '#5d3452',
        hover_color = '#754363'
    )

    button_3.pack(pady = (20, 0))

    frame_2 = ctk.CTkFrame(frame_1,
        width = 175,
        height = 25,
        fg_color = 'transparent'
    )

    frame_2.pack(pady = (4, 0))

    label_7 = ctk.CTkLabel(frame_2,
        text = 'Não possui uma conta?',
        font = ('Inter', 8),
        width = 0,
        height = 0
    )

    label_7.pack(side = 'left')

    label_8 = ctk.CTkLabel(frame_2,
        text = 'Criar conta',
        font = ('Inter', 8, 'underline'),
        width = 0,
        height = 0,
        cursor = 'hand2'
    )

    label_8.pack(padx = (2, 0), side = 'left')

    frame_1.label_criar_conta = label_8

    frame_1.entry_login = entry_1
    frame_1.entry_senha = entry_2

    frame_1.login_button = button_3

    frame_1.google_button = button_1
    frame_1.facebook_button = button_2

    frame_1.label_esqueci_minha_senha = label_6

    return frame_1