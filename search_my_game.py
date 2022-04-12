def searchMyGame(user_id,ownership,game_list):
    idGame = input("Masukkan ID Game ")
    tahun_rilis = input("Masukkan tahun rilis game ")

    print ("Daftar game pada inventory yang memenuhi kriteria:")

    #hitung jumlah row dalam ownership
    count_own = 0
    for i in ownership:
        count_own += 1

    #hitung jumlah row dalam game_list
    count_game = 0
    for i in game_list:
        count_game += 1
    
    count_ada = 0 #state = 0 artinya tidak ada game yang ditemukan
    urut = 1
    if idGame == "" and tahun_rilis == "": #jika idGame dan tahun_rilis dikosongkan
        for i in range(count_own):
            if user_id == ownership[i][1]:
                for j in range(count_game):
                    if ownership[i][0] == game_list[j][0]: #cari berdasarkan data di kepemilikan.csv saja
                        print(f"{urut}. {game_list[j][0]} | {game_list[j][1]} | {game_list[j][4]} | {game_list[j][2]} | {game_list[j][3]}")
                        count_ada += 1
                        urut += 1

        if count_ada <= 0:
            print("Tidak ada game yang ditemukan")
    elif idGame != "":  #jika idGame dikosongkan
        for i in range(count_own):
            if user_id == ownership[i][1]:
                for j in range(count_game):
                    if idGame == game_list[j][0] and ownership[i][0] == game_list[j][0]: #cari berdasarkan data di kepemilikan.csv dan input
                        print(f"{urut}. {game_list[j][0]} | {game_list[j][1]} | {game_list[j][4]} | {game_list[j][2]} | {game_list[j][3]}")
                        count_ada += 1
                        urut += 1

        if count_ada <= 0:
            print("Tidak ada game yang ditemukan")
    elif tahun_rilis != "": #hanya tahun_rilis yang dikosongkan
        for i in range(count_own):
            if user_id == ownership[i][1]:
                for j in range(count_game):
                    if ownership[i][0] == game_list[j][0] and tahun_rilis == game_list[j][3]:
                        print(f"{urut}. {game_list[j][0]} | {game_list[j][1]} | {game_list[j][4]} | {game_list[j][2]} | {game_list[j][3]}")
                        count_ada += 1
                        urut += 1

        if count_ada <= 0:
            print("Tidak ada game yang ditemukan")
    else: #kedua parameter diisi
        for i in range(count_own):
            if user_id == ownership[i][1]:
                for j in range(count_game):
                    if idGame == game_list[j][0] and tahun_rilis == game_list[j][3]:
                        print(f"{urut}. {game_list[j][0]} | {game_list[j][1]} | {game_list[j][4]} | {game_list[j][2]} | {game_list[j][3]}")
                        count_ada += 1
                        urut += 1
            
        if count_ada <= 0:
            print("Tidak ada game yang ditemukan")

#TES
#searchMyGame("1")