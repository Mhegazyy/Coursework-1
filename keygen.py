import string
import random

def get_message():
    message = ""
    if message == "":
        message = input("Please Enter Your Message: \n")
        return message 

def get_key(length):
    key = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return key

key=get_key(4)

def keygen(text,k):
    i = 0
    while True:
        if len(k) == len(text):
            break
        if text[i] == " ":
            i += 1
        else:
            k += text[i]
            i += 1
    return k

message = get_message()
key2 = keygen(message,key)

file1=open("Key.txt","w")
file1.write(key2)
file1.close()

file1=open("Message.txt","w")
file1.writelines(message)
file1.close()

