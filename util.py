import re

class utils:
    def words(text):
        return len(text.split())

    def characters(text):
        return len(re.sub('[^a-zA-Z0-9 \.\:]', '', text))

    def sentences(text):
        return len(text.split('.'))

    def frequency_char(text):
        temp = {i : text.count(i) for i in set(text)}
        rchar = sorted(temp.items(), key =
             lambda kv:(kv[1], kv[0]), reverse=True)
        return rchar

    def frequency_word(text):
        temp = {i : text.count(i) for i in list(text.split())}
        rword = sorted(temp.items(), key =
             lambda kv:(kv[1], kv[0]), reverse=True)
        return rword

    #vowels
    #punctuations