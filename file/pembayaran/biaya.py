from texttable import Texttable
def biaya():
    table= Texttable ()
    no=0
    name=[]
    nim=[]
    kelas=[]
    semester=[]
    seminar=[]
    kas=[]
    uts=[]
    uas=[]
    admin=[]
    jawab3 = "y"
    while(jawab3 == "y"):
        nama=(input("Masukan Nama  : "))
        nim=(input("Masukan NIM   : "))
        kelas=(input("Masukan Kelas: "))
        print("_"*60)
        pilih = (input("Apakah anda ingin membayar semester (y/t) ? "))
        if pilih == 'y':
            semester =int(input("untuk berapa bulan ? "))
            d_semester = 'SEMESTER'
            semester=500000*semester
        else :
            sem_ = ''
            sem=0
        print("_"*60)
        print("_"*60)
        pilih = (input("ingin bayar SEMINAR (y/t) ? "))
        if  pilih == 'y':
            seminar  = 'SEMINAR'
            seminar=100000
        else :
            seminar = ''
            seminar=0
        print("_"*60)
        print("_"*60)
        pilih = (input("ingin bayar KAS Bulanan (y/t) ? "))
        if  pilih == 'y':
            kas  = 'KAS'
            kas=20000
        else :
            kas = ''
            kas=0
        print("_"*60)
        print("_"*60)
        pilih = (input("ingin bayar UTS (y/t) ? "))
        if  pilih == 'y':
            uts =int(input("untuk berapa bulan ? "))
            d_uts  = 'UTS'
            uts=250000*uts
        else :
            uts_ = ''

            uts=0
        print("_"*60)
        print("_"*60)  
        pilih = (input("ingin bayar UAS (y/t) ? "))
        if  pilih == 'y':
            uas =int(input("untuk berapa bulan ? "))
            d_uas  = 'UAS'
            uas=300000*uas
        else :
            uas_ = ''
            uas=0
        print("_"*60)
        print("_"*60)
        pilih = (input("Anda akan di kenakan biaya admin sebesar 5000 (y/t) ? "))
        if  pilih == 'y':
            admin  = 'ADMIN'
            admin=5000
        else :
            admin = ''
            admin=0
        print("_"*60)
        

        total_bayar = semester+seminar+kas+uts+uas+admin
        table.add_rows([['SEMESTER','SEMINAR','KAS','UTS','UAS','ADMIN','TOTAL'],
                        [semester,seminar,kas,uts,uas,admin,total_bayar]])
        print("_"*30)
        print("Total Rincian")
        print("_"*30)
        print ("Nama :",nama)
        print ("Nim :",nim)
        
        print ("Kelas :",kelas)
        print (table.draw())
        jawab3 = input("\n  Tambahkan Data PEMBAYARAN (y/t)? ") ; print("")
