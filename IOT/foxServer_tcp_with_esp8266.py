from socket import *
import time

Buffer = ""

server = socket(AF_INET, SOCK_STREAM)
server.bind(("", 8380))
while 1:
    server.listen(5)

    clientTar, clientAddr = server.accept()

    dev_id = clientTar.recv(1024).decode("utf-8")
    if dev_id == "OrangeWorkShopT00":
        if Buffer is not "":
            clientTar.send(Buffer.encode("utf-8"))

    time.sleep(1000)
    clientTar.close()
