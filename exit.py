def exit():
    print("Apakah Anda ingin keluar dari aplikasi ini? (Y/N) ", end="")
    confirm_exit = input()
    #exit_state = False
    state = False
    while state == False:
        if confirm_exit == "Y" or confirm_exit == "y" or confirm_exit == "N" or confirm_exit == "n":
            state = True
            if confirm_exit == "Y" or confirm_exit == "y":
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