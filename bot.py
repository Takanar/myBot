from comandos import *
import speech_recognition as sr
import pyttsx3
import subprocess
import re
from datetime import datetime
import yt

class xBot:
    def __init__(self, bot):
        self.bot = bot
        self.inst_comando = comandos(self.bot)
        self.comandoDict = {
            '/info' : self.inst_comando.info,
            '/email': self.inst_comando.email
            }
        self.resposta = 0
        self.lista_id = None

    def falar(self, palavra):
        en = pyttsx3.init()
        en.setProperty('voice',b'brazil')
        en.say(palavra)
        en.runAndWait()

    def ouvir(self):
        rec = sr.Recognizer()
        with sr.Microphone() as fala:
            frase = rec.listen(fala)
            try:
                vfala = rec.recognize_google(frase, language="pt")
                print(vfala)
                self.comando_voz(vfala)
            except:
                print("Não entendi")
                self.falar('nao entendi')
  
    def comando_voz(self, fala):
        inst_comando = automatizer(self.bot)
        if self.resposta == 0:
            vfala = fala
            if vfala == 'ver info':
                info = 'Bot em desenvolvimento'
                self.falar(info)
                print(info)
            elif vfala == 'ler e-mail':
                email = inst_comando.ler_email()
                for i in range(0, len(email)):
                    v = False
                    while v == False:
                        self.falar(re.sub('[^A-Za-z0-9]+','',email[i]))
                        v = True
            elif vfala == 'quantas horas':
                hora = datetime.now().strftime('%H:%M:%S')
                print(hora)
                self.falar(hora)
            elif vfala == 'pesquisar música':
                self.resposta = 1
                self.falar('qual musica deseja ouvir?')
            elif vfala == 'ajuda':
                ajuda = 'Tenho varios comandos. ver Info, ver e-mail, ouvir musica, parar musica, abrir internet e fechar internet'
                self.falar(ajuda)
            elif vfala == 'ouvir música':
                p = subprocess.Popen('"C:/Program Files (x86)/Windows Media Player/wmplayer.exe" "C:/Users/Dyganar/Music/Playlists/Acústico.wpl"')
            elif vfala == 'Parar música':
                p.kill()
            elif vfala == 'Abrir internet':
                q = subprocess.Popen("C:/Program Files (x86)/Mozilla Firefox/firefox.exe")
        elif self.resposta == 1:
            vfala = fala
            lista = yt.youtube_search(vfala)
            lista_nomes = lista[0]
            self.lista_id = lista[1]
            for i in range (0, len(lista_nomes)):
                print("{}: {}".format(i, lista_nomes[i]))
            self.resposta = 2

        elif self.resposta == 2:
            vfala = fala
            q = subprocess.Popen("C:/Program Files (x86)/Mozilla Firefox/firefox.exe https://www.youtube.com/watch?v=%s"%(self.lista_id[int(vfala)]))
            print("Tocando música...")
            self.resposta = 0
            
    def handle(self, msg):
        texto = msg['text'].split(' ')
        ctexto = texto[0].lower()
        user_id = msg['from']['id']
        try:
            cantor = texto[1]
            musica = texto[2]
        except:
            pass
        content_type, chat_type, chat_id = telepot.glance(msg)
        if self.resposta == 0:
            if ctexto == '/musica':
                self.inst_comando.musica(user_id=user_id, cantor=cantor, musica=musica)
                #self.resposta = 1
            elif self.comandoDict.get('/info'):
                self.comandoDict[ctexto](user_id)
            elif self.comandoDict.get('/email'):
                self.comandoDict[ctexto](user_id)
            
        elif self.resposta == 1:
            self.resposta = 0
            self.inst_comando.musicaesc(user_id, ctexto)
            
