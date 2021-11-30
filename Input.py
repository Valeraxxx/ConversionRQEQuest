import colorama
from colorama import Fore as f
from colorama import Style as s
from colorama import Back as b
from main import CmdEXE

l = "BMOD:"
k = f.BLUE
q = f.YELLOW
w = f.RED
e = s.RESET_ALL
colorama.init()

def inputy():
  while True:
    l1 = input(k + "[BMOD]" + q + "[INPUT]:" + e + "")

    lw0 = l1.casefold()

    lw1 = lw0.strip()

    splt = lw1.split(" ")

    cnt = len(splt)

    if cnt > 1:
      print(f.RED + "You've entered more than one Command or more than one argument. Please try Again." + s.RESET_ALL)
      continue
    else:
      break

  CmdEXE(lw0)

  

inputy()