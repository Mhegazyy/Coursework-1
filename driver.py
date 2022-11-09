# Importing the code files of the program
import keygen
import encrypt
import decrypt

#Opening the key file
file = open("Key.txt","r+")
key = file.read()
file.close()

#Opening the Message file
file1 = open("Message.txt","r+")
holder = file1.read()
txxt = encrypt.encrypt(holder,key)

#Writing the encrypted text
file2 = open("Encrypted Text.txt","w")
file2.write(txxt)
file2.close()

#Pulling the encrypted text from the file for decryption
file1 = open("Encrypted Text.txt","r+")
holder = file1.read()
txxt = decrypt.decrypt(holder,key)

#Writing the decrypted text
file2 = open("Decrypted Text.txt","w")
file2.write(txxt)
file2.close()
