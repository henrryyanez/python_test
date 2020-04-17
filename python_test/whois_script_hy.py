import sys
import socket
from datetime import datetime as dt
import time

def whois(ip):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.arin.net", 43))
    s.send(('n ' + ip + '\r\n').encode())

    response = b""
    print(s)

    # setting time limit in secondsmd
    startTime = time.mktime(dt.now().timetuple())
    timeLimit = 6
    while True:
        elapsedTime = time.mktime(dt.now().timetuple()) - startTime
        data = s.recv(4096)
        response += data
        if (not data) or (elapsedTime >= timeLimit):
            break
    s.close()

    print(response.decode())
    
def main():
    nombre = "ip.txt"
    with open(nombre, "r") as archivo:
        for linea in archivo:
        #domain = sys.argv[1];
            ip = socket.gethostbyname("linea")#;
            whois(ip)
            #print(ip)
main()
