def help(role): #parameter berupa role dari user yang sedang login
    print("====== HELP MENU ======")
    if role == "admin": #menu yang ditampilkan jika rolenya adalah admin
        print("1. register - menu untuk melakukan registrasi user baru")
        print("2. login - menu untuk melakukan login")
        print("3. tambah_game - menu untuk menambah game")
        print("4. list_game_toko - Untuk melihat list game yang dijual pada toko")
        print("5. ubah_game - Untuk mengubah data game")
        print("6. ubah_stok - Untuk mengubah stok game")
        print("7. search_game_at_store - untuk mencari game di toko")
        print("8. topup - untuk melakukan top up saldo pada user")
        print("9. help - untuk melihat perintah yang ada")
        print("10. exit - untuk exit dari program")
    else: #role user. masukan pasti benar karena diambil dari data user.csv. menu yang ditampilkan jika rolenya adalah user
        print("1. login - menu untuk melakukan login")
        print("2. list_game_toko - Untuk melihat list game yang dijual pada toko")
        print("3. buy_game - untuk membeli game")
        print("4. list_game - untuk melihat list game yang dimiliki user")
        print("5. search_my_game - untuk mencari game yang dimiliki user")
        print("6. search_game_at_store - untuk mencari game di toko")
        print("7. riwayat - untuk melihat riwayat pembelian game")
        print("8. help - untuk melihat perintah yang ada")
        print("9. exit - untuk exit dari program")

#tes
#help("admin")