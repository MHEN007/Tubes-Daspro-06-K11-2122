import isempty
def list_game(username, ownership, game_list, user):
    count_own = -1
    for row in ownership:
        count_own += 1
    
    count_game = -1
    for row in game_list:
        count_game += 1
    
    count_user = -1
    for row in user:
        count_user += 1
        
    #cari id
    for i in range(1,count_user+1):
        if user[i][1] == username:
            id = user[i][0]

    #cari berapa banyak game yang dimiliki
    milik = 0
    for i in range(1,count_own+1):
        if ownership[i][1] == id:
            milik +=1

    #buat list tentang id game yang dimiliki
    owngameid = [0 for i in range(milik)]
    a = 0
    for i in range(1,count_own+1):
        if ownership[i][1] == id:
            owngameid[a] = ownership[i][0]
            a += 1

    #buat list untuk nama game, kategori, tahun, dan harga
    owngamenama = [0 for i in range(milik)]
    owngamekategori = [0 for i in range(milik)]
    owngametahun = [0 for i in range(milik)] 
    owngameharga = [0 for i in range(milik)]
    for i in range(0,milik):
        for j in range(1,count_game+1):
            if owngameid[i] == game_list[j][0]:
                owngamenama[i] = game_list[j][1]
                owngamekategori[i] = game_list[j][2]
                owngametahun[i] = game_list[j][3]
                owngameharga[i] = game_list[j][4]

    #cari nama game dan kategori paling panjang
    max_nama = 0
    max_kategori = 0
    for i in range(0,milik):
        if isempty.lenght(owngamenama[i])>max_nama:
            max_nama = isempty.lenght(owngamenama[i])
        if isempty.lenght(owngamekategori[i])>max_kategori:
            max_kategori = isempty.lenght(owngamekategori[i])
    
    #samakan panjang dengan menambahkan spasi
    for i in range(0,milik):
        if isempty.lenght(owngamenama[i])<max_nama:
            owngamenama[i] = owngamenama[i] + (" "*(max_nama-isempty.lenght(owngamenama[i])))
        if isempty.lenght(owngamekategori[i])<max_kategori:
            owngamekategori[i] = owngamekategori[i] + (" "*(max_kategori-isempty.lenght(owngamekategori[i])))

    nomor = 1
    if milik == 0 :
        print("Maaf, kamu belum membeli game. Ketik perintah buy_game untuk beli.")
    else:
        for i in range(0,milik):
            print(str(nomor)+". "+owngameid[i]+" | "+owngamenama[i]+" | "+owngamekategori[i]+" | "+owngametahun[i]+" | "+owngameharga[i])
            nomor +=1