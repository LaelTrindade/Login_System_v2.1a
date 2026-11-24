import os
import json
from src.config.paths import BASE_DIR

PATH = BASE_DIR/'database'/'data.json'

os.makedirs(os.path.dirname(PATH), exist_ok = True)

def carregar_dados():
    try:
        with open(PATH, 'r') as f:
            return json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        return {'users': []}

def salvar_dados(nome, sobrenome, email, senha):

    login = f'{nome}.{sobrenome}'.lower()

    user_data = {

        "nome": nome,
        "sobrenome": sobrenome,
        "email": email,
        "senha": senha,
        "login": login

    }

    data = carregar_dados()
    data['users'].append(user_data)

    with open(PATH, 'w') as f:
        json.dump(data, f, indent = 4)