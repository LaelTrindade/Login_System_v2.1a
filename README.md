# Login System [v2.1a]

Sistema de autenticação desktop com interface moderna, desenvolvido em Python com CustomTkinter. Conta com telas de login e cadastro, persistência local de usuários e feedback visual customizado (sem os message boxes padrão do Tkinter).

> Projeto de estudo/portfólio, focado em praticar organização de código (separação em `views` e `services`), manipulação de arquivos JSON e construção de interfaces gráficas modernas com Python.

## ✨ Funcionalidades

- **Cadastro de usuário** com validação de campos obrigatórios, confirmação de senha e aceite de termos de uso
- **Login** com verificação de credenciais
- **Recuperação de senha** (fluxo de interface simulado)
- **Login social** com Google e Facebook (botões simulados, sem integração real)
- Alternância entre as telas de Login e Cadastro na mesma janela, sem recarregar o app
- Message boxes customizadas (CTkToplevel), substituindo os alerts padrão do Tkinter

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) — interface gráfica
- [Pillow (PIL)](https://python-pillow.org/) — manipulação de imagens
- JSON — persistência local dos dados de usuário (`database/data.json`)

## 📁 Estrutura do projeto

```
src/
├── main.py                    # Ponto de entrada da aplicação
├── config/
│   └── paths.py                # Caminhos de assets centralizados
├── database/
│   └── data.json               # Armazenamento local dos usuários cadastrados
├── services/
│   ├── database_svc.py         # Leitura/escrita dos dados de usuário
│   ├── login_page_svc.py       # Lógica de login, "esqueci senha" e login social
│   └── register_page_svc.py    # Lógica de cadastro e validações
├── views/
│   ├── screen.py                # Janela principal e transição entre telas
│   ├── login_page_vws.py        # Interface da tela de login
│   ├── register_page_vws.py     # Interface da tela de cadastro
│   └── messagebox_page_vws.py   # Message box customizada
└── assets/
    └── images/                  # Logos, ícone e imagens da interface
```

## ▶️ Como executar

1. Clone o repositório
   ```bash
   git clone <url-do-repositorio>
   cd "Sistema de Login [Moderno + Atualizado]/src"
   ```

2. Instale as dependências
   ```bash
   pip install customtkinter pillow
   ```

3. Execute o projeto
   ```bash
   python main.py
   ```

## ⚠️ Estado atual e limitações conhecidas

- O login com Google/Facebook é apenas visual — não há integração real de autenticação.
- A recuperação de senha simula o envio de e-mail, mas não dispara nenhum e-mail de verdade.
- As senhas são armazenadas em texto puro no `data.json` (sem hash) — adequado para fins de estudo, mas não recomendado para produção.
- As fontes usadas na interface (Inter / DejaVu Sans Condensed) podem variar de aparência entre Linux e Windows, dependendo das fontes instaladas no sistema.

## 🚀 Possíveis melhorias futuras

- Hash de senha (bcrypt ou hashlib) antes de salvar no banco de dados
- Validação de duplicidade também pelo `login` gerado, não só pelo e-mail
- Integração real com OAuth do Google/Facebook
- Migração da persistência de JSON para um banco de dados relacional (SQLite, por exemplo)

## 👤 Autor

Desenvolvido por Lael.
