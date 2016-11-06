import os
import random
from time import sleep


# A more secure way for this generator is to import words from linux.
#There are several thousand words available.
#Add clear screen function
numbers = [0,1,2,3,4,5,6,7,8,9]
sym = ['~','!','@','#','$','%','^','&','*','?', '_','-', '+','=']


def read_file_randomly():
    pword = []
    with open('foo/sexywords.txt', 'r') as f:
        for line in f:
            pword.append(line.strip())
        return random.choice(pword)

def not_option(n):
    print "Sorry " + n + " is not an option. Try again."
    sleep(3)
    os.system("clear")
    return
    #not_option(input_str)



def start():
    input_str = raw_input("Hello and welcome to your very own password generator!"
    " Do you want your password to be strong,"
    " very strong or super strong? ")

    if input_str == 'strong':
        word = read_file_randomly().title()
        for num in range(2):
            digit = random.choice(numbers)
            word = word + str(digit)
        for num in range(1):
            symbol = random.choice(sym)
            word = word + symbol
        print word
        return

    if input_str == 'very strong':
        word = read_file_randomly().title()
        for i in range(3):
            digit = random.choice(numbers)
            word = word + str(digit)
        for i in range(1):
            second_word = read_file_randomly().title()
            symbol = random.choice(sym)
            word = symbol + word + second_word + symbol
        print word
        return

    if input_str == 'super strong':
        word = read_file_randomly().title()
        for i in range(3):
            digit = random.choice(numbers)
            word = word + str(digit)
        for i in range(1):
            second_word = read_file_randomly().title()
            symbol = random.choice(sym)
            word = symbol + word + second_word + symbol
            word = ''.join(random.sample(word,len(word)))
        print word
        return


    not_option(input_str)
    start()



start()
