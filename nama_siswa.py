# membuat array siswa
siswa = []

# membuat perulangan for
for i in range(3):
    
    # mengecek nilai indeks
    print ("")
    print("ini adalah indeks ke-",i)

    # menerima inputan nama
    nama_siswa = input("Masukkan nama siswa : ")

    # memasukkan hasil inputan nama ke array siswa
    siswa.append(nama_siswa)

print("")

# membuat perulangan untuk mencetak data dari array siswa
for k in siswa:

    #mencetak array siswa
    print("Nama Siswa : " , k)