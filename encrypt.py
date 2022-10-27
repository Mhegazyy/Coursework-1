import string
message = input("Enter Message: \n")
alpha = list(string.ascii_letters)

file1 = open("Key.txt","r+")
key1 = file1.read()
file1.close()



def encrypt(plaintext,key):
    enc = ''
    i = 0
    for letter in plaintext:
        if letter == ' ':
            enc += ' '
        else:
            x = (alpha.index(letter)+alpha.index(key[i]))%26
            i += 1 
            enc += alpha[x]
    return enc

encr = encrypt(message,key1)
