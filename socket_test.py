#!/bin/env python3

import socket

host = "185.74.221.20"
port = 2101

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print("Connected to server:", host, port)

while True:
    message = input('Enter a message (or "exit" to quit): ')
    client_socket.send(message.encode("utf-8"))

    if message.lower() == "exit":
        break
client_socket.close()
