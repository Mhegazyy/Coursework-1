import string

# This is the variable that will hold the list of the alphabet
alpha = list(string.ascii_letters)


# This is the function to decrypt the plaintext
def decrypt(message,key):
    dec = ''
    i = 0
    for letter in message:
        if letter == ' ':
            dec += ' '
        else:
            x = (alpha.index(letter)-alpha.index(key[i])+26)%26
            i += 1
            dec += alpha[x]
    return dec


