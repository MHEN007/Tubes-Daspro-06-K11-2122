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
    ulang = 1
    for i in [namaGame,kategori,tahun_Rilis,hargaGame]:
        if i != '':
            ubahGame[list][ulang] = i
        ulang += 1
    return ubahGame
