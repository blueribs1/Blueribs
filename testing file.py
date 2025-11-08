#testing file
import random
def random():
    while True:
        number = random.randrange(1, 10000000000000000000000000000000000000000000000000000000000000000000000000000)
        print(number)
def func2(string="supercalifragilisticexpialidocious"):
    count = {}
    for letter in string:
        if letter not in count:
            count[letter] = 1
        else:
            count[letter]+=1
    print(count)
def reverse_word(word):
    return "".join(reversed(word))
print(reverse_word("hello world"))
