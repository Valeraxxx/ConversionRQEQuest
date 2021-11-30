import colorama
from colorama import Fore as f
from colorama import Style as s
from colorama import Back as b

l = "[BMOD]"
i = "[WARNING]:"
p = "[ERROR]:"
we = "[SUCCESS]:"
k = f.BLUE
q = f.YELLOW
w = f.RED
e = s.RESET_ALL
colorama.init()

def Error(self):
  print(k + f"{l}" + w + f"{p}" + f"{self}" + e + "")

def Warning(self):
  print(k + f"{l}" + q + f"{i}" + e + f"{self}")

def Success(self):
  print(k + f"{l}" + f.GREEN + f"{we}" + e + f"{self}")



  


