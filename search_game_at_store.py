def searchGameAtStore(game_list):
    idGame = input("Masukkan ID Game ")
    namaGame = input("Masukkan Nama game ")
    hargaGame = input("Masukkan Harga Game ")
    kategori = input("Masukkan Kategori Game ")
    tahun = input("Masukkan Tahun Rilis Game ")
    print("")

    #count row dalam game.csv
    count_row = 0
    for row in game_list:
        count_row += 1

    #count col dalam game.csv
    count_col = 0
    for row in game_list:
        for col in row:
            count_col += 1
        break
    
    #buat result
    result = ["ada" for i in range(count_row)]
    #nilai dalam array ini berkorespondensi terhadap row dalam game_list

    urut = 1
    true = 0
    if idGame == "" and namaGame == "" and hargaGame =="" and kategori =="" and tahun =="": #keluarkan semua game jika paramater tidak diisi
        for i in range(1,count_row):
            # ID | NAMA  | Harga | Kategori | Tahun rilis | stok
            print(f"{urut}. {game_list[i][0]} | {game_list[i][1]} | {game_list[i][2]} | {game_list[i][3]} | {game_list[i][4]} | {game_list[i][5]}")
            urut += 1
            true += 1
    else:
        #cek idGame dalam result
        if idGame != "":
            for i in range(count_row):
                if game_list[i][0] != idGame:
                    result[i] = ""
                else:
                    result[i] = result[i]
        else:
            result = result
        
        #cek nama game
        if namaGame != "":
            for i in range(count_row):
                if game_list[i][1] != namaGame:
                    result[i] = ""
                else:
                    result[i] = result[i]
        else:
            result = result

        #cek harga game
        if hargaGame != "":
            for i in range(count_row):
                if game_list[i][4] != hargaGame:
                    result[i] = ""
                else:
                    result[i] = result[i]
        else:
            result = result

        #cek kategori game
        if kategori != "":
            for i in range(count_row):
                if game_list[i][2] != kategori:
                    result[i] = ""
                else:
                    result[i] = result[i]
        else:
            result = result

        #cek tahun game
        if tahun != "":
            for i in range(count_row):
                if game_list[i][3] != tahun:
                    result[i] = ""
                else:
                    result[i] = result[i]
        else:
            result = result

        for i in range(count_row):
            if result[i] != "":
                # ID | NAMA  | Harga | Kategori | Tahun rilis | stok
                print(f"{urut}. {game_list[i][0]} | {game_list[i][1]} | {game_list[i][2]} | {game_list[i][3]} | {game_list[i][4]} | {game_list[i][5]}")
                urut += 1
                true += 1
    if true <= 0:
        print("Tidak ada data game yang ditemukan")

    return
#TES
'''
game_list = []
temp = ""
cc = []
with open("./database/game.csv","r") as game:
    for row in game:
        for char in row:
            if char != ";" and char != "\n":
                temp += char
            else:
                cc += [temp]
                temp = ""
        game_list += [cc]
        cc = []
game.close()
searchGameAtStore(game_list)
'''
