from tkinter import *
import socket

import win32api
from tendo import singleton
from time import gmtime, strftime
from _thread import start_new_thread
import time

FORMAT = "utf-8"


def threaded(user):
    while True:
        try:
            while True:
                print("Client connected")
                command_choose = user.recv(1024).decode(FORMAT)
                if command_choose == "1":

                    last_err = win32api.GetLastError()
                    user.sendall(f"Server 1 priority: "
                                 f"Last error is {last_err} {strftime('%H:%M:%S', gmtime())} \n".encode(
                        "utf-8"))

                elif command_choose == "2":
                    coord = win32api.GetCursorPos()
                    user.sendall(
                        f"%Cursor coordinates:  x:{coord[0]} and y:{coord[1]} {strftime('%H:%M:%S', gmtime())} \n ".encode(
                            "utf-8"))

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

    return 0


def main():
    # Проверка на создание более одного сервера
    try:
        me = singleton.SingleInstance()
    except:
        sys.exit()

    # Устанавливаем адрес и порт
    HOST = ""  # Standard loopback interface address (localhost)
    PORT = 8000  # Port to listen on (non-privileged ports are > 1023)
    PORT2 = 8888

    # Выполняем прослушивание порта
    server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server1.bind((HOST, PORT))
    server1.listen()

    while True:
        user, address = server1.accept()
        start_new_thread(threaded, (user,))

    return 0


if __name__ == "__main__":
    main()
