import save,os,time

def exit(user,game_list,history,ownership):
    print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N) ", end="")
    confirm_save = input()
    state = False #state input benar atau salah
    while state == False:
        if confirm_save == "Y" or confirm_save == "y" or confirm_save == "N" or confirm_save == "n":
            state = True
            if confirm_save == "Y" or confirm_save == "y":
                parent_dir = './save/' #folder penyimpanan untuk prosedur save
                folder = time.strftime("%d-%m-%Y") #nama folder default

                state = save.folder_exist(folder, parent_dir) #cek apakah folder tersebut sudah ada atau belum

                if state == False: #kalau folder belum ada
                    os.mkdir(f'{parent_dir}/{folder}')
                
                #save user.csv
                save.save_file(user, "user", parent_dir, folder)

                #save game.csv
                save.save_file(game_list, "game", parent_dir, folder)

                #save kepemilikan.csv
                save.save_file(ownership, "kepemilikan", parent_dir, folder)

                #save riwayat.csv
                save.save_file(history, "riwayat", parent_dir, folder)
                exit_state = True #klo true berarti keluar
            else:
                exit_state = True
        else:
            state = False
            print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N) ", end="")
            confirm_save = input()
    return exit_state

#tes
#exit()