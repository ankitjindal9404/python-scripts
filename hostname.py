#checking hostname and sending output to file
import socket

try:
    filename = input("Enter a txt filename: ")
except Exception as e:
    print("Error: {e}")

with open(filename, "w+") as file:
    file.write(socket.gethostname())
    file.seek(0)
    content = file.read()
    print(content)
