import unittest
import encrypt

file = open('Key.txt','r+')
key = file.read()
file.close()

file1 = open('Message.txt','r+')
original = file1.read()
file1.close()

file2 = open('Encrypted Text.txt','r+')
encrypted = file2.read()
file2.close()

file3 = open('Decrypted Text.txt','r+')
decrypted = file3.read()
file3.close()


class TestCode(unittest.TestCase):

    def testEncrypt(self):
        self.assertEqual(encrypt.encrypt(original,key),encrypted,'The Ciphers Do Not Match!')
    
    def testDecrypt(self):
        self.assertEqual(original,decrypted,'The Decrypted Text Does Not Match The Original Message!')

if __name__ == '__main__':
    unittest.main()
