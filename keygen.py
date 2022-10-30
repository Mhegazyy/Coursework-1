import string
import random
from os.path import exists
# This function will ask the user to input the message meant for encryption
if exists('Message.txt') == False:
    file1=open("Message.txt",'w')
    file1.write('')
    file1.close()

if exists('Key.txt') == False:
    file3=open('Key.txt','w')
    file3.write('')
    file3.close()

# This function is to create a random key string using upper and lower case letters
def get_key(length):
    key = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return key

# This function will concatenate the key and message in order to generate the full key for the cipher
def keygen(text,k):
    i=0
    while True:
        if len(k) == len(text):
            break
        if text[i] == " ":
            i += 1
        else:
            k += text[i]
            i += 1
    return k

file2=open("Message.txt","r+")
message1=file2.read()
file2.close()

if message1 == '':
    print("Please Enter A Message In The Message.txt File!")
    exit()

# Deciding the length of the key
length = message1.count(' ')
if length < 4 :
    length = 4

# Calling the functions and storing them in variables
key=get_key(length)
key2 = keygen(message1,key)

# This segment will create a txt file and store the generated full key in it for the driver code
file1=open("Key.txt","w")
file1.write(key2)
file1.close()