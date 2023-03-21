import socket
import sys

HOST = '127.0.0.1'
PORT = 32007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

while True:
    try:
        s.listen(2)

        c, addr = s.accept()
        while True:
            equation = c.recv(1024).decode()
            x = equation.split(" ")
            op = x[0]
            num1 = x[1]
            num2 = x[2]
            equation = equation.strip()
            #wrong operators
            if op != "+" and op != "-" and op != "*" and op != "/":
                c.send("620 InvalidOperator".encode())
                writing = "%s -> 620 -1\n" % (equation)
                sys.stdout.write(writing)
                break

            #checking if num1 is int
            try:
                int(num1)
            except ValueError:
                c.send("630 InvalidOperands".encode())
                writing = "%s -> 630 -1\n" % (equation)
                sys.stdout.write(writing)
                break

            #checking if num2 is int
            try:
                int(num2)
            except ValueError:
                c.send("630 InvalidOperands".encode())
                writing = "%s -> 630 -1\n" % (equation)
                sys.stdout.write(writing)
                break


            num1 = int(num1)
            num2 = int(num2)

            #division by zero
            if op == "/" and num2 == 0:
                c.send("630 DivisionByZero".encode())
                writing = "%s -> 630 -1\n" % (equation)
                sys.stdout.write(writing)
                break

            #calculations
            if op == "+":
                sol = "200 " + str(num1+num2)
                c.send(sol.encode())
                writing = "%s -> 200 %d\n" % (equation, num1 + num2)
                sys.stdout.write(writing)
                break
            if op == "-":
                sol = "200 " + str(num1 - num2)
                c.send(sol.encode())
                writing = "%s -> 200 %d\n" % (equation, num1 - num2)
                sys.stdout.write(writing)
                break
            if op == "*":
                sol = "200 " + str(num1 * num2)
                c.send(sol.encode())
                writing = "%s -> 200 %d\n" % (equation, num1 * num2)
                sys.stdout.write(writing)
                break
            if op == "/":
                sol = "200 " + str(float(num1) / num2)
                c.send(sol.encode())
                writing = "%s -> 200 %s\n" % (equation, str(float(num1) / num2))
                sys.stdout.write(writing)
                break

    except KeyboardInterrupt:
        s.close()
        sys.exit(0)

