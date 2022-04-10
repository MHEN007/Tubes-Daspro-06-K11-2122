import os
import time

def save():
    #PARSE UNTUK user.csv
    user = []
    temp = ""
    cc = []

    #save user.csv
    with open('user.csv', 'w') as new_user_file:
        count = 0
        for i in user:
            count += 1

        for i in range(count):
            new_user_file.write(f"{user[i][0]};{user[i][1]};{user[i][2]};{user[i][3]};{user[i][4]};{user[i][5]}\n")
    new_user_file.close()

    #save game.csv
    with open('game.csv', 'w') as new_game:
        count = 0
        for i in user:
            count += 1

        for i in range(count):
            new_user_file.write(f"{user[i][0]};{user[i][1]};{user[i][2]};{user[i][3]};{user[i][4]};{user[i][5]}\n")
    new_game.close()