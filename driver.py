import encrypt
import decrypt
import keygen

keygen.key2

file = open("Key.txt","r+")
key = file.read()
file.close()

file1 = open("message.txt","r+")
holder = file1.read()
txxt = encrypt.encrypt(holder,key)

file2 = open("Encrypted Text.txt","w")
file2.writelines(txxt)
file2.close()

file1 = open("Encrypted Text.txt","r+")
holder = file1.read()
txxt = decrypt.decrypt(holder,key)

file2 = open("Decrypted Text.txt","w")
file2.writelines(txxt)
file2.close()
