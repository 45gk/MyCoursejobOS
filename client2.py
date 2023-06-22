import socket
HOST = ""  # The server's hostname or IP address
PORT = 8000  # The port used by the server
PORT2 = 8888
FORMAT = "utf-8"


def main():
    # window_client = Tk()
    # window_client.title("Server 1")
    # window_client.geometry('400x250')

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_choose = input("Which server do you want to connect to or write \"exit\" to disconnect: ")
    # Если выбран первый сервер
    if server_choose == "1":
        port = PORT
        client.connect((HOST, port))
        while True:
            server1_choose = input("Last error (1) or cursor coordinates (2) or write \"exit\" to disconnect: ")
            if server1_choose == "1":
                client.send(server1_choose.encode("utf-8"))
                data = client.recv(1024).decode("utf-8")
                print(f"{data}")
            elif server1_choose == "2":
                client.send(server1_choose.encode(FORMAT))
                data = client.recv(1024).decode("utf-8")
                print(f"{data}")
            elif server1_choose == "exit":
                client.send(server1_choose.encode(FORMAT))
                data = client.recv(1024).decode("utf-8")
                print(f"{data}")
                break

            else:
                break
    # Если выбран второй сервер
    elif server_choose == "2":
        port = PORT2
        client.connect((HOST, port))
        while True:
            server2_choose = input("Procent of usage of virtual memory(1) or physical memory(2) or write \"exit\" to disconnect: ")
            if server2_choose == "1":
                client.send(server2_choose.encode(FORMAT))
                data = client.recv(1024).decode(FORMAT)
                print(data)
            elif server2_choose == "2":
                client.send(server2_choose.encode(FORMAT))
                data = client.recv(1024).decode(FORMAT)
                print(data)
            elif server2_choose == "exit":
                client.send(server2_choose.encode(FORMAT))
                data = client.recv(1024).decode("utf-8")
                print(f"{data}")
                break

            else:
                break
    elif server_choose == "exit":
        client.close()

    client.close()


if __name__ == "__main__":
    main()
