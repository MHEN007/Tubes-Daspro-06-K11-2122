import time as tm

def kerangajaib():
    question = input("Apa pertanyaanmu? ")
    
    #m, a, c dari konstanta yang digunakan oleh module random
    m = 134456
    a = 8121
    c = 28411
    y = int(tm.strftime("%S")) #ambil sekuens dari detik waktu saat ini
    z = int(tm.time()) #cetak waktu saat ini dengan format dari module time

    if y == 0: #handle ketika x = 0 (syarat LCG, 0<X<m)
        y += 1
    
    x = ((y//5)*z) #membuat set X dari operasi antara y dan z
    
    x = ((a*x) + c) % m #rumus LCG

    batas = []
    for i in range(10000,100000,10000): #saat dibatas, hasil LCG paling banyak dalam rentang 10000 s.d. 100000
        batas += [i]

    if batas[8]<=x:
        print("Ya")
    elif batas[7]<=x and x<batas[8]:
        print("Tidak")
    elif batas[6]<=x and x<batas[7]:
        print("Sudah jalannya")
    elif batas[5]<=x and x<batas[6]:
        print("Sangat Mungkin")
    elif batas[4]<=x and x<batas[5]:
        print("Tidak Mungkin")
    elif batas[3]<=x and x<batas[4]:
        print("Tanya lagi nanti")
    elif batas[2]<=x and x<batas[3]:
        print("Jangan tanya ini lagi")
    elif batas[1]<=x and x<batas[2]:
        print("Sangat tidak mungkin")
    elif batas[0]<=x and x<batas[1]:
        print("Yakinkan diri")
    else:
        print("Opini yang bagus mahasiswa, sekarang belajar lagi ya")


#kerangajaib()
