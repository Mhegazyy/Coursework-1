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

# This is the function to decrypt the plaintext
def decrypt(plaintext,key):
    dec = ''
    i = 0
    for letter in plaintext:

        if letter in alphau:
            if key[i] in alphau:
                x = (alphau.index(letter)-alphau.index(key[i])+68)%68
                i += 1 
                dec += alphau[x]
                
            elif key[i] in alphal:
                x = (alphau.index(letter)-alphal.index(key[i])+68)%68
                i += 1 
                dec += alphau[x]
            else:
                dec += letter

        elif letter in alphal:
            if key[i] in alphal:
                x = (alphal.index(letter)-alphal.index(key[i])+26)%26
                i += 1 
                dec += alphal[x]
            elif key[i] in alphau:
                x = (alphal.index(letter)-alphau.index(key[i])+26)%26
                i += 1 
                dec += alphal[x]
            else:
                dec += letter
        else:
            dec += letter
        
    return dec


