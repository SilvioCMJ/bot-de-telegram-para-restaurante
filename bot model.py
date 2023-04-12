import telebot

key = 'KEY DO BOT'
# criando bot
bot = telebot.TeleBot(key)


@bot.message_handler(commands=['pizza'])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, 'Pedido aceito, Sua pizza chegará em 40 min')


@bot.message_handler(commands=['hamburguer'])
def hamburger(mensagem):
    bot.send_message(mensagem.chat.id, 'Pedido aceito, Sua hamburguer chegará em 40 min')


@bot.message_handler(commands=['salada'])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, 'nao tem salada, clique /iniciar')


@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    texto = '''O que você vai querer?(CLIQUE EM UMA OPÇÃO)
        /pizza
        /hamburguer
        /salada'''

    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, 'para enviar uma reclamação, mande um email para teste@gmail.com')


@bot.message_handler(commands=['opcao3'])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, 'SALVE RATO')


# func do bot
def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (CLIQUE NO ITEM)
        /opcao1 Fazer um pedido
        /opcao2 Reclamar de um pedido
        /opcao3 Da um alo ae parça
    Responder qualquer outra coisa não vai funcionar, selecione uma das opções    
            """
    bot.reply_to(mensagem, texto)


bot.polling()
