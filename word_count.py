
#Exercise 3 - Counting occurences of words in a string

def main ():
    word_dict = {}
    user_sentence = str(input("Enter a string of text here:"))
    user_words = user_sentence.split()

    for word in user_words:
        number_of_words = word_dict.get(word, 0)
        word_dict[word] = number_of_words + 1

    user_words = list(word_dict.keys())
    user_words.sort()

    char_length = max((len(word) for word in user_words))
    for word in user_words:
        print("{:{}} : {}".format(word, char_length, word_dict[word]))


main()
