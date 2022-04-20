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
        '''
        user_src = open(f"{args.x}/user.csv")  
        game_src = open(f"{args.x}/game.csv")
        history_src = open(f"{args.x}/riwayat.csv")
        ownership_src = open(f"{args.x}/kepemilikan.csv")
        '''
        #PARSE UNTUK user.csv
        user = []
        temp = ""
        cc = []
        with open(f'{args.x}/user.csv', 'r') as user_file:
            for row in user_file:
                for char in row:
                    if char != ";" and char != "\n":
                            temp += char
                    else: #char == ";"
                        cc += [temp]
                        temp = ""
                
                user += [cc]
                cc = []
                
        user_file.close()


        #PARSE UNTUK game.csv
        game_list = []
        temp = ""
        cc = []
        with open(f'{args.x}/game.csv',"r") as game:
            for row in game:
                for char in row:
                    if char != ";" and char != "\n":
                        temp += char
                    else:
                        cc += [temp]
                        temp = ""
                game_list += [cc]
                cc = []
        game.close()

        #PARSE UNTUK kepemilikan.csv
        ownership = []
        temp = ""
        cc= []
        with open(f'{args.x}/kepemilikan.csv',"r") as own:
            for row in own:
                for char in row:
                    if char != ";" and char!="\n":
                        temp += char
                    else:
                        cc += [temp]
                        temp = ""
                ownership += [cc]
                cc = []
        own.close()

        #PARSE UNTUK riwayat.csv
        history = []
        temp = ""
        cc = []
        with open (f'{args.x}/riwayat.csv', "r") as history_file:
            for row in history_file:
                for char in row:
                    if char != ";" and char!="\n":
                        temp += char
                    else:
                        cc += [temp]
                        temp = ""
                history += [cc]
                cc = []
        history_file.close()
        print("Selamat datang di antarmuka “Binomo”")
        return(user,game_list,history,ownership)
    else:
        print(f"Folder “{args.x}” tidak ditemukan.")
        sys.exit() #exit dari program
    

#load()
