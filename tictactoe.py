import sys
def tictactoe():
    #pemain 1 = x
    #pemain 2 = o
    #declare matrix jawaban
    ans = [["","",""], ["","",""], ["","",""]] #list jawaban
    turn = 1 #putaran ke berapa
    pemain = 1 #yang mulai adalah pemain 1
    while turn <= 9:
        print(f"Giliran Pemain {pemain}")
        if pemain == 1:

            cetak_game(ans)

            input_ans(ans,pemain)
            
            pemain = 2
        
        else: #pemain = 2
            cetak_game(ans)

            input_ans(ans,pemain)
            
            pemain = 1
        
        turn += 1

        #cek jawaban untuk pemain 1
        for i in range(3): #cek untuk setiap baris
            if (ans[i][0] == "X" and ans[0][1] == "X" and ans[0][2] == "X"):
                print()
                print("Pemain 1 menang!")
                cetak_game(ans)
                turn = 10
                menang = True
        for i in range(3): #cek untuk setiap kolom
            if (ans[0][i] == "X" and ans[1][i]=="X" and ans[2][i]=="X"):
                print()
                print("Pemain 1 menang!")
                cetak_game(ans)
                turn = 10
                menang = True
        if (ans[0][0] == "X" and ans[1][1] == "X" and ans[2][2] == "X") or (ans[2][0] == "X" and ans[1][1] == "X" and ans[0][2] == "X"): #cek untuk menyilang
            print()
            print("Pemain 1 menang!")
            cetak_game(ans)
            turn = 10
            menang = True

        #cek jawaban untuk pemain 2
        for i in range(3):#cek untuk setiap baris
            if (ans[i][0] == "O" and ans[0][1] == "O" and ans[0][2] == "O"):
                print()
                print("Pemain 2 menang!")
                cetak_game(ans)
                turn = 10
                menang = True
        for i in range(3):#cek untuk setiap kolom
            if (ans[0][i] == "O" and ans[1][i]=="O" and ans[2][i]=="O"):
                print()
                print("Pemain 2 menang!")
                cetak_game(ans)
                turn = 10
                menang = True
        if (ans[0][0] == "O" and ans[1][1] == "O" and ans[2][2] == "O") or (ans[2][0] == "O" and ans[1][1] == "O" and ans[0][2] == "O"): #cek untuk menyilang
            print()
            print("Pemain 2 menang!")
            cetak_game(ans)
            turn = 10
            menang = True
        print()
    
    #cek variabel menang
    if menang == False:
        print("Draw")
        cetak_game(ans)
            

def cetak_game(ans):
    for row in range (3):
        if row != 2:
            print(f"   {ans[row][0]} | {ans[row][1]} | {ans[row][2]}   ")
            print("-------------")
        else:
            print(f"   {ans[row][0]} | {ans[row][1]} | {ans[row][2]}   ")

def input_ans(ans, pemain):
    row = int(input("Masukkan baris Anda "))
    col = int(input("Masukkan kolom Anda "))

    state = False
    while state == False:
        if ans[row-1][col-1] == "X" or ans[row-1][col-1]=="O":
            print("Tempat itu sudah diisi")
            row = int(input("Masukkan baris Anda "))
            col = int(input("Masukkan kolom Anda "))
        elif row == "" or col == "":
            print("Silakan isi baris dan kolom")
            row = int(input("Masukkan baris Anda "))
            col = int(input("Masukkan kolom Anda "))
        else:
            state = True
    
    if pemain == 1:
        ans[row-1][col-1] = "X"
    else:
        ans[row-1][col-1] = "O"

#tictactoe()