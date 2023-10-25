# Natasha Buehler

def encode(password):
    # Encodes input by increasing each digit by 3
    result = ""
    for i in range(0, len(password)):
        result += str(int(password[i]) + 3)
    return result

def decode(password):
    # Decodes input by decreasing each digit by 3
    result = ""
    for i in range(0, len(password)):
        if (int(password[i])-3) < 0:
            result += str(int(password[i]+10))
        else:
            result += str(int(password[i]) -3)
    return result

def menu():
    # Prints a menu
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit")


def main():
    user_choice = 0
    password = ""
    encoded_pass = ""

    # While loop for menu
    while user_choice != 3:
        menu()
        user_choice = int(input("\nPlease enter an option: "))

        if user_choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_pass = encode(password)
            print("Your password has been encoded and stored!")
        ''' uncomment after adding decode method
        elif user_choice == 2:
            print("The encoded password is " + encoded_pass + ", and the original password is " + decode(encoded_pass) + ".")
        '''
main()
