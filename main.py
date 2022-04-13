#bagian utama program
#lakukan import terhadap module yang sudah ada
import os
import help
import exit
import login
import tambah_game
import isempty
import search_my_game
import topup
import list_game
import search_game_at_store
import riwayat
import save
import ubahstok
import ubahGame
import register
import listing

#SKEMA LOAD
#Copa tolong ganti ini dg module load ya... ini buat penyesuaian aja
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
#SKEMA LOAD SELESAI

#Program utama
#Skema Login
print("Selamat Datang di Toko BNMO")

#SKEMA LOGIN
#inisialisasi
role, username, user_id = login.login(user) #nanti harus didefinisikan dari login
exit_state = False #deklarasi exit state
loop_state = True
input_state = False

#SKEMA MENU
#Pemilihan menu
while exit_state == False:
    menu_pilihan = input(">>> ")
    if menu_pilihan == "help":
        help.help(role)
    elif menu_pilihan == "exit":
        exit_state = exit.exit()
    elif menu_pilihan =="tambah_game":
        while loop_state == True:
            nama_game = input("Masukkan nama game: ")
            kategori = input("Masukkan kategori: ")
            tahun = input("Masukkan tahun rilis: ")
            harga = input("Masukkan harga: ")
            stok = input("Masukkan stok awal: ")
            if tambah_game.ulang(nama_game,kategori,tahun,harga,stok)==False:
                loop_state = False
                input_state = True
            else:
                print("Data Kurang!")
                print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        loop_state = True
        if input_state==True:
            tambah_game.tambah_game(nama_game,kategori,tahun,harga,stok,game_list)
            input_state = False
    elif menu_pilihan == "search_my_game":
        if role == "user":
            search_my_game.searchMyGame(user_id, ownership, game_list) #tolong diisi parameternya adalah user_id
        else:
            print("Anda tidak berwenang untuk mengakses menu ini!")
    elif menu_pilihan == "list_game_toko":
        listing.listing(game_list)
    elif menu_pilihan == "topup":
        if role == "admin":
            topup.topup(user)
        else: #role != admin
            print("Anda tidak berwenang untuk mengakses menu ini!")
    elif menu_pilihan == "ubah_stok":
        if role == "admin":
            ubahstok.ubah_stok(game_list)
        else: #role != admin
            print("Anda tidak berwenang untuk mengakses menu ini!")
    elif menu_pilihan == "list_game":
        list_game.list_game(username, ownership, game_list, user)
    elif menu_pilihan == "search_game_at_store":
        search_game_at_store.searchGameAtStore(game_list)
    elif menu_pilihan == "riwayat":
        if role == "user":
            riwayat.riwayat(username, history)
        else:
            print("Anda tidak berwenang untuk mengakses menu ini!")
    elif menu_pilihan == "save":
        save.save(user, game_list, ownership, history)
    elif menu_pilihan == "ubah_game":
        ubahGame.ubah_Game(game_list)
    elif menu_pilihan == "register":
        if role == "admin":
            register.register(user)
        else:
            print("Anda tidak berwenang untuk mengakses menu ini!")
    else:
        print("Masukkan pilihan yang benar!")
