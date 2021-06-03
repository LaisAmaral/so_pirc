import socket


HOST = '127.0.0.1'
PORT = 60000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
     print("Insira a url do vídeo que deseja baixar: Enter para encerrar")
     b = input("> ")
     if b == "":
          break
     s.send(str.encode(b))
     data = s.recv(1024).decode()
     print(data)
     if data != 'erro':
          namefile = data
          print(f'Baixando o vídeo: {namefile}')
          file = open(f'{namefile}.mp4', 'wb')
          file_data = s.recv(1000000)
          file.write(file_data)
          file.close()
          print("Arquivo recebido")
     else:
          print("Url invalida")