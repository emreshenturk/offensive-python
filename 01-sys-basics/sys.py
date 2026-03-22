import sys

v = sys.version_info

if v.major == 3 and v.minor == 8 and v.micro < 5:
    print("Exploit can run")
else:
    print("Exploit can't run")