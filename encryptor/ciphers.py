import coding
import string
import argparse
from enumerators import Language
from enumerators import lang_len

# english constants
LOWER_ALPHABET_DICT = {i[1]:i[0] + 1 for i in enumerate(string.ascii_lowercase)}
UPPER_ALPHABET_DICT = {i[1]:i[0] + 1 for i in enumerate(string.ascii_uppercase)}
LOWER_INV_ENG = {i[0] + 1:i[1] for i in enumerate(string.ascii_lowercase)}
UPPER_INV_ENG = {i[0] + 1:i[1] for i in enumerate(string.ascii_uppercase)}

# ru constants
ru_lowercase = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
lower_ru_dict = {i[1]:i[0] + 1 for i in enumerate(ru_lowercase)}
upper_ru_dict = {i[1]:i[0] + 1 for i in enumerate(ru_lowercase.upper())}
ru_lower_inv = {i[0] + 1:i[1] for i in enumerate(ru_lowercase)}
ru_upper_inv = {i[0] + 1:i[1] for i in enumerate(ru_lowercase.upper())}


def get_contants(lang):
    res = dict()
    if lang == Language.RUS:
        res["lowercase"] = ru_lowercase
        res["UP"] = upper_ru_dict
        res["LOW"] = lower_ru_dict
        res["UPPER_INV"] = ru_upper_inv
        res["LOWER_INV"] = ru_lower_inv
    elif lang == Language.ENG:       
        res["lowercase"] = string.ascii_lowercase
        res["UP"] = UPPER_ALPHABET_DICT
        res["LOW"] = LOWER_ALPHABET_DICT
        res["UPPER_INV"] = UPPER_INV_ENG
        res["LOWER_INV"] = LOWER_INV_ENG
    return res


def caesar(text, key, command, lang = Language.ENG):
    
    delta = lang_len[lang]
    if command == "decode":
        key = delta - key
    
    key %= delta

    consts = get_contants(lang)
    lowercase, UP, LOW, UPPER_INV, LOWER_INV = (consts[i] for i in consts)
    res = []
    for i in text:
        print(i, end = " ")
        if i.isupper():
            value = (UP[i] + key) % delta if (UP[i] + key) % delta != 0 else delta
            res.append(UPPER_INV[value])
        elif i.islower():
            value = (LOW[i] + key) % delta if (LOW[i] + key) % delta != 0 else delta
            res.append(LOWER_INV[value])
        else:
            res.append(i)
    res_str = "".join(str(i) for i in res)
    return res_str


def vigenere(text, key, command, lang = Language.ENG):
    constants = get_contants(lang)
    lowercase, UP, LOW, UPPER_INV, LOWER_INV = (consts[i] for i in consts)

    amount_of_symbs = 0
    for i in text:
        if i.lower().islower():
            amount_of_symbs += 1

    key_word = key
    key = key_word * (amount_of_symbs // len(key_word))
    i = 0 
    remained_part = []
    for j in range(len(key), amount_of_symbs):
        remained_part.append(key_word[i])
        i += 1
    remained_str = "".join(str(i) for i in remained_part)  
    key += remained_str
    key = key.lower()
    cnt = 0
    res = []
    for i in text:
        if i.lower().islower():
            res.append(caesar(i, LOW[key[cnt]] - 1, command, lang))
            cnt += 1
        else:
            res.append(i)
    res_str = "".join(str(i) for i in res)
    return res_str
