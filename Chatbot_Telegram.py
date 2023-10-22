# 'É PRECISO IMPORTAR AS BIBLIOTECAS:
# pip install python-dotenv
# pip install openai
# pip install pyTelegramBotAPI

# INFORMAÇÕES DETALHADA DE UM VALIDADOR
import telebot
import openai
import os
from dotenv import load_dotenv

# CARREGANDO AS VARIÁVEIS QUE ESTÃO NO ARQUIVO .env
load_dotenv()

# CHAVE BOT - TELEGRAM
chave_api = os.environ.get("API_KEY_TELEGRAM_PROD")

# Ambiente de Teste - TELEGRAM
# chave_api = os.environ.get("API_KEY_TELEGRAM_TEST")

# CRIANDO A INTEGRAÇÃO DO BOT - TELEGRAM
bot = telebot.TeleBot(chave_api)

# CHAVE CONTA - OPENAI
openai.api_key = os.environ.get("API_KEY_OPENAI")

# VARIÁVEIS DE APOIO
texto = ""
resposta = ""
resultado = ""


# TODAS AS MENSAGENS CONSIDERAR - TELEGRAM
def verificar(mensagem):
    if mensagem.text != "/start":
        if mensagem.text != "\start":
            return True


# INFORMA QUANDO ESTA FUNÇÃO SERÁ EXECUTADA
@bot.message_handler(func=verificar)
# FUNÇÃO RESPONDENDO A RESPOSTA
def responder(mensagem):

    # MENSAGEM ESCRITA TELEGRAM
    texto = mensagem.text

    # RESPOSTA DO CHAT DE INTELIGENCIA ARTIFICIAL - OPENAI
    resposta = openai.Completion.create(engine="text-davinci-003", prompt=texto, max_tokens=2048, n=1, stop=None,
                                        temperature=0, )

    resultado = resposta["choices"][0]["text"]

    # ENVIANDO MENSAGEM COM UMA DAS OPÇÕES ACIMA PARA INTERAGIR COM O USUÁRIO
    bot.reply_to(mensagem, resultado)


print("Preparado!")
# LOOP INFINITO PARA OUVIR AS MENSAGENS
bot.polling()
