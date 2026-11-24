from tkinter import messagebox
from src.services.database_svc import carregar_dados
from src.views.messagebox_page_vws import show_message_box


def realizar_login(frame):

    dados = carregar_dados()

    login = frame.entry_login.get()
    senha = frame.entry_senha.get()

    for data_users in dados['users']:

        if data_users['login'] == login and data_users['senha'] == senha:

            show_message_box(frame, 'Sucesso', f"Bem-vindo, {data_users['login']}!")
            frame.entry_login.delete(0, 'end')
            frame.entry_senha.delete(0, 'end')

            return

    show_message_box(frame, 'Erro', 'Login ou Senha inválidos.')


def esqueci_minha_senha(frame):

    show_message_box(frame, 'Esqueci minha senha', 'Informe o seu e-mail', True)



def logar_com_google(frame):

    show_message_box(frame, 'Entrar com Google', 'Logando...')

def logar_com_facebook(frame):

    show_message_box(frame, 'Entrar com Facebook', 'Logando...')