import telepot

class control:
    def __init__(self, bot, msg):
        self.bot = bot
        self.user_id = msg['from']['id']