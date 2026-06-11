from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)

message = "Testing RSA Performance"
cipher = PKCS1_OAEP.new(key.publickey())

encrypted = cipher.encrypt(message.encode())
decrypted = PKCS1_OAEP.new(key).decrypt(encrypted)

print("Original:", message)
print("Decrypted:", decrypted.decode())

if message == decrypted.decode():
    print("Test Passed")
else:
    print("Test Failed")