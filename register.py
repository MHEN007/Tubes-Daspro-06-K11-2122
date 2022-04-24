def register(user):
    # Register
    nama=input("Masukan nama: ")
    username=input("Masukan username: ")
    password=input("Masukan password: ")    
    state = False
    while state == False:
        if nama == "" or username == "" or password == "":
            print("Harap mengisi semua data!")
            nama=input("Masukan nama: ")
            username=input("Masukan username: ")
            password=input("Masukan password: ")
        else: #semua terisi    
            state = True
    count_user = 0
    unique = True
    for row in user:
        count_user += 1
        for i in range(count_user):
            if (username == user[i][1]):
               unique = False 

    if unique: #jika username unik
        user += [[count_user, username, nama, password, "user", "0"]] #Masukkan ke user dg role user dan saldo awal 0
        print(f"Username {username} telah berhasil register ke dalam “Binomo”.")
    else:
        print(f"Username {username} sudah terpakai, silakan menggunakan username lain.")
    
    return
