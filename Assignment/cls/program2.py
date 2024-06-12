import re

def abbreviate_long_words(s):
    long_words = re.findall(r'\b\w{11,}\b', s)
    abbreviated = [word[0] + str(len(word) - 2) + word[-1] for word in long_words]

    for long_word, abbreviated_word in zip(long_words, abbreviated):
        s = s.replace(long_word, abbreviated_word)

    return s 

s = "In English class there is a boy named Hamid. He has little bit problem in writing long words. For eg. some words like 'localization' or 'internationalization' are so long that writing them many times in one text is quite tiresome."
print(abbreviate_long_words(s))