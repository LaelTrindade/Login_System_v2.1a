import customtkinter as ctk
from PIL import Image, ImageTk
from config.paths import ASSETS_IMAGES
from views.login_page_vws import login_frame
from views.register_page_vws import register_frame
from services.register_page_svc import cadastrar_usuario
from services.login_page_svc import realizar_login, logar_com_google, logar_com_facebook, esqueci_minha_senha


def login_screen():
    login_page = ctk.CTk()

    window_width = 600
    window_height = 500
    screen_width = login_page.winfo_screenwidth()
    screen_height = login_page.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height -  window_height) // 2

    login_page.geometry(f'{window_width}x{window_height}+{x}+{y}')
    ctk.set_appearance_mode('Light')

    login_page.title('Havenix')
    login_page.resizable(False, False)

    icon_img = ImageTk.PhotoImage(Image.open(ASSETS_IMAGES/'program_icon.png'))
    login_page.iconphoto(True, icon_img)

    background_image = ctk.CTkImage(
        dark_image = Image.open(ASSETS_IMAGES/'background_image_2.jpeg'),
        light_image = Image.open(ASSETS_IMAGES/'background_image_2.jpeg'),
        size = ((600, 500))
    )

    label_bg = ctk.CTkLabel(master = login_page,
        width = 0,
        height = 0,
        text = '',
        image = background_image
    )

    label_bg.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

    frame_login = login_frame(login_page)
    frame_register = register_frame(login_page)

    exibir_Login(frame_register, frame_login)

    frame_login.label_criar_conta.bind('<Button-1>', command = lambda e: exibir_Register(frame_login, frame_register))

    frame_register.retornar_button.bind('<Button-1>', command = lambda e: exibir_Login(frame_register, frame_login))
    frame_register.registrar_button.bind('<Button-1>', command = lambda e: cadastrar_usuario(frame_register))
    frame_register.google_button.bind('<Button-1>', command = lambda e: logar_com_google(frame_register))
    frame_register.facebook_button.bind('<Button-1>', command = lambda e: logar_com_facebook(frame_register))

    frame_login.login_button.bind('<Button-1>', command = lambda e: realizar_login(frame_login))
    frame_login.google_button.bind('<Button-1>', command = lambda e: logar_com_google(frame_login))
    frame_login.facebook_button.bind('<Button-1>', command = lambda e: logar_com_facebook(frame_login))
    frame_login.label_esqueci_minha_senha.bind('<Button-1>', command = lambda e: esqueci_minha_senha(frame_login))

    login_page.mainloop()


def exibir_Login(frame_register, frame_login):
    frame_register.grid_remove()

    frame_login.grid(row = 0, column = 0, padx = 20)

def exibir_Register(frame_login, frame_register):
    frame_login.grid_remove()

    frame_register.grid(row = 0,column = 0, sticky = 'nsew', padx = 10, pady = 10)