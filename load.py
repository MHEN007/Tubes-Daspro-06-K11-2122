import os
import sys
import argparse
import isempty


# fungsi untuk cek folder
def cekfolder(x):
    exist = os.path.exists(x)
    return exist
    
def load():
    print("loading...")
    parser = argparse.ArgumentParser(usage = "python program_binomo.py <nama_folder>") 
    parser.add_argument("x") # nama untuk argumen
    

    if isempty.lenght(sys.argv) == 1: # cek nama folder
        print("Tidak ada nama folder yang diberikan!")
        sys.exit(1)
    args = parser.parse_args() 
    
    if cekfolder(args.x): # validasi folder
        #PARSE UNTUK user.csv
        user = load_file(args.x, "user")

        #PARSE UNTUK game.csv
        game_list = load_file(args.x, "game")

        #PARSE UNTUK kepemilikan.csv
        ownership = load_file(args.x, "kepemilikan")

        #PARSE UNTUK riwayat.csv
        history = load_file(args.x, "riwayat")
        
        print("Selamat datang di antarmuka “Binomo”")
        return(user,game_list,history,ownership)
    else:
        print(f"Folder “{args.x}” tidak ditemukan.")
        sys.exit() #exit dari program
    
    return
    
def load_file(args, file_name):
    saveas = []
    temp = ""
    cc = []
    with open (f'{args}/{file_name}.csv', "r") as file:
        for row in file:
            for char in row:
                if char != ";" and char!="\n":
                    temp += char
                else:
                    cc += [temp]
                    temp = ""
            saveas += [cc]
            cc = []
    file.close()
    return(saveas)

#load()
