import os
import pickle

from cryptography.fernet import Fernet

# we will be encrypting the below string.
message = "hello geeks"

# generate a key for encryption and decryption
# You can use fernet to generate
# the key or use random key generator
# here I'm using fernet to generate key

key = Fernet.generate_key()
print("key is: ", key.decode()[:5]+"3****")

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

with open(os.path.join(dir_path, "../chat/key.fernet"), "wb") as output_file:
	pickle.dump(key, output_file)
