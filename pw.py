import random


start = raw_input("Do you want your password to be strong, very strong or super strong? ")
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = []

def read_file_randomly():
    pword = []
    with open('sexywords.txt', 'r') as f:
        for line in f:
            pword.append(line.strip())
        return random.choice(pword)

if start == 'strong':
    word = read_file_randomly().title()
    for num in range(5):
        digit = random.choice(numbers)
        word = word + str(digit)
    print word






#if start == 'very strong':


#if start == 'super strong':
