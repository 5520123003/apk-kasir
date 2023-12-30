import os

while True:
    print('\n')
    print(80 * '-')
    print(f"|{'SELAMAT DATANG':^78}|")
    print(f"|{'DIKASIR MILIK KAMI':^78}|")
    print(80*'-')
    print('\n')


    data_product = {
        1:"LAPTOP",
        2:"KOMPUTER",
        3:"MINIOTOR",
        4:"MOUS PAD",
        5:"CHARGER"
    }
    daftar_harga = {
        1: 2000000,
        2: 5000000,
        3: 600000,
        4: 30000,
        5: 15000
    }

    dict_trx = {}
    daftar_metode_pembayaran = {
        1:"TRANSFER BANK",
        2:"FIRTUAL ACCOUNT",
        3:"CAS ON DELIFERI",
        4:"KARTU CREDIT"
    }

    os.system('cls')
    print(79*'-')
    print(32*'-'," LIST PRODUCK ",'-'*32)
    print(80*'-')
    for i in data_product:
        print("id product : ", i, "\t nama product :", data_product[i], "\t \tharga product :",   daftar_harga[i])

    print('\n')
    pilih_id = int(input("[+] Pilih Id Product : "))
    if pilih_id in data_product :
        pilih_beli = input("[+] Ingin Beli ? (Y/N): ")
        if pilih_beli  == "y" or pilih_beli=="Y":
            print('\n')
            print(80 * '-')
            nama_penerima    = input("Nama Penerima : ")
            alamat_penerima  = input("Alamat Penerima : ")
            telepon          = input("NO HP : ")
            kurir_pengiriman = input("Kurir Pengiriman : ")
            dict_trx = {
                "Nama Penerima"   :nama_penerima,
                "Alamat Penerima" :alamat_penerima,
                "NO HP"           :telepon,
                "Kurir Pengiriman":kurir_pengiriman,
                "Product Id"      :data_product,
            }
        else:
            pass
        if len (dict_trx) > 0 :
            print('\n')
            print(80 * '-')
            print(30*'-'," METODE PEMBAYARAN ",'-'*29)
            print(80 * '-')

        for i in daftar_metode_pembayaran:
            print("id : ", i, "\t Metode Pembayaran : ", daftar_metode_pembayaran[i])
        pilih_metode = int(input("\n[+] Pilih Id Metode Pembayaran : "))
        if pilih_metode in daftar_metode_pembayaran :
            print(80 * '-')
            print("Nama Penerima     : ", dict_trx["Nama Penerima"])
            print("Alamat Penerima   : ", dict_trx["Alamat Penerima"])
            print("NO HP             : ", dict_trx["NO HP"])
            print("Kurir Pengiriman  : ", dict_trx["Kurir Pengiriman"])
            print("Product           : ", data_product[pilih_id])
            print("Harga             : ", daftar_harga[pilih_id])
            print("Metode Pembayaran :", daftar_metode_pembayaran[pilih_metode])
            print(80 *'-')
            konfirmasi = input(" ~ Apakah Anda Yakin Ingin Melakukan Pembayaran? (Y/N) : ")
            if konfirmasi == "y" or konfirmasi == "Y":
                print('\n')
                print(f"{'--<<<< [*_*] TERIMAKASIH ANDA SUDAH MELAKUKAN PEMBAYARAN [*_*] >>>>--':^30}\n")

                is_done = input("Apakah Ingin Memesan Product Lagi? ")
                if is_done == "y":
                    print("\n")

                else:
                    break


            else:
                pass
        else:
            print("id metode pembayaran tidak tersedia")
    else:
        print("id product tidak tersedia\n")

    is_done = input("Apakah Ingin Memesan Product Lagi? ")
    if is_done == "y":
        print("\n")

    else:
        break
    os.system("cls")

