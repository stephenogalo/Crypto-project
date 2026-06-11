from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

message = "Hello RSA Secure Communication"

with open("public.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

cipher = PKCS1_OAEP.new(public_key)
encrypted = cipher.encrypt(message.encode())

with open("encrypted_message.txt", "wb") as f:
    f.write(encrypted)

print("Message Encrypted Successfully")