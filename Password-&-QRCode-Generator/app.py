import random
import qrcode
import string

def password_generate(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    symbol = string.punctuation
    mixed = lower + upper + digit + symbol
    password = ''.join(random.sample(mixed,length))
    return password

def qrcode_generate(password):
    file = input("Enter File Name :")
    img = qrcode.make(password)
    img.save(file+".png")
    
def main():
    length = int(input("Enter Password Length : "))
    password = password_generate(length)
    print(f"Your Password is : {password}")
    qrcode_generate(password)
    print("Your password has been save as a QR code.")

if __name__ == "__main__" :
    main()
