from pytube import YouTube
import validators
import socket
import threading

HOST = '127.0.0.1'
PORT = 60000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('Aguardando conexão de um cliente')


def server(conn, ender):
    print(f"conectado em {ender}")
    while True:
        print("Pronto pra receber arquivo")
        data = conn.recv(1024).decode()
        validador = validators.url(data)
        if validador == True:
            print("Baixando arquivo...")
            yt = YouTube(data)
            yt.streams.first().download()
            print("baixou")
            conn.send(str.encode(yt.title))
            file = open(yt.title+".mp4", 'rb')
            file_data = file.read(1000000)
            conn.send(file_data)
        else:
            resposta = 'erro'
            conn.send(str.encode(resposta))


while True:
    try:
        con, cliente = s.accept()
    except:
        break
    threading.Thread(target=server, args=(con, cliente)).start()
