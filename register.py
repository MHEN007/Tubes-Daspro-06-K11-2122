def register(user):
    # Register
    nama=input("Masukan nama: ")
    username=input("Masukan username: ")
    password=input("Masukan password: ")    
    count_user = 0
    unique = False
    for row in user:
        count_user += 1
        for i in range(count_user):
            if (username != user[i][1]):
               unique = True 

    if unique: #jika username unik
        user += [[count_user, username, nama, password, "user", "0"]] #Masukkan ke user dg role user dan saldo awal 0
        print(f"Username {username} telah berhasil register ke dalam “Binomo”.")
        return(user)
    else:
        print(f"Username {username} sudah terpakai, silakan menggunakan username lain.")
