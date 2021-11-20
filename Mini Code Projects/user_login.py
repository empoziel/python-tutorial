print("""
*****************
kullanıcı girişi
*****************

""")


sys_kullanıcı_adı = "Hasan"
sys_parola = "12345"

kullanıcı_adı = input("Kullanıcı adı:")
parola = input("Parola:")

if (kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola):
    print ("Parola Hatalı...")

elif (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
    print("Kullanıcı Adı Hatalı...")

elif (kullanıcı_adı != parola and parola != sys_parola):
    print("Kullanıcı Adı ve Parola Hatalı...")

else:
    print("Sisteme başarıyla giriş yapıldı.")
