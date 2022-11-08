import string
# This is the variable that will hold the list of the alphabet
alphau = list(string.ascii_uppercase)
alphal = list(string.ascii_lowercase)
punctuation=list(string.punctuation)
digits  = list(string.digits)
alphal.extend(punctuation)
alphau.extend(punctuation)
alphal.extend(digits)
alphau.extend(digits)

# This segment is to grab the key from the txt file
file1 = open("Key.txt","r+")
key1 = file1.read()
file1.close()


# This is the encryption function
def encrypt(plaintext,key):
    enc = []
    i = 0
    for letter in plaintext:

        if letter in alphau:
            if key[i] in alphau:
                x = (alphau.index(letter)+alphau.index(key[i]))%68
                i += 1 
                enc.append(alphau[x])
                
            elif key[i] in alphal:
                x = (alphau.index(letter)+alphal.index(key[i]))%68
                i += 1 
                enc.append(alphau[x])
            else:
                enc.append(letter)
                
        elif letter in alphal:
            if key[i] in alphal:
                x = (alphal.index(letter)+alphal.index(key[i]))%26
                i += 1 
                enc.append(alphal[x])
            elif key[i] in alphau:
                x = (alphal.index(letter)+alphau.index(key[i]))%26
                i += 1 
                enc.append(alphal[x])
            else:
                enc.append(letter)
        else:
            enc.append(letter)
        
    return ''.join(enc)






