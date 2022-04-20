def list_game(username, ownership, game_list, user):
    count_own = -1
    for row in ownership:
        count_own += 1
    
    count_game = -1
    for row in game_list:
        count_game += 1
    
    count_user = -1
    for row in user:
        count_user += 1
        
    #cari id
    for i in range(1,count_user+1):
        if user[i][1] == username:
            id = user[i][0]

    nomor = 1
    validate = False
    print("Daftar game: ")
    for i in range(1,count_own+1):
        if ownership[i][1] == id:
            temp_game = ownership[i][0]
            validate = True
        if validate :
            for i in range(1,count_game+1):
                if game_list[i][0]==temp_game:
                    print(str(nomor) +". " + game_list[i][0]+" | "+game_list[i][1]+ " | " + game_list[i][2] + " | " + game_list[i][3] + " | " + game_list[i][4])
                    nomor +=1
            validate = False
    if nomor==1:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
# WII = "WII"
# list_game(WII)
