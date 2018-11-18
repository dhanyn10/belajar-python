from distutils.core import setup
import py2exe

setup(
    #tiga parameter di bawah ini bersifat opsional
    version     = "0.1.0",
    description = "contoh penggunaan py2exe",
    name        = "sample",

    #nama file yang akan dijadikan .exe
    #program dalam bentuk console
    console     = ["sample.py"],
)