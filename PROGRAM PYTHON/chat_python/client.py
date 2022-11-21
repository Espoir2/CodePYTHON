import socket
s = socket.socket()
s.bind(('', 50007))
s.listen(1)
client, adresse = s.accept()
print('connecté avec ', adresse)
message = client.recv(1024).decode('utf8')
while message != 'Z':
    print(message)
    message = client.recv(1024).decode('utf8')
s.close()
client.close()