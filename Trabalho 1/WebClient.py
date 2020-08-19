# -*- coding: utf-8 -*-

from socket import *
import sys

serverHost = '127.0.0.1'
serverPort = 6789
filename = sys.argv[1]

clientSocket = socket(AF_INET, SOCK_STREAM)
try:
    clientSocket.connect((serverHost, int(serverPort)))
except: 
    print("O servidor não está disponível.")
    clientSocket.close()
    sys.exit()
print("Conexão bem-sucedida.")

httpRequest = "GET /" + filename + " HTTP/1.1\r\n\r\n"
clientSocket.send(httpRequest.encode())
print("Requisição enviada.")

print("Resposta HTTP do servidor:\r\n")

data = ""
while True:
    clientSocket.settimeout(5)
    newData = clientSocket.recv(1024).decode()
    data += newData
    if (len(newData) == 0):
        break
print(data)

print("Fechando socket.")
clientSocket.close()
