def ubah_Game(ubahGame):
    cek = True
    list = 0
    count = 0
    while cek == True:
        idGame = str(input("Masukkan ID Game: "))
        for i in ubahGame:
            if i[0] == idGame:
                cek = False
                list = count
                break
            count += 1 
        if cek == True:
            print("ID tidak valid.")
    namaGame = str(input("Masukkan nama game: "))
    kategori = str(input("Masukkan kategori: "))
    tahun_Rilis = str(input("Masukkan tahun rilis: "))
    hargaGame = str(input("Masukkan harga: "))
    
    #edit nama game
    if namaGame != "":
        ubahGame[list][1] = namaGame
    else:
        ubahGame[list][1] = ubahGame[list][1]
    
    #edit kategori game
    if kategori != "":
        ubahGame[list][2] = kategori
    else:
        ubahGame[list][2] = ubahGame[list][2]
    
    #edit tahun rilis
    if tahun_Rilis != "":
        ubahGame[list][3] = tahun_Rilis
    else:
        ubahGame[list][3] = ubahGame[list][3]

    #edit harga game
    if hargaGame != "":
        ubahGame[list][4] = hargaGame
    else:
        ubahGame[list][4] = ubahGame[list][4]
    return
