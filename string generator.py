import random
import string

def stringr(length):
    strng = ''.join(random.choice(string.printable) for i in range(length))
    
    return strng
punc = len(string.digits)
stringf= stringr(2000)
file1=open("Message.txt","w")
file1.write(stringf)
file1.close()

