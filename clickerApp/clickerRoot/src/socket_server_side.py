import socket

from django.db.models import Sum

from ..models import User
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('https://djangoclickers.herokuapp.com', 9005)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(100)


def run():
    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                # data = connection.recv(16)
                # print('received {!r}'.format(data))
                # if data:
                print('sending data back to the client')
                global_counter = User.objects.all().aggregate(Sum('counter'))['counter__sum']
                connection.sendall(bytes(global_counter))
            # else:
            #     print('no data from', client_address)
            #     break

        finally:
            # Clean up the connection
            connection.close()

