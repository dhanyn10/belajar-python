from __future__ import print_function

def main():
    #static teks
    statteks = "bandung jakarta medan bandung sumatera medan kalimantan medan papua aceh timika kediri kediri"
    #spit teks
    teksSplit = statteks.split(" ")
    #cetak teks yang telah di split
    print("split: ", teksSplit)
    #inisiasi array teks unik python
    teksunik = []
    #for loop python
    for a in teksSplit:
        if a not in teksunik:
            teksunik.append(a)
    
    print("teksunik: ", teksunik)

    #array untuk menghitung jumlah teks didalam kalimat
    tekscount = []
    for b in teksunik:
        hitung = 0
        for c in teksSplit:
            if b == c:
                hitung += 1
        tekscount.append(hitung)
    print(tekscount)

if __name__ == "__main__":
    main()