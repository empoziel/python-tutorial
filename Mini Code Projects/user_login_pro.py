print("""
*******************
user login pro
*******************
""")

sys_user_name = "hasann"
sys_password= "12345"
giris_hakki =3

while True:
    user_name = input("User Name:")
    password = input("Password:")
    if(user_name != sys_user_name and password == sys_password):
        print("Username is incorrect")
        giris_hakki -= 1
    elif(user_name == sys_user_name and password != sys_password ):
        print("Password is incorrect")
        giris_hakki -= 1
    elif(user_name != sys_user_name and password != sys_password ):
        print("Password and username are incorrect")
        giris_hakki -= 1
    else:
        print("successfully logged into the system")
        break
    if(giris_hakki == 0):
        print("giris_hakki nız bitti")
        break