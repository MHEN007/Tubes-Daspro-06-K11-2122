def register(username, nama, password, role, saldo):
    db_user = open('./database/user.csv', 'a')
    # get max id
    id = 3 # ini harus cari cara biar bisa dapetin last row!
    insert = db_user.write(f"{id};{username};{nama};{password};{role};{saldo}")

    if insert:
        print(f"Username {username} berhasil didaftarkan!")

register("duca_AS", "Ronald", "12345", "user", "50000") # contoh input
