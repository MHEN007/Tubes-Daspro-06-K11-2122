# Register
nama=input("Masukan nama: ")
username=input("Masukan username: ")
password=input("Masukan password: ")    
for row in user:
    a += 1
    for i in range(a):
        if (username != user[i][2]) and username != nama:
            print(f"Username {username} telah berhasil register ke dalam “Binomo”.")
    else:
        print(f"Username {username} sudah terpakai, silakan menggunakan username lain.")
