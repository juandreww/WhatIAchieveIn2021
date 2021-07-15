jumlahbaris = 10
baris = 0
bintang = 0
while baris < jumlahbaris:
    if (bintang) >= (baris+1):
        print()
        baris = baris+1
        bintang=0
        continue      ##saat masuk ke if, maka bagian print * diluar if tidak akan dijalankan, langsung ulang ke while
    print("*",end="")
    bintang= bintang+1