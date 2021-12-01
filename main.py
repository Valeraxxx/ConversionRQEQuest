##TODO SetupFile for Python Conversion to C and vice versa, BMOD Files ext generation forking from QPM.
##Require PowerShell for Windows Machine to compile and build the BMOD package extension.

from PreError import *
from colorama import Fore as f
from colorama import Style as s
from colorama import Back as b
import socket

l = "BMOD:"
k = f.BLUE
q = f.YELLOW
w = f.RED
e = s.RESET_ALL
colorama.init()

host = 'local host'
port = 5000

b = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

b.connect(('some random string for now', port))

message = b.recv(1104)

while message:
  print("Server:" + message.decode())
  msg.recv(1104)


b.close()
