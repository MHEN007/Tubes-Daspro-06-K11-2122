def ubah_stok (game_list) :
    
    a = 0
    '''
    game_list = []
    temp = ""
    cc = []
    with open('./database/game.csv', 'r') as game:
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
    '''
    
    for row in game_list:
        a += 1
        
    id = input("Masukkan ID game: ")
    
    stockIsValid = False
    
    for i in range (a) :
        
        if (id == game_list[i][0]) :
            
            stockIsValid = True
            count = int(input("Masukkan jumlah: ")) # variable yang memasukkan jumlah stok yg mau ditambahkan atau dikurangkan
            
            if count > 0 :
                game_list[i][5] = int(game_list[i][5]) + count
                print("Stok game " + str(game_list[i][1]) + " berhasil ditambahkan. Stok sekarang: " + str(game_list[i][5]))
            
            else :
                if count + int(game_list[i][5]) >= 0:
                    game_list[i][5] = int(game_list[i][5]) + count
                    print("Stok game " + str(game_list[i][1]) + " berhasil dikurangkan. Stok sekarang: " + str(game_list[i][5]))
                else :
                    print("Stok game " + str(game_list[i][1]) + " gagal dikurangi karena stok kurang. Stok sekarang: " + str(game_list[i][5]) + " ( <" + str(count*(-1)) + " )")
            
            break
        
    if (stockIsValid == False) :
        print("Tidak ada game dengan ID tersebut!")
        
