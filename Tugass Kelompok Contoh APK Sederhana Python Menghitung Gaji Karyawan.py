print("-------------------------------------")
print("-----Gaji Karyawan YBM PLN 2022------")
print("-------------------------------------")


    #Inputan
while (True) :
    nama = str(input("Masukkan nama : "))
    gol = input ("golongan : ")
    jam = int (input("Masukkan jumlah jam : "))
    gaji = 300000
    if gol == "1" : 
        upah = 0.05*gaji
    elif gol == "2" :
        upah = 0.10*gaji
    elif gol == "3" :
        upah = 0.15*gaji
    else:
        print("tidak ada golongan")
        
    # Menghitung rumus
    if jam >= 48 :
        lembur = jam - 48
        rumus = 48 * upah + lembur * 20000
    else :
        rumus = jam * upah

    print (rumus)

    status = input("Apakah masih ada yang ingin di input? (y = ya, n = tidak)?")
    if status == "n" :
        print("Program Berhenti")
        break

    elif status == "y" :
        print("Silahkan Input Kembali Data")
    else :
        print("Inputan Tidak Di Kenali")
        break