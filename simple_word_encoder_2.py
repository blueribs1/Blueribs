# I went ahead and did decode and encode, this time with the shifted_letter function
def main():
    """Main function, asks to encode or decode and accounting for errors"""
    answer = input("Encode or decode? ")
    if answer.lower() == "encode":
        encode_word()
    elif answer.lower() == "decode":
        decode_word()
    else:
        answer = input("Invalid input, try again? (y) or (n): ")
        if answer.lower() == "y":
            main()
        elif answer.lower() == "n":
            quit
def encode_word():
    """Recieves word and shift, and calls word shifter"""
    word = input("Enter a word to encode: ")
    shift = int(input("Enter a shift value: "))
    encode=1
    output_word = shift_letter(shift, word, encode)
    print("Encoded word: {}".format(output_word))
    answer = input("Would you like to try again? (y) or (n): ")
    if answer.lower() == "y":
        main()
    elif answer.lower() == "n":
        quit
def decode_word():
    """Recieves word and shift, and calls word shifter"""
    word = input("Enter a word to decode: ")
    shift = int(input("Enter a shift value: "))
    encode = 0
    output_word = shift_letter(shift, word, encode)
    print("Encoded word: {}".format(output_word))
    answer = input("Would you like to try again? (y) or (n): ")
    if answer.lower() == "y":
        main()
    elif answer.lower() == "n":
        quit
def shift_letter(shift, word, encode):
    """Creates variables needed for for() loop and ensures that the shift is no larger than 26"""
    shift%=26
    word_size = len(word)
    word_size = word_size + 1
    character = 0
    output_word = ""
    """checks to see if decoding or encoding, then goes through shifting each letter
    making sure to keep them within range and shifting them correctly"""
    if encode == 0:
        shift*=-1
    for f in range(1, word_size):
        character_2 = word[character] 
        letter = ord(character_2)+shift
        if ord(character_2) in range(97, 123) or ord(character_2) in range(65, 91):
            if (letter in range(97, 123) and ord(character_2) in range(97, 123)) or (letter in range(65, 91) and ord(character_2) in range(65, 91)):
                output_word+=chr(letter)
            elif ord(character_2) in range(97, 123):
                if encode==1:
                    letter = ((letter-96)%26)+96
                    output_word+=chr(letter)
                elif encode==0:
                    letter = 123 - (97-letter)
                    output_word+=chr(letter)
            elif ord(character_2) in range(65, 91):
                if encode==1:
                    letter = ((letter-64)%26)+64
                    output_word+=chr(letter) 
                elif encode==0:
                    letter = 123 - (97-letter)
                    output_word+=chr(letter)        
        else:
            output_word+=character_2  
        
        word_size -= 1
        character += 1
    return output_word

    
main()