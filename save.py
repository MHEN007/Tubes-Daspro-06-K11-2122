import os

def save(user, game_list, ownership, history):
    state = False #state apakah nama folder sudah ada atau belum ada
    parent_dir = './save/' #folder penyimpanan untuk prosedur save
    folder = input("Masukkan nama folder penyimpanan: ")
    
    for (root, files, dirs) in os.walk(f'{parent_dir}'):
        if folder in root: #jika nama folder ada dalam parameter root
            state = True
            break
        else: #jika nama folder tidak ada dalam parameter root
            state = False
    print()
    print("Saving ...")
    if state: #jika nama foldernya ada
        #overwrite/buat semua file yang ada di sana
        #save user.csv
        with open(f'{parent_dir}/{folder}/user.csv', 'w') as new_user_file:
            count = 0
            for i in user:
                count += 1

            for i in range(count):
                new_user_file.write(f"{user[i][0]};{user[i][1]};{user[i][2]};{user[i][3]};{user[i][4]};{user[i][5]}\n")
        new_user_file.close()


        #save game.csv
        with open(f'{parent_dir}/{folder}/game.csv', 'w') as new_game_file:
            count = 0
            for i in game_list:
                count += 1

            for i in range(count):
                new_game_file.write(f"{game_list[i][0]};{game_list[i][1]};{game_list[i][2]};{game_list[i][3]};{game_list[i][4]};{game_list[i][5]}\n")
        new_game_file.close()

        #save kepemilikan.csv
        with open(f'{parent_dir}/{folder}/kepemilikan.csv', 'w') as new_kepemilikan_file:
            count = 0
            for i in ownership:
                count += 1

            for i in range(count):
                new_kepemilikan_file.write(f"{ownership[i][0]};{ownership[i][1]}\n")
        new_kepemilikan_file.close()

        #save riwayat.csv
        with open(f'{parent_dir}/{folder}/riwayat.csv', 'w') as new_riwayat_file:
            count = 0
            for i in history:
                count += 1

            for i in range(count):
                new_riwayat_file.write(f"{history[i][0]};{history[i][1]};{history[i][2]};{history[i][3]}\n")
        new_riwayat_file.close()
        

    else: #jika nama folder tidak ada
        #buat folder nya
        os.mkdir(f'{parent_dir}/{folder}')
        #save user.csv
        with open(f'{parent_dir}/{folder}/user.csv', 'w') as new_user_file:
            count = 0
            for i in user:
                count += 1

            for i in range(count):
                new_user_file.write(f"{user[i][0]};{user[i][1]};{user[i][2]};{user[i][3]};{user[i][4]};{user[i][5]}\n")
        new_user_file.close()


        #save game.csv
        with open(f'{parent_dir}/{folder}/game.csv', 'w') as new_game_file:
            count = 0
            for i in game_list:
                count += 1

            for i in range(count):
                new_game_file.write(f"{game_list[i][0]};{game_list[i][1]};{game_list[i][2]};{game_list[i][3]};{game_list[i][4]};{game_list[i][5]}\n")
        new_game_file.close()

        #save kepemilikan.csv
        with open(f'{parent_dir}/{folder}/kepemilikan.csv', 'w') as new_kepemilikan_file:
            count = 0
            for i in ownership:
                count += 1

            for i in range(count):
                new_kepemilikan_file.write(f"{ownership[i][0]};{ownership[i][1]}\n")
        new_kepemilikan_file.close()

        #save riwayat.csv
        with open(f'{parent_dir}/{folder}/riwayat.csv', 'w') as new_riwayat_file:
            count = 0
            for i in history:
                count += 1

            for i in range(count):
                new_riwayat_file.write(f"{history[i][0]};{history[i][1]};{history[i][2]};{history[i][3]}\n")
        new_riwayat_file.close()

    #kalau sudah selesai melakukan save
    print("Data telah disimpan pada folder {}".format(folder))