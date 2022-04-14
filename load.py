import os
import sys
import argparse

#fungsi untuk cek folder
def cekfolder(x):
    exist = os.path.exists(x)
    return exist

def load():
    print("loading...")
    parser = argparse.ArgumentParser(usage = "python program_binomo.py <nama_folder>") 
    parser.add_argument("x") #nama untuk argumen

    if isEmpty(sys.argv) == 1: #cek nama folder
        print("Tidak ada nama folder yang diberikan!")
        sys.exit(1)
    args=parser.parse_args() 
    
    if cekfolder(args.x): # validasi folder
        db_user = open(f"{args.x}/user.csv")  
        db_game = open(f"{args.x}/game.csv")
        db_riwayat = open(f"{args.x}/riwayat.csv")
        db_kepemilikan = open(f"{args.x}/kepemilikan.csv")
        print("Selamat datang di antarmuka “Binomo”") 
    else:
        print(f"Folder “{args.x}” tidak ditemukan.")
    return (db_user.readlines()),db_game.readlines()(db_kepemilikan.readlines())(db_riwayat.readlines())
