def find_longest_word(word_list):
    longest_word = ''
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)
    print(len(longest_word))

words = input('Enter list of words: ')  
word_list = words.split()  
find_longest_word(word_list)