from __future__ import print_function
import os, compileall

def main():
    dir = "D:\\Dokumen\\python\\bab-1\\compile-dir"
    compileall.compile_dir(dir)
    print("Semua file dalam %s berhasil dikompilasi" % dir)
    os.system("pause");

if __name__ == "__main__":
    main()