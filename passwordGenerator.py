import random as r
from cryptography.fernet import Fernet

def pwdGenerator():
    lst = ['abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!@#$%^&*()_+-=[]{}<>?', '0123456789']
    l = r.randint(10,15) #lowercase
    u = r.randint(5,10) #uppercase
    s = r.randint(2,5) #symbol
    n = r.randint(2,10) #number

    p = [[],[],[],[]]

    for i in range(l):
        num = r.randint(0,l-1)
        p[0].append(lst[0][num])
    for i in range(u):
        num = r.randint(0,u-1)
        p[1].append(lst[1][num])
    for i in range(s):
        num = r.randint(0,n-1)
        p[2].append(lst[2][num])
    for i in range(n):
        num = r.randint(0,s-1)
        p[3].append(lst[3][num])

    high = 3
    password = ""

    while high != -1:
        num = r.randint(0,high)
        try:
            rand = r.randint(0,len(p[num])-1)
            password += p[num][rand]
            p[num].pop(rand) 
        except:
            high -= 1
            p.pop(num)

    return password

choice = int(input("Enter 1 create new password or 2 to decrypt existing password: "))
fn = 'pwd2.txt'
if choice == 1:
    acc = input("Enter Account Name: ")
    password = pwdGenerator()
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encoded_text = cipher_suite.encrypt(password)
    try: 
        file = open(fn, 'a')
        file.write('ACCOUNT:\n' + acc + '\n')
        file.write('PASSWORD:\n' + encoded_text + '\n')
        file.write('KEY: \n' + key + '\n\n')
        file.close()
    except FileNotFoundError:
        file = open(fn, 'w+')
        file.write('ACCOUNT:\n' + acc + '\n')
        file.write('PASSWORD:\n' + encoded_text + '\n')
        file.write('KEY: \n' + key + '\n\n')
        file.close()
elif choice == 2:
    try:
        file = open('pwd2.txt', 'r')
        next_ = 0
        accounts = []
        num = 1
        lines = []
        for line in file.readlines():
            if line != '\n':
                lines.append(line)
        index = 0
        for line in lines:
            line = line.rstrip()
            inc = 0
            if line == "ACCOUNT:":
                index += inc + 1
                account = lines[index]
                inc += 2
                index += inc 
                pwd = lines[index]
                index += inc
                key = lines[index]
                lst = [num, account, pwd, key]
                accounts.append(lst)
                print('\n' + str(num) + ' ' + account)
                num += 1
                lines.remove('ACCOUNT:\n')
        
        response = int(input("Enter corresponding number for account access: "))
        for i in range(len(accounts)):
            if response == accounts[i][0]:
                cipher_suite = Fernet(accounts[i][3])
                decoded_text = cipher_suite.decrypt(accounts[i][2])
                print(decoded_text)
                break
    except:
        error = input("No passwords saved. Enter new account name or type 'No' to exit: ")
        if error == "No":
            exit()
        password = pwdGenerator()
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encoded_text = cipher_suite.encrypt(password)
        file = open(fn, 'w+')
        file.write('ACCOUNT:\n' + error + '\n')
        file.write('PASSWORD:\n' + encoded_text + '\n')
        file.write('KEY: \n' + key + '\n\n')
        file.close()
