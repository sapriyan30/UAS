def login ():
    import getpass
    print ("-"*30)
    print (""*6, "hay pak, selamat datang",""*6)
    print ("-"*30)
    print ("Silahkan masukan dulu!!!")
    USERNAME = input("username : ")
    PASSWORD = getpass.getpass("password : ")
    if USERNAME == 'yan30' and PASSWORD == '3006':
        print ("Berhasil!")
    else :
        print ("Coba lagi")
        exit()
