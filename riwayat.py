import isempty
def riwayat(username, history):
    count_hist = -1
    for row in history:
        count_hist += 1
    
    #tentukan banyak data dengan username sesuai
    count = 0
    for i in range(1,count_hist+1):
        if history[i][3]==username:
            count +=1
    
    #isi array nama dan harga
    nama_game = [0 for i in range(count)]
    harga_game = [0 for i in range(count)]
    tahun = [0 for i in range (count)]
    game_id = [0 for i in range (count)]
    n = 0
    for i in range(1,count_hist+1):
        if history[i][3] == username:
            nama_game[n] = history[i][1]
            harga_game[n] = history[i][2]
            tahun[n] = history[i][4]
            game_id[n] = history[i][0]
            n +=1
    
    #cari nama game dan harga yang paling panjang
    max_game = 0
    max_harga = 0
    for i in range(0,count):
        if isempty.lenght(nama_game[i])>max_game:
            max_game = isempty.lenght(nama_game[i])
        if isempty.lenght(harga_game[i])>max_harga:
            max_harga = isempty.lenght(harga_game[i])

    #samakan panjang string dengan spasi
    for i in range(0,count):
        if isempty.lenght(nama_game[i])<max_game:
            nama_game[i] = nama_game[i] + (" "*(max_game-isempty.lenght(nama_game[i])))
        if isempty.lenght(harga_game[i])<max_harga:
            harga_game[i] = harga_game[i] + (" "*(max_harga-isempty.lenght(harga_game[i])))

    nomor = 1
    if count == 0:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah buy_game untuk membeli.")
    else:
        for i in range(0,count):
            print(str(nomor)+". "+game_id[i]+" | " + nama_game[i] + " | " + harga_game[i] + " | " + tahun[i])
            nomor +=1
    
    return
# WII = "WII"
# riwayat(WII, [['game_id', 'nama', 'harga', 'username', 'tahun'],['GAME001', 'Tomb Raider', '500000', 'WII', '2022'],['GAME002','League of legends','0','WII','2021']])