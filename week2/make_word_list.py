def make_word_list(sentence):
    words = sentence.split(' ')
    frequency_of_word = {}
    for word in words:
        if word in frequency_of_word:
            frequency_of_word[word] += 1
        else:
            frequency_of_word[word] = 1
    
    return frequency_of_word


def main():
    sentence = input("Enter your sentence: ").strip()
    result = make_word_list(sentence=sentence)

    print(result)

if __name__ == "__main__":
    main()