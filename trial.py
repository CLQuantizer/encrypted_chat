from string_encryption.encrypt import decrypt
from string_encryption.encrypt import encrypt

msg = "dsfsgdfdsfsdf"
enc = encrypt(msg)
dec = decrypt(enc)
print(dec)
print(type(dec))