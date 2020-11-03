import telegram

token = '1239560340:AAG90oSiaRuVzy56MUM_2dRpL9iEQuWFGzI'

bot = telegram.Bot(token=token)

chat_id = '1489946579'

bot.sendMessage(chat_id = chat_id, text="테스트")