from login.login import login
from perhitungan.nilai import nilai
from perhitungan.gaji import gaji
from pembayaran.biaya import biaya
from kalkulator.kalkulator import kalkulator

def pilih():
    login()
    print(">>>>>>PILIH MENU<<<<<<")
    print("\n\t***pilihan***\n\t1. Nilai\n\t2. Gaji\n\t3. Biaya\n\t4. Kalkulator\n\t5. exit")

    pilih = input("\n\tsilahkan pilih:")
    if pilih == "1":
        nilai()
        lagi()
    elif pilih == "2":
        gaji()
        lagi()
    elif pilih == "3":
        biaya()
        lagi()
    elif pilih == "4":
        kalkulator()
        lagi()
    elif pilih == "5":
        exit
        print("\n\t*****TERIMA KASIH*****")
    else :
        exit
        print ("\n\t*****TERIMA KASIH*****")

def lagi():
    tanya = input("\nKembali ke menu pilihan (y/t)?")
    if tanya == "y":
        pilih()
    elif tanya == "t":
        exit
        print ("\n\tTERIMA KASIH")
    else:
        print("\n\tSalah input........!")
        exit
pilih()
