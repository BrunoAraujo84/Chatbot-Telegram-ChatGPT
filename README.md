[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/BrunoAraujo84/Chatbot-Telegram-ChatGPT/blob/main/LICENSE) ![GitHub top language](https://img.shields.io/github/languages/top/BrunoAraujo84/Chatbot-Telegram-ChatGPT) ![GitHub last commit](https://img.shields.io/github/last-commit/BrunoAraujo84/Chatbot-Telegram-ChatGPT) ![Contribuições bem-vindas](https://img.shields.io/badge/contribuições-bem_vindas-brightgreen.svg?style=flat)

# Chatbot do Telegram com OpenAI

## Descrição
Projeto desenvolvido por Bruno Araujo, este projeto é um chatbot do Telegram desenvolvido em Python. Ele usa a API GPT da OpenAI para gerar respostas mais humanas e inteligentes.

## Requisitos

### Bibliotecas Python
Para rodar o código, você precisa instalar as seguintes bibliotecas Python:

- python-dotenv
- openai
- pyTelegramBotAPI

Você pode instalar todas elas usando o pip:

```bash
pip install python-dotenv openai pyTelegramBotAPI
```

### Variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

- `API_KEY_TELEGRAM_PROD`: Sua chave de API do Telegram para o ambiente de produção.
- `API_KEY_TELEGRAM_TEST`: Sua chave de API do Telegram para o ambiente de teste (opcional).
- `API_KEY_OPENAI`: Sua chave de API da OpenAI

## Como usar

1. Clone o repositório:

    ```bash
    git clone https://github.com/BrunoAraujo84/Chatbot-Telegram-ChatGPT.git
    ```

2. Entre na pasta do projeto:

    ```bash
    cd seu_projeto
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Execute o script:

    ```bash
    python Chatbot_Telegram.py
    ```

## Configurando a API da OpenAI

1. Visite o [site da OpenAI](https://www.openai.com/) e crie uma conta.
2. Navegue até a seção de API e gere uma chave de API.
3. Adicione essa chave ao arquivo `.env` como uma nova variável chamada `API_KEY_OPENAI`.
4. A API ofereceido pela OpenAI é um serviço pago.

## Configurando o Bot do Telegram

1. Utilize o [@BotFather](https://t.me/botfather) no Telegram para criar um novo bot e obter a chave da API.
2. Adicione a chave da API ao arquivo `.env`.

## Exemplo do bot em funcionamento
Acesse o link [site do LinkedIn](https://www.linkedin.com/posts/bruno-araujo-de-oliveira_ai-inteligaeanciaartificial-python-activity-7022927829541490690-Bpl9?utm_source=share&utm_medium=member_desktop) para visualizar o post publicado por mim demonstrando como funciona o bot em um video.