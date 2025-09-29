# I went ahead and did decode and encode
def main():
    """Main function, asks to encode or decode and accounting for errors"""
    answer = input("Encode or decode? ")
    if answer.lower() == "encode":
        encode()
    elif answer.lower() == "decode":
        decode()
    else:
        answer = input("Invalid input, try again? (y) or (n): ")
        if answer.lower() == "y":
            main()
        elif answer.lower() == "n":
            quit
def encode():
    """Recieves word, checks the size of the word and creates variables for for() loop"""
    word = input("Enter a word to encode: ")
    shift = int(input("Enter a shift value: "))
    shift%=26
    word_size = len(word)
    word_size = word_size + 1
    character = 0
    output_word = ""
    """ For loop, checks to see if the original letter was in range, then checks to see if shifted letter is in the normal range, 
    if not, it checks to see if its uppercase or lower case and puts the new letter back in range """
    for f in range(1, word_size):
        character_2 = word[character] 
        letter = ord(character_2)+shift
        if ord(character_2) in range(97, 123) or ord(character_2) in range(65, 91):
            if (letter in range(97, 123) and ord(character_2) in range(97, 123)) or (letter in range(65, 91) and ord(character_2) in range(65, 91)):
                output_word+=chr(letter)
            elif ord(character_2) in range(97, 123):
                letter = ((letter-96)%26)+96
                output_word+=chr(letter)
            elif ord(character_2) in range(65, 91):
                letter = ((letter-64)%26)+64
                output_word+=chr(letter)         
        else:
            output_word+=character_2  
        
        word_size -= 1
        character += 1
    print("Encoded word: {}".format(output_word))
    answer = input("Would you like to try again? (y) or (n): ")
    if answer.lower() == "y":
        main()
    elif answer.lower() == "n":
        quit
def decode():
    """Recieves word, checks the size of the word and creates variables for for() loop"""
    word = input("Enter a word to decode: ")
    shift = int(input("Enter a shift value: "))
    shift%=26
    print(shift)
    word_size = len(word)
    word_size = word_size + 1
    character = 0
    output_word = ""
    f=1
    """For loop, checks to see if the shifted letter is already in the normal range, 
    if not, it checks to see if original letter was in range, if it was, then it puts the new letter back in range"""
    while f in range(1, word_size):
        character_2 = word[character] 
        letter = ord(character_2)-shift
        if ord(character_2) in range(97, 123) or ord(character_2) in range(65, 91):
            if (letter in range(97, 123) and ord(character_2) in range(97, 123)) or (letter in range(65, 91) and ord(character_2) in range(65, 91)):
                output_word+=chr(letter)
            elif ord(character_2) in range(97, 123):
                letter = 123 - (97-letter)
                output_word+=chr(letter)
            elif ord(character_2) in range(65, 91):
                letter = 91 - (65-letter)
                output_word+=chr(letter)
        else:
            output_word+=character_2  
        
        word_size -= 1
        character += 1
    print("Encoded word: {}".format(output_word))
    answer = input("Would you like to try again? (y) or (n): ")
    if answer.lower() == "y":
        main()
    elif answer.lower() == "n":
        quit
main()