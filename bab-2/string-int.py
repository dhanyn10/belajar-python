# konversi tipe data string ke integer
# kemudian dilakukan operasi hitung bilangan

from __future__ import print_function

def main():
    # membuat prompt untuk tipe data string
    s = raw_input("masukkan bilangan bulat: ")

    # melakukan konversi dari tipe data string ke tipe data integer
    bilanganbulat = int(s)

    # menggunakan variabel untuk menampung hasil hitung dari bilangan bulat
    # hitungan yang dibuat bisa dengan keinginan sendiri :)
    hasil = bilanganbulat * 2

    # menampilkan nilai hasil dari perhitungan
    print("bilangan bulat: %d" % bilanganbulat)
    print("%d * 2 = %d" % (bilanganbulat, hasil))

if __name__ == "__main__":
    main()