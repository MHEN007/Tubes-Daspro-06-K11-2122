def login(username, password):
    db_user = open('./database/user.csv', 'r') #buka user.csv untuk diread saja
    found_state = 0 #inisialisasi state (found_state)
    for row in db_user: #melakukan traversal row untuk setiap row dalam db_user
        if username in row: #mencari username dalam row yang ingin dicari
            if password in row: #jika username benar, lanjutkan dengan mencari password dalam row yang sama
                found_state += 1 #jika password ditemukan dalam row yang sama found_state ditambah 1
                break #exit dari traversal
    if found_state == 1: #Jika hasilnya 1 maka boleh login (True) jika tidak, tidak boleh login (False)
        return True
    else:
        return False

#TES
#print(login("duca_AS","12345")) #return true

#Cek username dengan if x in y masih kurang baik karena tidak mencari berdasarkan ketepatan (word to word)