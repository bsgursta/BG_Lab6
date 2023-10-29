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

def main():
    n = 1
    while n == 1:
        print("Menu")
        print("---------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        user_inp = input("Please enter and option: ")
        if user_inp == "1":
            user_str = input("Please enter your password to encode: ")
            encoded_pass = encoder(user_str)
            print("Your password has been encoded and stored!")
        elif user_inp == '3':
            n = 0
if __name__=="__main__":
    main()
