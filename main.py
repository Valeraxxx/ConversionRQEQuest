##TODO SetupFile for Python Conversion to C and vice versa, BMOD Files ext generation forking from QPM.
##Require PowerShell for Windows Machine to compile and build the BMOD package extension.
from colorama import Fore, Style
import argparse

##I don't feel like creating another server today sooooo Python args it is!

## C# Being used for Quest interactions, easier.

def erf(self):
  print(Fore.BLUE + "[BMOD]" + Fore.YELLOW + ":" + Fore.RED + "[ERROR]: " + Style.RESET_ALL + self + "")

par = argparse.ArgumentParser()

par.add_argument("-b", "--build", nargs='?', help="Builds your project into a BMOD Extension.")
par.add_argument("-s", "--sync", help="Adds the BMOD Packages and libraries needed to your project.")
par.add_argument("-im", "--import", nargs="?", help="Imports a package you want from the BMOD library.")
par.add_argument("-ar", "--arch", nargs="?", help="Platform Architecture to compile for, THIS IS IMPORTANT!!", required=False)
par.add_argument("-tt", "--test", help="Test your        connection between you and the BMOD API, helpful if something fails to fetch or build.")



a, unknown = par.parse_known_args()


if len(unknown) > 0:
  prob = "Unknown argument(s) Provided. Type \"-h/--help \" for help."
  erf(prob)
else:
  pass

if a.build is not None:
  print("It's none!")
elif a.sync is not None:
  print()
elif a.arch is not None:
  print()
elif a.test is not None:
  print()
elif a.import is not None:
  print()

