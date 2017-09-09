def falar(fala):
    vfala = fala
    if vfala == 'ver info':
        info = 'Bot em desenvolvimento'
        self.falar(info)
        print(info)
    elif vfala == 'quantas horas':
        hora = datetime.now().strftime('%H:%M:%S')
        self.falar(hora)
    elif vfala == 'ver e-mail':
        email = inst_comando.ler_email()
        for i in range(0, len(email)):
            v = False
            while v == False:
                self.falar(re.sub('[^A-Za-z0-9]+','',email[i]))
                v = True

    elif vfala == 'ajuda':
        ajuda = 'Tenho dois comandos. ver Info, ver e-mail, ouvir música, parar música, abrir internet e fechar internet'
        self.falar(ajuda)
    elif vfala == 'ouvir música':
        p = subprocess.Popen('"C:/Program Files (x86)/Windows Media Player/wmplayer.exe" "C:/Users/Dyganar/Music/Playlists/Acústico.wpl"')
    elif vfala == 'Parar música':
        p.kill()
    elif vfala == 'Abrir internet':
        q = subprocess.Popen("C:/Program Files (x86)/Mozilla Firefox/firefox.exe")