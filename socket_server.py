import socket
import sys
import main as robot
from google_trans_new import google_translator  

translate=google_translator()

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host='127.0.0.1'
port=8888

server.bind((host,port))
server.listen()


con,address=server.accept()
while True:
    data=con.recv(1024)
    if not data:
        break
    trans=translate.translate(data.decode("utf-8"),lang_tgt='en')# translate the input to English before generate the answer
    reply= robot.makereply(trans)

    con.sendall(reply.encode("utf-8"))
con.close()