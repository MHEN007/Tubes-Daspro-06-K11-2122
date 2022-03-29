def login(username, password):
    db_user = open('./database/user.csv', 'r')
    print(db_user)

db_user = open('./database/user.csv', 'r')
for row in db_user:
    print(row)