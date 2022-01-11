# Message/File Encrypter and Decrypter
import cryptography
from cryptography import fernet
from cryptography.fernet import Fernet
# Functions for options
def en_message():
    key = Fernet.generate_key()
    msg = input("Enter message to encrypt : ")
    msg = bytes(msg,'utf-8')
    fernet = Fernet(key)
    en_msg = fernet.encrypt(msg)
    print("Encrpted Message is : "+en_msg.decode())
    print("Your Key is : "+key.decode(),end="\n\n")
def en_file():
    key = Fernet.generate_key()
    fernet = Fernet(key)
    file = str(input("Enter full path to file or drag & drop the file : "))
    file = file.strip()
    if file.startswith("'") and file.endswith("'"):
        file = file[1:len(file)-1]
    with open(file,"rb") as tf:
        content = tf.read()
    en_content = fernet.encrypt(content)
    ans = input("Do you want to create new file or overwrite same file (Y(New File)/N(Same File)) : ")
    if ans.lower()=="yes" or ans.lower()=="y": 
        with open("encryptedfile","wb") as tf:
            tf.write(en_content)
    elif ans.lower()=="no" or ans.lower()=="n": 
        with open(file,"wb") as tf:
            tf.write(en_content)
    else:
        with open("encryptedfile","wb") as tf:
            tf.write(en_content)
    print("Your Key is : "+key.decode())
    print("File Successfully Encrypted.",end="\n\n")   
def de_message():
    msg = input("Enter message to decrypt : ")
    key = input("Enter key of message : ")
    try:
        fernet = Fernet(key)
        de_msg = fernet.decrypt(bytes(msg,'utf-8'))
        print("Decrpted Message is : "+de_msg.decode())
    except cryptography.exceptions.InvalidSignature as e:
        print("Invalid Key")
    except cryptography.fernet.InvalidToken as e:
        print("Invalid Key")
    except Exception :
        print("Invalid Decrypted Message")
def de_file():
    file = str(input("Enter full path to file or drag & drop the file : "))
    key = input("Enter key of message : ")
    file = file.strip()
    if file.startswith("'") and file.endswith("'"):
        file = file[1:len(file)-1]
    with open(file,"rb") as tf:
        content = tf.read()
    try:
        fernet = Fernet(key)
        de_content = fernet.decrypt(content)
        ans = input("Do you want to create new file or overwrite same file (Y(New File)/N(Same File)) : ")
        if ans.lower()=="yes" or ans.lower()=="y": 
            with open("encryptedfile","wb") as tf:
                tf.write(de_content)
        elif ans.lower()=="no" or ans.lower()=="n": 
            with open(file,"wb") as tf:
                tf.write(de_content)
        else:
            with open("encryptedfile","wb") as tf:
                tf.write(de_content)
        print("File Successfully Decrypted.",end="\n\n")
    except Exception :
        print("Invalid File or Key")
# Start of Script
flag = True
print("-"*50,end="\n\n")
print("SecretPy Tool || Made by @vamshi-vemula with Python",end="\n\n")
print("-"*50,end="\n")
while flag:
    print("-"*50)
    print("Available options are :-")
    print("1.Encrypt Message")
    print("2.Encrypt File")
    print("3.Decrypt Message")
    print("4.Decrypt File")
    print("-"*50)
    try :
        choice = int(input("Choose any option from above : "))
        if choice==1: en_message()
        elif choice==2: en_file()
        elif choice==3: de_message()
        elif choice==4: de_file()
        else: print("Wrong Choice")
    except ValueError as e:
        print("Invalid Choice")
    ans = input("Do you want to continue (Y/N)? : ")
    if ans.lower()=="yes" or ans.lower()=="y": flag = True
    elif ans.lower()=="no" or ans.lower()=="n": flag = False
    else:
        print("Wrong Input")
        flag = False