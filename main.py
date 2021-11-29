##TODO SetupFile for Python Conversion to C and vice versa, BMOD Files ext generation forking from QPM.
##Require PowerShell for Windows Machine to compile and build the BMOD package extension.
import colorama
from colorama import Fore as f
from colorama import Style as s
from colorama import Back as b
colorama.init()


kwncmds = ["build", "import", "sync"]

def CmdEXE(self):
  for i in kwncmds[:3]:
    word = i
    chck = 1
    if self == word:
      chck += 1
      if chck := 2:
        ##TODO
        print("")
      else:
        print("Okay")
    else:
      chck = 0



def inputy():
  while True:
    print("RQE:")

    l1 = input()

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