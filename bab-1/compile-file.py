from __future__ import print_function
import os, py_compile

def main():
    os.chdir("D:\\Dokumen\python\\bab-1")
    py_compile.compile("hello.py")
    print("file hello.pyc berhasil dibuat")
    os.system("pause");

if __name__ == "__main__":
    main()