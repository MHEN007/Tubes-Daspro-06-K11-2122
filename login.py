def login ():
    
    a = 0
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
            a += 1      
            user += [cc]
            cc = []
        
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
