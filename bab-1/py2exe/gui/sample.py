from __future__ import print_function
import os
import sys

def main():
    print("Contoh penggunaan library py2exe")
    print("sys.path:")
    print(sys.path)
    print("sys.executable\t: %s" % sys.executable)
    print("sys.prefix\t: %s" % sys.prefix)
    print("sys.argv\t: %s" %sys.argv)
    os.system("pause")

if __name__ == "__main__":
    main()