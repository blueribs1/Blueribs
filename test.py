def main():
    answer = input("Encode or decode? ")
    if answer.lower == "encode":
        encode()
    elif answer.lower == "decode":
        decode()
    else:
        answer = input("Invalid input, try again? (y) or (n): ")
        if answer.lower == "y":
            main()
        elif answer.lower == "n":
            quit
def encode():
    word = input("Enter a word to encode: ")
    shift = int(input("Enter a shift value: "))
    word_size = len(word)
    word_size = word_size + 1
    character = 0
    x = ""
    #print(ord("a"), ord("z"), ord("A"), ord("Z"))
    for f in range(1, word_size):
        character_2 = word[character] 
        letter = ord(character_2)+shift
        if letter in range(97, 123) or letter in range(65, 91):
            x+=chr(letter)
        elif ord(character_2) in range(97, 123):
            letter = (letter%122)+96
            x+=chr(letter)
        elif ord(character_2) in range(65, 91):
            letter = (letter%90)+64
            x+=chr(letter)
        else:
            x+=character_2  
        
        word_size -= 1
        character += 1
    print(x)
def decode():
    word = input("Enter a word to decode: ")
    shift = int(input("Enter a shift value: "))
    word_size = len(word)
    word_size = word_size + 1
    character = 0
    x = ""
    #print(ord("a"), ord("z"), ord("A"), ord("Z"))
    for f in range(1, word_size):
        character_2 = word[character] 
        letter = ord(character_2)-shift
        if letter in range(97, 123) or letter in range(65, 91):
            x+=chr(letter)
        elif ord(character_2) in range(97, 123):
            letter = 122 - (letter-97)
            x+=chr(letter)
        elif ord(character_2) in range(65, 91):
            letter = 90 - (letter-65)
            x+=chr(letter)
        else:
            x+=character_2  
        
        word_size -= 1
        character += 1
    print(x)
main()