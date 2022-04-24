def login (user):
    a = 0
    for row in user:
        a += 1
    
    rolling = True
    while rolling:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print()
        
        hasLogin = False
        
        for i in range(a):
            if (username == user[i][1]) and (password == user[i][3]):
                hasLogin = True
                print("Halo " + (user[i][2]) + "! Selamat datang di Binomo")
            
                if user[i][4] == "admin":
                    return("admin", username, user[i][0])
                    
                elif user[i][4] == "user":
                    return("user", username, user[i][0])
                    
                break
            
        if (hasLogin == False):
            print("Password atau username salah atau tidak ditemukan")
            print()
        
        else:
            rolling = False
    
    return
