import socket
import sys

HOST = '127.0.0.1'
PORT = 32007

file = open(sys.argv[1], 'r')

lines = file.readlines()

for x in range(7):
    line = lines[x]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(line.encode())
    data = s.recv(1024).decode()

    dataSplit = data.split(" ")

    if dataSplit[0] == "200":
        print("Result is " + dataSplit[1])
    else:
        print("Error %s: %s" %(dataSplit[0], dataSplit[1]))

    s.close()