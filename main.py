##TODO SetupFile for Python Conversion to C and vice versa, BMOD Files ext generation forking from QPM.
##Require PowerShell for Windows Machine to compile and build the BMOD package extension.

import argparse

##I don't feel like creating another server today sooooo Python args it is!

## C# Being used for Quest interactions, easier.

par = argparse.ArgumentParser()

par.add_argument("-b", "--build", nargs='?', help="Builds your project into a BMOD Extension.")
par.add_argument("-s", "--sync", help="Adds the BMOD Packages and libraries needed to your project.")
par.add_argument("-im", "--import", nargs="?", help="Imports a package you want from the BMOD library.")
par.add_argument("-ar", "--arch", nargs="?", help="Platform Architecture to compile for, THIS IS IMPORTANT!!", required=True)
par.add_argument("-tt", "--test", help="Test your        connection between you and the BMOD API, helpful if something fails to fetch or build.")



a = par.parse_args()

print(a.action)
