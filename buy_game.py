import time

def buy_game(username, user, ownership, history, game_list) :
    
    row_ownership = 0
    for row in ownership:
        row_ownership += 1
    
    row_game = 0  
    for row in game_list:
        row_game += 1
    
    row_user = 0   
    for row in user:
        row_user += 1
        
    #cari id
    for i in range(row_user):
        if user[i][1] == username:
            id = user[i][0]
            saldo = int(user[i][5])

    id_game = input("Masukkan ID Game: ")
    
    # cari id game di game.csv
    for i in range (row_game) :
        if id_game == game_list[i][0] :
            harga_game = int(game_list[i][4])
            stok_game = int(game_list[i][5])
            nama_game = game_list[i][1]

    found = False        
    for i in range (row_ownership) :
        if ((id_game == ownership[i][0]) and (id == ownership[i][1])):
            found = True
            print("")
            print("Anda sudah memiliki game ini!")
            break
            
    if found == False :
        if (saldo >= harga_game) and (stok_game > 0):
            saldo = saldo - harga_game
            stok_game -= 1
            year = time.strftime("%Y")
            print("")
            print("Game " + nama_game + " berhasil dibeli!")
            history += [[str(id_game), str(nama_game), str(harga_game), str(username), str(year)]] #masukkan ke riwayat.csv
            ownership += [[str(id_game), str(id)]] #masukkan ke kepemilikan.csv
            #kurangkan saldo user
            for i in range(row_user):
                if user[i][0] == id:
                    user[i][5] = str(saldo)
            
            #kurangkan stok di game.csv
            for i in range(row_game):
                if game_list[i][0] == id_game:
                    game_list[i][5] = str(stok_game)
            
        elif (saldo >= harga_game) and (stok_game <= 0) :
            print("")
            print("Stok game tersebut sedang habis!")
        elif (saldo < harga_game) :
            print("")
            print("Saldo anda tidak cukup untuk membeli game tersebut!")
            
    return
#buy_game(username, user, ownership, history, game_list)
