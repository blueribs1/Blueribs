def main():
    '''Takes inputs and calls shift_character to calculate output'''
    char = ord(input("Enter a character: "))
    shift = int(input("Enter shift value: "))
    mode = input("Enter direction (forward/backward): ")
    print("Shifted character: {}".format(shift_character(char, shift, mode)))

def shift_character(char, shift, mode):    
    '''checks to see forward or backward, then checks to make sure letter is upper or lower case, then adds shift'''
    if mode == "forward":
        if char in range(97, 123):
            num_1 = char + shift
            if num_1 in range(97, 123):
                return chr(num_1)
            else:
                num_2 = num_1 % 122
                num_2 += 96
                return chr(num_2)
        elif char in range(65, 91):
            num_1 = char + shift
            if num_1 in range(65, 91):
                return chr(num_1)
            else:
                num_2 = num_1 % 90
                num_2 += 64
                return chr(num_2)
        else: 
            return chr(char)
    
    elif mode == "backward":
        if char in range(97, 123):
            num_1 = char - shift
            if num_1 in range(97, 123):
                return chr(num_1)
            else:
                num_2 = num_1 - 97
                num_2 += 123
                return chr(num_2)
        elif char in range(65, 91):
            num_1 = char + shift
            if num_1 in range(65, 91):
                return chr(num_1)
            else:
                num_2 = num_1 - 65
                num_2 += 91
                return chr(num_2)
        else: 
            return chr(char)
    else: 
        restart = input("Invalid input, try again? (y) or (n): ")
        if restart == "y":
            main()


main()