import socket
import sys
import random

p = float(sys.argv[1])
random.seed(sys.argv[2])

HOST = '127.0.0.1'
PORT = 32007
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
while True:
    try:

        while True:
            equation, address = s.recvfrom(1024)
            equation = equation.decode()
            equation = equation.strip()

            if random.random() <= p:
                print("%s -> dropped" % (equation))
                break

            x = equation.split(" ")
            op = x[0]
            num1 = x[1]
            num2 = x[2]

            #wrong operators
            if op != "+" and op != "-" and op != "*" and op != "/":
                s.sendto("620 InvalidOperators".encode(), address)
                writing = "%s -> 620 -1\n" % (equation)
                sys.stdout.write(writing)
                break

            #checking if num1 is int
            try:
                int(num1)
            except ValueError:
                s.sendto("630 InvalidOperands".encode(), address)
                writing = "%s -> 630 -1\n" % (equation)
                sys.stdout.write(writing)
                break

            #checking if num2 is int
            try:
                int(num2)
            except ValueError:
                s.sendto("630 InvalidOperands".encode(), address)
                writing = "%s -> 630 -1\n" % (equation)
                sys.stdout.write(writing)
                break


            num1 = int(num1)
            num2 = int(num2)

            #division by zero
            if op == "/" and num2 == 0:
                s.sendto("630 DivisionByZero".encode(), address)
                writing = "%s -> 630 -1\n" % (equation)
                sys.stdout.write(writing)
                break

            #calculations
            if op == "+":
                sol = "200 " + str(num1+num2)
                s.sendto(sol.encode(), address)
                writing = "%s -> 200 %d\n" % (equation, num1 + num2)
                sys.stdout.write(writing)
                break
            if op == "-":
                sol = "200 " + str(num1 - num2)
                s.sendto(sol.encode(), address)
                writing = "%s -> 200 %d\n" % (equation, num1 - num2)
                sys.stdout.write(writing)
                break
            if op == "*":
                sol = "200 " + str(num1 * num2)
                s.sendto(sol.encode(), address)
                writing = "%s -> 200 %d\n" % (equation, num1 * num2)
                sys.stdout.write(writing)
                break
            if op == "/":
                sol = "200 " + str(float(num1) / num2)
                s.sendto(sol.encode(), address)
                writing = "%s -> 200 %s\n" % (equation, str(float(num1) / num2))
                sys.stdout.write(writing)
                break

    except KeyboardInterrupt:
        s.close()
        sys.exit(0)