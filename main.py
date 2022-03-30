#bagian utama program
#lakukan import terhadap module yang sudah ada
import help
import exit
import login

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

#Pemilihan menu
while exit_state == False:
    menu_pilihan = input(">>> ")
    if menu_pilihan == "help":
        help.help(role)
    elif menu_pilihan == "exit":
        exit_state = exit.exit()
    else:
        print("Masukkan pilihan yang benar!")
