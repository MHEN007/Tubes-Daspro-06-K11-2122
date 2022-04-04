#bagian utama program
#lakukan import terhadap module yang sudah ada
import help
import exit
import login
import tambah_game
import isempty

#Program utama
#Skema Login
print("Selamat Datang di Toko BNMO")

login_state = False #inisialisasi state awal
print("Silakan Login!")
username = input("Masukkan Username: ")
password = input("Masukkan Password: ")
login_state = login.login(username, password)

while login_state == False:
    print("Username/Password salah, silakan ulangi login!")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    login_state = login.login(username, password)

#Pesan sukses login
print(f"Selamat datang {username}!")

#SKEMA MENU
#inisialisasi
role = "admin" #nanti harus didefinisikan dari login
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
    else:
        print("Masukkan pilihan yang benar!")
