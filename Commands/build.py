import os as o
from colorama import Fore, Style
import Setup as s
import glob
import os

def start(projectpath):
  ##Initiate the compiling process, Cython will be used ##to convert python to C.
  pathcheck = o.path.isdir(projectpath)

  def erf(self):
    print(Fore.BLUE + "[BMOD]" + Fore.YELLOW + ":" + Fore.RED + "[ERROR]: " + Style.RESET_ALL + self + "")
 
  errf = Fore.BLUE + "[BMOD]" + Fore.RED + ":" + Fore.YELLOW + "[INFO]: " + Style.RESET_ALL  


  if pathcheck is False:
    er = "Project Directory Doesnt exist. Try again."
    erf(er)
  else:
    pass

  s.path(projectpath)

  print(errf + " Checking if the variable has been passed to Setup")

  if projectpath != s.path:
    n = " Project Path wasn't passed down to Setup."
    erf(n)
  else:
    print(errf + " The variable has been passed down to the Setup file.")
    pass
  

  files = glob.glob(f"{projectpath}*.py")
  for i in files:
    hm = os.path.basename(i)
    fixed = os.path.splitext(hm)[0]+'.pyx'

    os.rename(fixed)
  


  





  



    