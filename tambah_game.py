import isempty
def tambah_game(nama,kategori,tahun,harga,stok):
    db_game = open("./database/game.csv","a")
    insert = db_game.write(f"{nama};{kategori};{tahun};{harga};{stok}\n") #ditambahkan \n agar buat baris baru
def ulang(a,b,c,d,e):
    if isempty.isempty(a) or isempty.isempty(b) or isempty.isempty(c) or isempty.isempty(d) or isempty.isempty(e):
        return True
    else :
        return False