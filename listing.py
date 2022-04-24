import isempty

def listing (game_list) :
    
    a = 0
    
    for row in game_list:
        a += 1
    
    sorting = input("Skema sorting: ")
    
    if ((sorting == "tahun+") or (sorting == "tahun-") or (sorting == "harga+") or (sorting == "harga-") or (sorting == "")) : 
        if (sorting == "tahun+") : #ascending
            i = 1
            while (i < a) :
                j = i + 1
                while (j < a) :
                    if game_list[i][3] > game_list[j][3] :
                        temp = game_list[i]
                        game_list[i] = game_list[j]
                        game_list[j] = temp
                    j += 1
                i += 1
            
        elif (sorting == "tahun-") : #descending
            i = 1
            while (i < a) :
                j = i + 1
                while (j < a) :
                    if game_list[i][3] < game_list[j][3] :
                        temp = game_list[i]
                        game_list[i] = game_list[j]
                        game_list[j] = temp
                    j += 1
                i += 1
        
        elif (sorting == "harga+") : #ascending
            i = 1
            while (i < a) :
                j = i + 1
                while (j < a) :
                    if game_list[i][4] > game_list[j][4] :
                        temp = game_list[i]
                        game_list[i] = game_list[j]
                        game_list[j] = temp
                    j += 1
                i += 1        
        
        elif (sorting == "harga-") : #descending
            i = 1
            while (i < a) :
                j = i + 1
                while (j < a) :
                    if game_list[i][4] < game_list[j][4] :
                        temp = game_list[i]
                        game_list[i] = game_list[j]
                        game_list[j] = temp
                    j += 1
                i += 1        
            
        elif (sorting == "") :
            temp = game_list
        
        #cari nama game dan harga yang paling panjang
        max_nama = 0
        max_kategori = 0
        max_harga = 0
        for i in range(0,a):
            if isempty.lenght(game_list[i][1])>max_nama:
                max_nama = isempty.lenght(game_list[i][1])
            if isempty.lenght(game_list[i][2])>max_kategori:
                max_kategori = isempty.lenght(game_list[i][2])
            if isempty.lenght(game_list[i][4])>max_harga:
                max_harga = isempty.lenght(game_list[i][4])            

        #samakan panjang string dengan spasi
        for i in range(0,a):
            if isempty.lenght(game_list[i][1])<max_nama:
                game_list[i][1] = game_list[i][1] + (" "*(max_nama-isempty.lenght(game_list[i][1])))
            if isempty.lenght(game_list[i][2])<max_kategori:
                game_list[i][2] = game_list[i][2] + (" "*(max_kategori-isempty.lenght(game_list[i][2])))
            if isempty.lenght(game_list[i][4])<max_harga:
                game_list[i][4] = game_list[i][4] + (" "*(max_harga-isempty.lenght(game_list[i][4])))

        i = 1                
        while (i < a) :
            print(str(i) + ". " + game_list[i][0] + " | " + game_list[i][1] + " | " + game_list[i][2] + " | " + game_list[i][3] + " | " + game_list[i][4] + " | " + game_list[i][5])
            i += 1
    
    else :
        print("Skema sorting tidak valid!")
    
    return
