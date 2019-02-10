from __future__ import print_function

def main():
    s = "hello from python programming repository"
    print(s[0])     # cetak karakter indeks ke 0
    print(s[4])     # cetak karakter indeks ke 4
    print(s[-5])    # cetak karakter ke 5 dihitung dari kanan
    print(s[:13])   # mencetak 13 karakter dari indeks pertama
    print(s[3:7])   # mencetak karakter dimulai dari indeks ke 3 hingga 7
    print(s[6:])    # mencetak seluruh karakter dikurangi 6 karakter pertama

if __name__ == "__main__":
    main()