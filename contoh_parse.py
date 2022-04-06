#PARSE UNTUK user.csv
user = []
temp = ""
cc = []
with open('./database/user.csv', 'r') as user_file:
    for row in user_file:
        for char in row:
            if char != ";" and char != "\n":
                    temp += char
            else: #char == ";"
                cc += [temp]
                temp = ""
        
        user += [cc]
        cc = []
        
user_file.close()
print(user)


#PARSE UNTUK game.csv
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

#PARSE UNTUK kepemilikan.csv
ownership = []
temp = ""
cc= []
with open("./database/kepemilikan.csv","r") as own:
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

#PARSE UNTUK riwayat.csv
history = []
temp = ""
cc = []
with open ("./database/riwayat.csv", "r") as history_file:
    for row in history_file:
        for char in row:
            if char != ";" and char!="\n":
                temp += char
            else:
                cc += [temp]
                temp = ""
        history += [cc]
        cc = []
history_file.close()