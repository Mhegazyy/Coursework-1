import random
import string

def stringr(length):
    strng = ''.join(random.choice(string.ascii_letters) for i in range(length))
    
    return strng

stringf= stringr(100)
file1=open("Message.txt","w")
file1.write(stringf)
file1.close()