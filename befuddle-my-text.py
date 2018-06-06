#This version takes user input
from string import printable
encrypt = dict()
decrypt = dict()

def createCipher(password):
    eArray = list(printable)
    temp = []
    for c in password:
        if c in eArray:
            index = eArray.index(c)
            temp.append(eArray[index])
            del eArray[index]
    eArray = temp + eArray
    temp = list(printable)
    for i in range(len(temp)):
        encrypt[eArray[i]] = temp[i]
        decrypt[temp[i]] = eArray[i]

def encryptDocument(doc):
    encrypted = ''
    doc = open(doc, "r")
    if doc.mode == 'r':
        doc = doc.read()
    for c in doc:
        encrypted = encrypted + encrypt[c]
    doc2 = open("encrypted.txt", "w+")
    if doc2.mode == 'w+':
        doc2.write(encrypted)

def decryptDocument(doc):
    decrypted = ''
    encryptedFile = open(doc, "r")
    if encryptedFile.mode == 'r':
        encryptedFile = encryptedFile.read()
    for c in encryptedFile:
        decrypted = decrypted + decrypt[c]
    doc2 = open("decrypted.txt", "w+")
    if doc2.mode == 'w+':
        doc2.write(decrypted)

password = input("\nWhat's the password?\n > ")
createCipher(password)
doc = input("\nWhat is the name of your document?\n >")
choice = input("\nWould you like to encrypt or decrypt this document?\n >")
if choice == "encrypt":
    encryptDocument(doc)
    print("Encryption complete! Have a nice day :)")
elif choice == "decrypt":
    decryptDocument(doc)
    print("\n Decryption complete! Have a nice day :)")
else:
    print("Goodbye.")
