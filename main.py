#bagian utama program
#lakukan import terhadap module yang sudah ada
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

#Program utama
#Skema Login
print("Selamat Datang di Toko BNMO")

login_state = False #inisialisasi state awal
print("Silakan Login!")
username = input("Masukkan Username: ")
password = input("Masukkan Password: ")
login_state = login.login(username, password) #minta tolong ditambahkan supaya bisa tarik user_id buat menu search_my_game

while login_state == False:
    print("Username/Password salah, silakan ulangi login!")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    login_state = login.login(username, password)

#Pesan sukses login
print(f"Selamat datang {username}!")

#SKEMA MENU
#inisialisasi
role = "user" #nanti harus didefinisikan dari login
exit_state = False #deklarasi exit state
loop_state = True
input_state = False

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
            tambah_game.tambah_game(nama_game,kategori,tahun,harga,stok)
            input_state = False
    elif menu_pilihan == "search_my_game":
        if role == "user":
            search_my_game() #tolong diisi parameternya adalah user_id
        else:
            print("Anda tidak berwenang untuk mengakses menu ini!")
    elif menu_pilihan == "topup":
        if role == "admin":
            topup.topup()
        else: #role != admin
            print("Anda tidak berwenang untuk mengakses menu ini!")
    elif menu_pilihan == "list_game":
        list_game.list_game(username)
    elif menu_pilihan == "search_game_at_store":
        search_game_at_store.searchGameAtStore()
    elif menu_pilihan == "riwayat":
        if role == "user":
            riwayat.riwayat(username)
        else:
            print("Anda tidak berwenang untuk mengakses menu ini!")
    else:
        print("Masukkan pilihan yang benar!")
