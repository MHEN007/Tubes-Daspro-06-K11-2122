import isempty

def listing (game_list) :
    
    a = 0 #baris
    b = 0 #kolom
    for row in game_list: #hitung baris dalam game_list
        a += 1
    
    for row in game_list: #hitung kolom dalam game_list
        for col in row:
            b += 1
        break

    copy_game_list = [["" for j in range(b)] for i in range(a)]
    
    for i in range(a):
        for j in range(b):
            copy_game_list[i][j] = game_list[i][j]

    sorting = input("Skema sorting: ")
    
    if ((sorting == "tahun+") or (sorting == "tahun-") or (sorting == "harga+") or (sorting == "harga-") or (sorting == "")) : 
        if (sorting == "tahun+") : #ascending
            i = 1
            while (i < a) :
                j = i + 1
                while (j < a) :
                    if copy_game_list[i][3] > copy_game_list[j][3] :
                        temp = copy_game_list[i]
                        copy_game_list[i] = copy_game_list[j]
                        copy_game_list[j] = temp
                    j += 1
                i += 1
            
        elif (sorting == "tahun-") : #descending
            i = 1
            while (i < a) :
                j = i + 1
                while (j < a) :
                    if copy_game_list[i][3] < copy_game_list[j][3] :
                        temp = copy_game_list[i]
                        copy_game_list[i] = copy_game_list[j]
                        copy_game_list[j] = temp
                    j += 1
                i += 1
        
        elif (sorting == "harga+") : #ascending
            i = 1
            while (i < a) :
                j = i + 1
                while (j < a) :
                    if copy_game_list[i][4] > copy_game_list[j][4] :
                        temp = copy_game_list[i]
                        copy_game_list[i] = copy_game_list[j]
                        copy_game_list[j] = temp
                    j += 1
                i += 1        
        
        elif (sorting == "harga-") : #descending
            i = 1
            while (i < a) :
                j = i + 1
                while (j < a) :
                    if copy_game_list[i][4] < copy_game_list[j][4] :
                        temp = copy_game_list[i]
                        copy_game_list[i] = copy_game_list[j]
                        copy_game_list[j] = temp
                    j += 1
                i += 1        
            
        elif (sorting == "") :
            temp = copy_game_list
        
        #cari nama game dan harga yang paling panjang
        max_nama = 0
        max_kategori = 0
        max_harga = 0
        for i in range(0,a):
            if isempty.lenght(copy_game_list[i][1])>max_nama:
                max_nama = isempty.lenght(copy_game_list[i][1])
            if isempty.lenght(copy_game_list[i][2])>max_kategori:
                max_kategori = isempty.lenght(copy_game_list[i][2])
            if isempty.lenght(copy_game_list[i][4])>max_harga:
                max_harga = isempty.lenght(copy_game_list[i][4])            

        #samakan panjang string dengan spasi
        for i in range(0,a):
            if isempty.lenght(copy_game_list[i][1])<max_nama:
                copy_game_list[i][1] = copy_game_list[i][1] + (" "*(max_nama-isempty.lenght(copy_game_list[i][1])))
            if isempty.lenght(copy_game_list[i][2])<max_kategori:
                copy_game_list[i][2] = copy_game_list[i][2] + (" "*(max_kategori-isempty.lenght(copy_game_list[i][2])))
            if isempty.lenght(copy_game_list[i][4])<max_harga:
                copy_game_list[i][4] = copy_game_list[i][4] + (" "*(max_harga-isempty.lenght(copy_game_list[i][4])))

        i = 1                
        while (i < a) :
            print(str(i) + ". " + copy_game_list[i][0] + " | " + copy_game_list[i][1] + " | " + copy_game_list[i][2] + " | " + copy_game_list[i][3] + " | " + copy_game_list[i][4] + " | " + copy_game_list[i][5])
            i += 1
    
    else :
        print("Skema sorting tidak valid!")
    
    return
