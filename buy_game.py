user = []
temp = ""
cc = []
with open('C:/Users/Asus/Documents/Tubes GILA/user.csv', 'r') as user_file:
    for row in user_file:
        for char in row:
            if char != ";" and char != "\n":
                temp += char
            else:
                cc += [temp]
                temp = ""
        user += [cc]
        cc = []
user_file.close()
    
ownership = []
temp = ""
cc= []
with open('C:/Users/Asus/Documents/Tubes GILA/kepemilikan.csv', 'r') as own:
    for row in own:
        for char in row:
            if char != ";" and char!="\n":
                temp += char
            else:
                cc += [temp]
                temp = ""
        ownership += [cc]
        cc = []
own.close()
    
game_list = []
temp = ""
cc = []
with open('C:/Users/Asus/Documents/Tubes GILA/game.csv', 'r') as game:
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

def buy_game(username, user, ownership, game_list) :
    
    a = 0
    for row in ownership:
        a += 1
    
    b = 0  
    for row in game_list:
        b += 1
    
    c = 0   
    for row in user:
        c += 1
        
    #cari id
    i = 0
    for i in range(c):
        if user[i][1] == username:
            id = i
            saldo = user[i][5]
    print(id)
    
    id_game = input("Masukkan ID Game: ")
    
    i = 0
    # cari id game di game.csv
    for i in range (b) :
        if id_game == game_list[i][0] :
            harga_game = game_list[i][4]
            stok_game = game_list[i][5]
            nama_game = game_list[i][1]
    
    i = 0
    found = False        
    for i in range (a) :
        print(ownership[i][0])
        print(ownership[i][1])
        if ((id_game == ownership[i][0]) and (id == ownership[i][1])):
            found = True
            print("")
            print("Anda sudah memiliki game ini!")
            break
            
    if found == False :
        if (saldo >= harga_game) and (stok_game > 0):
            saldo = saldo - harga_game
            stok_game -= 1
            print("")
            print("Game " + nama_game + " berhasil dibeli!")
        elif (saldo >= harga_game) and (stok_game <= 0) :
            print("")
            print("Stok game tersebut sedang habis!")
        elif (saldo < harga_game) :
            print("")
            print("Saldo anda tidak cukup untuk membeli game tersebut!")

username = "WII"

buy_game(username, user, ownership, game_list)