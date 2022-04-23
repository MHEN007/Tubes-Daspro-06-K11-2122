#bagian utama program
#lakukan import terhadap module yang sudah ada
import os
import load
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
import buy_game
import magicshell
import tictactoe

#SKEMA LOAD
user,game_list,history,ownership = load.load()

#Program utama

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
        exit_state = exit.exit(user,game_list,history,ownership)
    elif menu_pilihan =="tambah_game":
        if role == "admin":
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
        else:
            print("Anda tidak berwenang untuk mengakses menu ini!")
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
    elif menu_pilihan == "buy_game":
        if role == "user":
            buy_game.buy_game(username, user, ownership, game_list)
        else:
            print("Anda tidak berwenang untuk mengakses menu ini!")
    elif menu_pilihan == "kerangajaib":
        magicshell.kerangajaib()
    elif menu_pilihan == "tictactoe":
        tictactoe.tictactoe()
    else:
        print("Masukkan pilihan yang benar!")
