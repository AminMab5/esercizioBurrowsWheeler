import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

    client.connect(("127.0.0.1", 5000))

    messaggio = input("Inserisci una parola da trasformare: ")

    client.sendall(messaggio.encode())

    risposta = client.recv(1024).decode()

    print("La trasformata di Burrows Wheeler della parola", messaggio, "è:", risposta)