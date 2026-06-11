from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open("private.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

with open("encrypted_message.txt", "rb") as f:
    encrypted_data = f.read()

cipher = PKCS1_OAEP.new(private_key)
decrypted = cipher.decrypt(encrypted_data)

print("Decrypted Message:", decrypted.decode())