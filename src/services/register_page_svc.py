from tkinter import messagebox
from services.database_svc import salvar_dados, carregar_dados
from views.messagebox_page_vws import show_message_box


def cadastrar_usuario(frame):

    nome = frame.entry_nome.get()
    sobrenome = frame.entry_sobrenome.get()
    email = frame.entry_email.get()
    senha = frame.entry_senha.get()
    confirmar_senha = frame.entry_confirmar_senha.get()

    dados = carregar_dados()

    if nome == '' or sobrenome == '' or email == '' or senha == '' or confirmar_senha == '':

        show_message_box(frame, 'Erro', 'Você deve preencher todos os campos.')
        return


    if confirmar_senha != senha:

        show_message_box(frame, 'Erro', 'Senhas não correspondem.')
        return


    if not frame.checkbox_var.get():

        show_message_box(frame, 'Erro', 'Você deve aceitar os Termos e Condições de Uso.')
        return


    else:

        for user_data in dados['users']:

            if user_data['email'] == email:

                show_message_box(frame, 'Aviso', 'Usuário já cadastrado.')
                return


        salvar_dados(nome, sobrenome, email, senha)
        show_message_box(frame, 'Informação', f'Usuário cadastrado com sucesso!\nLogin: {nome.lower()}.{sobrenome.lower()}')

        frame.entry_nome.delete(0, 'end')
        frame.entry_sobrenome.delete(0, 'end')
        frame.entry_email.delete(0, 'end')
        frame.entry_senha.delete(0, 'end')
        frame.entry_confirmar_senha.delete(0, 'end')
        frame.checkbox_var.set(False)
