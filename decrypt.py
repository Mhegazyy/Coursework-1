from ast import Or
import string

# This is the variable that will hold the list of the alphabet
alphau = list(string.ascii_uppercase)
alphal = list(string.ascii_lowercase)
punctuation=list(string.punctuation)
#alpha.extend(punctuation)

# This is the function to decrypt the plaintext
def decrypt(message,key):
    dec = ''
    i = 0
    for letter in message:
        if letter == ' ':
            dec += ' '
        elif letter == '\n':
            dec += '\n'
        elif letter not in alphau or alphal:
            dec += letter
            continue
        elif letter in alphal:
            x = (alphal.index(letter)-alphal.index(key[i])+26)%26
            i += 1
            dec += alphal[x]
        else:
            x = (alphau.index(letter)-alphau.index(key[i])+26)%26
            i += 1
            dec += alphau[x]
    return dec


