import string
# This is the variable that will hold the list of the alphabet
alpha = list(string.ascii_letters)

# This segment is to grab the key from the txt file
file1 = open("Key.txt","r+")
key1 = file1.read()
file1.close()


# This is the encryption function
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
