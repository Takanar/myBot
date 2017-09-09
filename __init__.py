import telepot, sys
from time import sleep
from telepot.loop import MessageLoop
from bot import *
from comandos import *
import schedule

TOKEN = sys.argv[1]
bot = telepot.Bot(TOKEN)
myBot = xBot(bot)
cmd = automatizer(bot)

if __name__ == '__main__':
	myBot.falar('Oi! Eu sou o bot')
	MessageLoop(bot, myBot.handle).run_as_thread()
	schedule.every().day.at("13:00").do(cmd.email)
	while True:
		myBot.ouvir()
while True:	
	sleep(100)