import encrypt
import decrypt
import keygen

keygen.key2

file = open("Key.txt","r+")
key = file.read()
file.close()

file1 = open("message.txt","r+")
holder = file1.read()
tt = encrypt.encrypt(holder,key)

file2 = open("Encrypted Text.txt","w")
file2.writelines(tt)
file2.close()

file1 = open("Encrypted Text.txt","r+")
holder = file1.read()
tt = decrypt.decrypt(holder,key)

file2 = open("Decrypted Text.txt","w")
file2.writelines(tt)
file2.close()
