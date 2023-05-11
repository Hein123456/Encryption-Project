import hashlib

def Encrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open("CC-" + filename, "wb")
    file.write(data)
    file.close()
    
def Decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open(filename, "wb")
    file.write(data)
    file.close()
    
def EncryptWithHash(filename, key):
    key = hashlib.sha256(key.encode('utf-8')).digest()
    Encrypt(filename, key)

choice = ""
while choice != "4":
    print("Please select your option.")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Encrypt File with Hashed Key")
    print("4. Quit")
    choice = input()
    if choice in ("1", "2", "3"):
        filename = input("Enter filename with extension:\n")
        key = input("Enter encryption key:\n")
    if choice == "1":
        Encrypt(filename, int(key))
    if choice == "2":
        Decrypt(filename, int(key))
    if choice == "3":
        EncryptWithHash(filename, key)
