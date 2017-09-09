import email_Get
import telepot
from control_bot import control
from bot import *
import yt

class automatizer:
    def __init__(self, bot):
        self.bot = bot
        self.lista = None

    def email(self):
        msgs = email_Get.email_get()
        if msgs != None:
            for i in range (0, len(msgs)):
                try:
                    self.bot.sendMessage(367067376, text='{}'.format(msgs[i]))
                except:
                    self.bot.sendMessage(367067376, ('Não há email\'s'))
        return msgs

    def ler_email(self):
        msgs = email_Get.email_get()
        if msgs != None:
            for i in range(0, len(msgs)):
                try:
                    print(msgs[i])
                except:
                    pass
        return msgs
            
class comandos:
    def __init__(self, bot):
        self.bot = bot

    def info(self):
        print('info')
        return True

    def email(self, user_id):
        msgs = email_Get.email_get()
        if msgs != None:
            for i in range (0, len(msgs)):
                try:
                    self.bot.sendMessage(user_id, text='{}'.format(msgs[i]))
                except:
                    self.bot.sendMessage(user_id, ('Não há email\'s'))
    
    def musica(self, user_id, cantor, musica):
        canto = cantor
        music = musica
        self.lista = yt.youtube_search(canto + ' ' + music)
        musicas = self.lista[0]
        #self.bot.sendMessage(user_id, parse_mode='HTML', text='{}'.format(musicas))
        self.musicaesc(user_id, 0)
    
    def musicaesc(self, user_id, musica):
        music = musica
        self.bot.sendMessage(user_id, parse_mode='HTML', text='https://www.youtube.com/watch?v={}'.format(self.lista[1][int(music)]))