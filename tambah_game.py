import isempty
def tambah_game(nama,kategori,tahun,harga,stok,game_list):
    count_game = 0
    for row in game_list:
        count_game += 1
    #db_game = open("./database/game.csv","a")
    #jumlah dari game diasumsikan maksimal 999, jadi cari kemungkinan untuk 3 digit tsb
    if count_game==3:
        id = "GAME" + str(count_game)
    elif count_game==2:
        id = "GAME0" + str(count_game)
    else :
        id = "GAME00" + str(count_game)
    game_list += [[id,nama, kategori, tahun, harga, stok]] 
    return (game_list)

def ulang(a,b,c,d,e):
    if isempty.isempty(a) or isempty.isempty(b) or isempty.isempty(c) or isempty.isempty(d) or isempty.isempty(e):
        return True
    else :
        return False