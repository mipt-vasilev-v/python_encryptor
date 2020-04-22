import coding
import string
import argparse

# english constants
LOWER_ALPHABET_DICT = {string.ascii_lowercase[i]:i + 1 for i in range(len(string.ascii_lowercase))}
UPPER_ALPHABET_DICT = {string.ascii_uppercase[i]:i + 1 for i in range(len(string.ascii_uppercase))}
LOWER_INV_ENG = {i + 1:string.ascii_lowercase[i] for i in range(len(string.ascii_lowercase))}
UPPER_INV_ENG = {i + 1:string.ascii_uppercase[i] for i in range(len(string.ascii_uppercase))}

# ru constants
ru_lowercase = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ru_uppercase = ru_lowercase.upper()
ru_letters = ru_lowercase + ru_uppercase
lower_ru_dict = {ru_lowercase[i]:i + 1 for i in range(len(ru_lowercase))}
upper_ru_dict = {ru_uppercase[i]:i + 1 for i in range(len(ru_uppercase))}
ru_lower_inv = {i + 1:ru_lowercase[i] for i in range(len(ru_lowercase))}
ru_upper_inv = {i + 1:ru_uppercase[i] for i in range(len(ru_uppercase))}


deltas = {"eng" : 26, "ru" : 33}


def get_contants(lang):
    res = dict()
    if lang == "ru":
        res["lowercase"] = ru_lowercase
        res["uppercase"] = ru_uppercase
        res["letters"] = ru_letters
        res["UP"] = upper_ru_dict
        res["LOW"] = lower_ru_dict
        res["UPPER_INV"] = ru_upper_inv
        res["LOWER_INV"] = ru_lower_inv
    elif lang == "eng":       
        res["lowercase"] = string.ascii_lowercase
        res["uppercase"] = string.ascii_uppercase
        res["letters"] = string.ascii_letters
        res["UP"] = UPPER_ALPHABET_DICT
        res["LOW"] = LOWER_ALPHABET_DICT
        res["UPPER_INV"] = UPPER_INV_ENG
        res["LOWER_INV"] = LOWER_INV_ENG
    return res


def caesar(text, key, command, lang = "eng"):
    
    delta = deltas[lang]
    if command == "decode":
        key = delta - key
    
    res = ""
    delta = deltas[lang]
    key %= delta

    constants = get_contants(lang)
    lowercase = constants["lowercase"]
    uppercase = constants["uppercase"]
    letters = constants["letters"]
    UP = constants["UP"]
    LOW = constants["LOW"]
    UPPER_INV = constants["UPPER_INV"]
    LOWER_INV = constants["LOWER_INV"]

    for i in text:
        if i in uppercase:
            value = (UP[i] + key) % delta if (UP[i] + key) % delta != 0 else delta
            res += UPPER_INV[value]
        elif i in lowercase:
            value = (LOW[i] + key) % delta if (LOW[i] + key) % delta != 0 else delta
            res += LOWER_INV[value]
        else:
            res += i
    return res


def vigenere(text, key, command, lang = "eng"):
    res = ""
    constants = get_contants(lang)
    lowercase = constants["lowercase"]
    uppercase = constants["uppercase"]
    letters = constants["letters"]
    UP = constants["UP"]
    LOW = constants["LOW"]
    UPPER_INV = constants["UPPER_INV"]
    LOWER_INV = constants["LOWER_INV"]

    amount_of_symbs = 0
    for i in text:
        if i in letters:
            amount_of_symbs += 1

    key_word = key
    key = key_word * (amount_of_symbs // len(key_word))
    i = 0 
    while len(key) != amount_of_symbs:
        key += key_word[i]
        i += 1
    
    key = key.lower()
    cnt = 0
    for i in text:
        if i in letters:
            res += caesar(i, LOW[key[cnt]] - 1, command, lang)
            cnt += 1
        else:
            res += i
    return res
