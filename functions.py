import random

def set_word():                                     #choses one word from 'words.txt'
    index = random.randint(0, 0)
    file = open('words.txt', 'r')
    read = file.readlines()
    selected_word = read[index].strip('\n')
