import save,os,time

def exit(save_state,user,game_list,history,ownership):
    print("Apakah Anda ingin keluar dari aplikasi ini? (Y/N) ", end="")
    confirm_exit = input()
    #exit_state = False
    state = False
    while state == False:
        if confirm_exit == "Y" or confirm_exit == "y" or confirm_exit == "N" or confirm_exit == "n":
            state = True
            if confirm_exit == "Y" or confirm_exit == "y":
                if save_state == False: #kalau belum ada aksi save sebelumnya, lakukan autosave
                    parent_dir = './save/' #folder penyimpanan untuk prosedur save
                    folder = time.strftime("%d-%m-%Y") #nama folder default

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
                exit_state = False
        else:
            state = False
            print("Apakah Anda ingin keluar dari aplikasi ini? (Y/N) ", end="")
            confirm_exit = input()
    return exit_state

#tes
#exit()