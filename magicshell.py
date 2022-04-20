import time as tm

def kerangajaib():
    question = input("Apa pertanyaanmu? ")
    
    m = 134456
    a = 8121
    c = 28411
    x = int(tm.strftime("%S")) #ambil seed
    x = ((a*x) + c) % m #rumus

    simpan = x
    test = []
    for i in range(10000,100000,10000):
        test += [i]

    if test[8]<=simpan:
        print("Ya")
    elif test[7]<=simpan and simpan>test[8]:
        print("Tidak")
    elif test[6]<=simpan and simpan>test[7]:
        print("Sudah jalannya")
    elif test[5]<=simpan and simpan>test[6]:
        print("Sangat Mungkin")
    elif test[4]<=simpan and simpan>test[5]:
        print("Tidak Mungkin")
    elif test[3]<=simpan and simpan>test[4]:
        print("Tanya lagi nanti")
    elif test[2]<=simpan and simpan>test[3]:
        print("Jangan tanya ini lagi")
    elif test[1]<=simpan and simpan>test[2]:
        print("Sangat tidak mungkin")
    elif test[0]<=simpan and simpan>test[1]:
        print("Yakinkan diri")
    else:
        print("Opini yang bagus mahasiswa, sekarang belajar lagi ya")


#kerangajaib()
