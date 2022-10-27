import string

alpha = list(string.ascii_letters)

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

decr = decrypt("llg xikfhr gxkmcx","SECRETTHEGERMANAT")

print(decr)


