##TODO SetupFile for Python Conversion to C and vice versa, BMOD Files ext generation forking from QPM.
##Require PowerShell for Windows Machine to compile and build the BMOD package extension.
import colorama
from Commands import build
from Commands import sync
from Commands import iimport
from PreError import *
from colorama import Fore as f
from colorama import Style as s
from colorama import Back as b

l = "BMOD:"
k = f.BLUE
q = f.YELLOW
w = f.RED
e = s.RESET_ALL
colorama.init()


kwncmds = ["build", "import", "sync"]

def CommandFinish():
  print("UhOh We're done")

def CmdEXE(self):
  op = "UNKNOWN COMMAND!!!"
  for i in kwncmds[:3]:
    word = i
    chck = 1
    if self == word:
      chck += 1
      if chck == 2:
        build
      elif chck == 1:
       Error(op)
       inputy()
    else:
       Error(op)
       inputy()
      


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
      CmdEXE(lw0)
      continue
