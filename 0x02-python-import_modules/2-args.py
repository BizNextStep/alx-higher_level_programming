#1/usr/bin/python3
# This script prints the number of and the list of its arguments
from sys import argv

if len(argv) == 1:
    print("0 arguments.")
elif len(argv) == 2:
    print("1 argument:")
else:
    print("{} arguments:".format(len(argv) - 1))

for i in range(1, len(argv)):
    print("{}: {}".format(i, argv[i]))
