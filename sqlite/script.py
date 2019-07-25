import sqlite3

conn = sqlite3.connect("lite.db")
cs = conn.cursor()
# to handle error when table already exists, you can add command
# <IF NOT EXISTS> after <TABLE> command
cs.execute("CREATE TABLE guru (nama TEXT, jabatan TEXT, ruang INTEGER)")
conn.commit()
conn.close()