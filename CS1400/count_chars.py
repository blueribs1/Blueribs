# Counts amount of "letter"
def counter(message, letter):
    message = message.lower()
    letter = letter.lower()
    result = message.count(letter)
    return result


def main():
    
    # Input
    message = input("Enter a string: ")
    letter = input("Enter a character to count: ")
    
    # Call counter
    result = counter(message, letter)
   
    # Output and checks if letter was one character
    if len(letter) == 1:
        print("""The character '{}' appears {} time(s) in "{}".""".format(letter, result, message))
    else:
        answer = input("Invalid Character(only one letter), try again? (y) or (n)")
        if answer == "y":
            main()

# Call main function
main()