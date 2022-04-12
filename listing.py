def listing (game_list) :
    
    a = 0
    
    for row in game_list:
        a += 1
    
    sorting = input("Skema sorting: ")
    
    if ((sorting == "tahun+") or (sorting == "tahun-") or (sorting == "")) : 
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
            
        elif (sorting == "") :
            temp = game_list
        
        i = 1
        while (i < a) :
            print(str(i)  + ". " + game_list[i][0] + "       | " + game_list[i][1] + "       | " + game_list[i][2] + "       | " + game_list[i][3] + "       | " + game_list[i][4] + "       | " + game_list[i][5])
            # outputnya masih belum rapi
            i += 1
    
    else :
        print("Skema sorting tidak valid!")
