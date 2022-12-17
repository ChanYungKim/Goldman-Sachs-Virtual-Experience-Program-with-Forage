import hashlib
import codecs

user_lists = open('PasswordsList', 'r')

found = 0

for user in user_lists :
    ids_passwords = user.split(':', 1)
    user_id = ids_passwords [0]
    user_hashed_password = ids_passwords[1]

    common_passwords_list = (codecs.open('CommonPasswordsList.txt', 'r', encoding='utf-8', errors='replace')).readlines()
    #length = len(common_passwords_list.readlines())
    for common_password in common_passwords_list :
        hashed_common_password = hashlib.md5(common_password.replace("\n", "").encode()).hexdigest()
        if user_hashed_password.replace("\n", "") == hashed_common_password:
            print (user_id + "'s Password is CRACKED")
            print("Password Found : " + common_password)
            found += 1
            break
        if common_password.replace("\n", "") == (common_passwords_list [-1]).replace("\n", "") :
            print (user_id + "'s Password is SECURED \n")

print ("%s Passwords are CRACKED" %(found))