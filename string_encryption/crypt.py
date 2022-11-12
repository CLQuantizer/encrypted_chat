import os
import random
from cryptography.fernet import Fernet
import pickle
# we will be encrypting the below string.
message = "hello geeks"

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path,"key.fernet"), "rb") as input_file:
	key = pickle.load(input_file)

print("key is: ", key)
# Instance the Fernet class with the key
fernet = Fernet(key)
 
# then use the Fernet class instance
# to encrypt the string string must
# be encoded to byte string before encryption
encMessage = fernet.encrypt(message.encode())
 
print("original string: ", message)
print("encrypted string: ", encMessage)
 
# decrypt the encrypted string with the
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods
decMessage = fernet.decrypt(encMessage).decode()
 
print("decrypted string: ", decMessage)