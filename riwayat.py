def riwayat(username, history):
    '''
    #Akses database riwayat.csv
    history = []
    temp = ""
    cc= []
    count_hist = -1
    with open("./database/riwayat.csv","r") as history_data:
        for row in history_data:
            for char in row:
                if char != ";" and char!="\n":
                    temp += char
                else:
                    cc += [temp]
                    temp = ""
            history += [cc]
            cc = []
            count_hist +=1
    '''
    count_hist = -1
    for row in history:
        count_hist += 1
        
    nomor = 1
    for i in range(1,count_hist+1):
        if history[i][3]==username:
            print(str(nomor) + ". " +history[i][0]+ " | "+history[i][1]+" | " + history[i][2] + " | " + history[i][4])
#WII = "WII"
#riwayat(WII, [['game_id', 'nama', 'harga', 'username', 'tahun'],['GAME001', 'Tomb Raider', '500000', 'WII', '2022']])