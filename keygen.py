import string
import random
# This function will ask the user to input the message meant for encryption
def get_message():
    message = ""
    if message == "":
        message = ("Please Enter Your Message: \n")
        return message 

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

# Deciding the length of the key
length = message1.count(' ')
if length < 4 :
    length = 4

# Calling the functions and storing them in variables
print(length)
key=get_key(length)
message = get_message()
key2 = keygen(message1,key)

# This segment will create a txt file and store the generated full key in it for the driver code
file1=open("Key.txt","w")
file1.write(key2)
file1.close()

# This segment will create a txt file and store the plaintext in it for the driver code
#file1=open("Message.txt","w")
#file1.writelines(message)
#file1.close()

