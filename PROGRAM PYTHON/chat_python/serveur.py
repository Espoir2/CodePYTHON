from email import message
import socket
s = socket.socket()
s.connect(('169.254.192.240', 50007))
message = input("? ")
while message != 'Z':
    s.send(bytes(message, 'utf8'))
    message = input('? ')
s.send(b'Z')
s.close()