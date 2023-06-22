import sys
import socket
from tendo import singleton
from _thread import start_new_thread
import psutil
import time
from time import gmtime, strftime
FORMAT = "utf-8"


def threaded(user):
    while True:
        try:
            while True:
                print("Client connected")
                command_choose = user.recv(1024).decode(FORMAT)

                if command_choose == "1":
                    virtual_mem = psutil.swap_memory()
                    user.sendall(f"Server 2 priority: "
                                 f"% of usage of virtual memory is {virtual_mem.percent}% { strftime('%H:%M:%S', gmtime())} \n".encode("utf-8"))

                elif command_choose == "2":
                    physic_mem = psutil.virtual_memory()
                    user.sendall(f"% of usage of physical memory is {physic_mem.percent}% { strftime('%H:%M:%S', gmtime())} \n ".encode("utf-8"))

                elif command_choose == "exit":
                    user.sendall(
                        f"%Disconnected at {strftime('%H:%M:%S', gmtime())} \n ".encode(
                            "utf-8"))
                    raise EOFError



        except BaseException:
            time.sleep(3)
            print("Client disconnected\n")
            break


    user.close()

def main():
    # Проверка на создание более одного сервера
    try:
        me = singleton.SingleInstance()
    except:
        sys.exit()



    #Устанавливаем адрес и порт
    HOST = ""  # Standard loopback interface address (localhost)
    PORT = 8000  # Port to listen on (non-privileged ports are > 1023)
    PORT2 = 8888



    #Выполняем прослушивание порта
    server2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server2.bind((HOST, PORT2))
    server2.listen()


    while True:
        user, address = server2.accept()
        start_new_thread(threaded, (user, ))

    server2.close()
    return 0

if __name__ == "__main__":
    main()
