import logging
import os
import pickle

from cryptography.fernet import Fernet

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path, "../chat/key.fernet"), "rb") as input_file:
	key = pickle.load(input_file)
print("key is: ", key.decode()[:5]+"3****")
fernet = Fernet(key)


def encrypt(msg: str) -> bytes:
	encMessage = fernet.encrypt(str.encode(msg))
	logging.info("%s encrypted to: %s", msg, encMessage.decode()[-5]+"_****")
	return encMessage


def decrypt(enc_msg: bytes) -> bytes:
	return fernet.decrypt(enc_msg)
