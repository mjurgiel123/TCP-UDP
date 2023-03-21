import socket
import sys

HOST = '127.0.0.1'
PORT = 32007

file = open(sys.argv[1], 'r')


lines = file.readlines()

for x in range(7):
    deadserver = False
    d = 0.1
    line = lines[x]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    data = ""
    address = ""

    while True:
        s.sendto(line.encode(), (HOST, PORT))
        s.settimeout(d)
        try:
            data, address = s.recvfrom(1024)
            break
        except socket.timeout:
            d = d * 2
            if d > 2:
                print("Request timed out: the server is dead")
                print("Error 300: the server is dead")
                deadserver = True
                break
            print("Request timed out: resending")




    if deadserver == True:
        s.close()
        continue

    data = data.decode()

    dataSplit = data.split(" ")

    if dataSplit[0] == "200":
        print("Result is " + dataSplit[1])
    else:
        print("Error %s: %s" % (dataSplit[0], dataSplit[1]))

    s.close()