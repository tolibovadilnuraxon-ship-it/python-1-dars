ism = input("Ism: ")
familiya = input("Familiya: ")

ism_qism = ism[0] + ism[1] + ism[2]
fam_qism = familiya[0] + familiya[1] + familiya[2]

username = ism_qism.lower() + "_" + fam_qism.lower()
print("Username:", username)
