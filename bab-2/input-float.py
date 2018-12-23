from __future__ import print_function

def main():
    #membuat prompt untuk tipe data float
    bilanganriil = float(raw_input("maskkan bilangan Riil(float): "))

    #menggunakan variabel untuk melakukan perhitungan
    hasil = bilanganriil / 2

    #menampilkan nilai variabel
    #2f menunjukkan nilai hingga 2 angka di belakang koma
    print("Bilangan yang dimasukkan adalah %.2f" % bilanganriil)
    print("%.2f / 2 = %.2f" % (bilanganriil, hasil))

if __name__ == "__main__":
    main()