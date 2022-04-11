def topup(user):
    '''
    user = []
    temp = ""
    cc = []
    count = 0
    found = False
    with open('./database/user.csv', 'r') as user_file:
        for row in user_file:
            for char in row:
                if char != ";" and char != "\n":
                        temp += char
                else: #char == ";"
                    cc += [temp]
                    temp = ""
            user += [cc]
            cc = []
            count +=1
    count -=1
    '''
    count = 0
    for row in user:
        count += 1
    count -= 1

    us = input("Masukkan username: ")
    saldo = int(input("Masukkan saldo: "))
    for i in range(1,count+1):
        if user[i][1] == us:
            if saldo>0 or saldo+user[i][5]>0:
                saldo_akhir = int(user[i][5])
                saldo_akhir += saldo
                user[i][5] = str(saldo_akhir)
                found = True
                break
            else:
                print("Masukan tidak valid")
    if found==False:
        print('Username "'+us+ '" tidak ditemukan.')
    else:
        print("Top up berhasil. Saldo "+us+ " bertambah menjadi "+str(saldo_akhir))
    return(user)