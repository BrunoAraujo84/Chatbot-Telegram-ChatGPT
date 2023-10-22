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
    git clone https://github.com/seu_usuario/seu_projeto.git
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
3. Adicione essa chave ao arquivo `.env` como uma nova variável chamada `OPENAI_API_KEY`.

## Configurando o Bot do Telegram

1. Fale com o [@BotFather](https://t.me/botfather) no Telegram para criar um novo bot e obter a chave da API.
2. Adicione a chave da API ao arquivo `.env`.
