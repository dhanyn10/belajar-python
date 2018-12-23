from __future__ import print_function

def main():
    #membuat prompt untuk tipe data ineger
    bilanganbulat = int(raw_input("maskkan bilangan bulat: "))

    #menggunakan variabel untuk melakukan perhitungan
    hasil = bilanganbulat + 1

    #menampilkan nilai variabel
    print("Bilangan yang dimasukkan adalah %d" % bilanganbulat)
    print("%d + 1 = %d" % (bilanganbulat, hasil))

if __name__ == "__main__":
    main()