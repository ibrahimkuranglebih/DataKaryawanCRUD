daftar_karyawan = []
pph = 0
gaji_pokok = 0
gaji_bersih = 0

def tampilkan_data() : #menampilkan data karyawan
    print     ("\nDATA KARYAWAN\n")
    print     ("------------------------------------------------------------------------------------------------------------------------")
    print     ("NAMA                         NOMOR KARYAWAN     GAJI POKOK (RP)    TUNJANGAN KELUARGA(RP)    PPH (RP)    GAJI BERSIH(RP)")
    for data in daftar_karyawan :
        print(f'{data["nama"]:<26}   {data["nomor karyawan"]:<16}   {data["gaji pokok"]:<10}         {data["tunjangan keluarga"]:<14}            {data["pph"]:<11} {data["gaji bersih"]:<15}')
    print     ("------------------------------------------------------------------------------------------------------------------------")

def input_karyawan() : #menginput data karyawan
    print("-------------INPUT DATA KARYAWAN-------------")
    while True:
        nama_karyawan = input("\nmasukkan nama karyawan                      : ")
        nama_karyawan.lower()
        nomor_karyawan = input("masukkan nomor karyawan (7 digit)           : ")
        alamat = input("alamat karyawan                             : ")
        status_nikah = input("apakah sudah kawin ? (k/b)                  : ")
        golongan = int(input("masukkan nomor golongan (1/2/3/4)           : "))
        sertifikasi = int(input("masukkan jumlah sertifikasi yang anda ikuti : "))
        
        if status_nikah == "k" : tunjangan = 500000
        elif status_nikah == "b" : tunjangan = 0 # tunjangan nikah

        if golongan == 1 : gaji_pokok = 2000000 #gaji pokok
        elif golongan == 2 : gaji_pokok = 2750000
        elif golongan == 3 : gaji_pokok = 4000000
        elif golongan == 4 : gaji_pokok = 5000000

        bonus = sertifikasi*150000 #bonus sertifikasi

        pph = 0.025*gaji_pokok #pph

        gaji_bersih = gaji_pokok + tunjangan + bonus - pph #gaji bersih karyawan

        daftar_karyawan.append({ #menambahkan karyawan
            "nama" : nama_karyawan,
            "nomor karyawan" : nomor_karyawan,
            "alamat" : alamat,
            "gaji pokok" : gaji_pokok,
            "tunjangan keluarga" : tunjangan,
            "pph" : pph,
            "gaji bersih" : gaji_bersih
        })

        pilihan = input("apakah anda lanjut ? : ")
        if pilihan == "y" : True
        elif pilihan == "t" : break

def output_karyawan(): #output pencarian karyawan
    while True : 
        print("\n---PENCARIAN DATA KARYAWAN---\n")
        cari_karyawan = input("masukkan nama karyawan : ")
        for karyawan in daftar_karyawan :
            if karyawan["nama"] == cari_karyawan :
                print(f'nama              : {karyawan["nama"]}')
                print(f'nomor karyawan    : {karyawan["nomor karyawan"]}')
                print(f'alamat karyawan   : {karyawan["alamat"]}')
                print(f'gaji pokok        : {karyawan["gaji pokok"]}')
                print(f'tunjangan keluarga: {karyawan["tunjangan keluarga"]}')
                print(f'pph               : {karyawan["pph"]}')
                print(f'gaji bersih       : {karyawan["gaji bersih"]}')
        lagi = input("apakah anda ingin mencari lagi ? (y/t) : ")
        if lagi == "y" : True
        elif lagi == "t" : break

def hapus_karyawan() : #menghapus data karyawan
    print                    ("---------PENGHAPUSAN DATA KARYAWAN---------")
    nama_yang_dihapus = input("masukkan nama karyawan yang akan dihapus : ")
    for data in daftar_karyawan :
        if nama_yang_dihapus == data["nama"] :
            daftar_karyawan.remove(data)
    print("\nDATA KARYAWAN TELAH DIHAPUS !! ")

def urut_karyawan() : #mengurutkan data karyawan
    daftar_karyawan.sort(key=lambda x: x['nomor karyawan'])
    print("\nDATA KARYAWAN BERHASIL DI SORTIR!!\n")

# Tampilan utama 

print("\nSELAMAT DATANG DI APLIKASI DATA KARYAWAN")

while True : 
    print("\n--------------------------")
    print("1. Buat Data\n2. Pencarian Karyawan\n3. Penghapusan Karyawan\n4. Pengurutan Karyawan\n5. Tampilkan Data Pegawai\n6. Exit")
    opsi = int(input("masukkan pilihan anda  : "))
    print("--------------------------\n")
    if opsi == 1 : input_karyawan()
    elif opsi == 2 : output_karyawan()
    elif opsi == 3 : hapus_karyawan()
    elif opsi == 4 : urut_karyawan()
    elif opsi == 5 : tampilkan_data()
    elif opsi == 6 : 
        print("\nterimakasih :) \n")
        break

