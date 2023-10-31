# Bryan Gonzalez
def encoder(in_str):
    en_str =''
    if len(in_str) == 8:
        use_enc = True
    elif len(in_str) != 8:
        quit()
    for i in range(0,(len(in_str))):
        indiv_char = int(in_str[i])
        indiv_char += 3
        en_str += str(indiv_char)
    return en_str

def decode_password(en_str):
    decoded_password = ""
    for digit in en_str:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password

def main():
    n = 1
    while n == 1:
        print("Menu")
        print("---------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        user_inp = input("Please enter an option: ")
        if user_inp == "1":
            user_str = input("Please enter your password to encode: ")
            encoded_pass = encoder(user_str)
            print("Your password has been encoded and stored!")
        elif user_inp == "2":
            if 'encoded_pass' in locals():
                print(f"The encoded password is {encoded_pass}, and the original password is {decode_password(encoded_pass)}.")
            else:
                print("No encoded password has been stored yet.")
        elif user_inp == '3':
            n = 0
if __name__=="__main__":
    main()
