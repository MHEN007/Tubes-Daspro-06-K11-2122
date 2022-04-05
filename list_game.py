def list_game(username):
    #Akses database kepemilikan.csv
    game = []
    temp = ""
    cc= []
    count_own = -1
    with open("./database/kepemilikan.csv","r") as game_owner:
        for row in game_owner:
            for char in row:
                if char != ";" and char!="\n":
                    temp += char
                else:
                    cc += [temp]
                    temp = ""
            game += [cc]
            cc = []
            count_own +=1
    game_owner.close()

    #Akses database game.csv
    info_game = []
    temp = ""
    cc = []
    count_game = -1
    with open("./database/game.csv","r") as info:
        for row in info:
            for char in row:
                if char != ";" and char != "\n":
                    temp += char
                else:
                    cc += [temp]
                    temp = ""
            info_game += [cc]
            cc = []
            count_game += 1
    info.close()

    #akses database user.csv
    user = []
    temp = ""
    cc = []
    count_user = -1 #header tidak dihitung
    with open("./database/user.csv","r") as user_file:
        for row in user_file:
            for char in row:
                if char != ";" and char != "\n":
                    temp += char
                else:
                    cc += [temp]
                    temp = ""
            count_user +=1
            user += [cc]
            cc = []
    user_file.close()

    #cari id
    for i in range(1,count_user+1):
        if user[i][1] == username:
            id = user[i][0]

    nomor = 1
    validate = False
    print("Daftar game: ")
    for i in range(1,count_own+1):
        if game[i][1] == id:
            temp_game = game[i][0]
            validate = True
        if validate :
            for i in range(1,count_game+1):
                if info_game[i][0]==temp_game:
                    print(str(nomor) +". " + info_game[i][0]+" | "+info_game[i][1]+ " | " + info_game[i][2] + " | " + info_game[i][3] + " | " + info_game[i][4])
                    nomor +=1
            validate = False
# WII = "WII"
# list_game(WII)
