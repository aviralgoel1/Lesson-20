import random
while True:
    characters=int(input("How many characters do you want in your password? (min 8)"))

    if characters < 8:
        print("Password must be at least 8 characters long.")
    else:
        password = ""
        for i in range(characters):
            password += random.choice("1234567890qwertyuiopasdfghjklzxcvbnm-=[];'\,./!@£$%^&*()_+}{|:?><±§}¡€#¢∞§¶•ªº–≠πø^¨¥†®´∑œåß∂ƒ©˙∆˚¬…æ÷≥≤µ~∫√ç≈``~")
        print("Your generated password is:", password)