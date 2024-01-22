import socket
import struct
import time


socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
adress = ("192.168.88.250", 20002)
#налево, направо
command = [0, 0, 0, 100, 0, 0]
massage = struct.pack("<cB2b4Bc", b"#", 1, *command, b"*")
for i in range(10):
    time.sleep(0.25)
    socket.sendto(massage, adress)


# command = [0, 0, 0, 100, 0, 0]
# massage = struct.pack("<cB2b4Bc", b"#", 1, *command, b"*")
# for i in range(10):
#     time.sleep(0.25)
#     socket.sendto(massage, adress)

command = [0, 0, 0, 0, 0, 0]
massage = struct.pack("<cB2b4Bc", b"#", 1, *command, b"*")
socket.sendto(massage, adress)