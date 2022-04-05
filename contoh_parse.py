user = []
temp = ""
cc = []
with open('./database/user.csv', 'r') as user_file:
    for row in user_file:
        for char in row:
            if char != ";" and char != "\n":
                    temp += char
            else: #char == ";"
                cc += [temp]
                temp = ""
        
        user += [cc]
        cc = []
        

print(user)
