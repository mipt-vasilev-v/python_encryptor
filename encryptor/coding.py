import string 
import ciphers
from enumerators import Language, lang_len


def out(file, *args):
    if file is None:
        print(*args)
    else:
        with open(file, "w") as f:
            f.write(*args)


def get_text(input_file, command):
    res = []
    if input_file is None:
        print("Enter text to {}".format(command))
        res.append(input())
    else:
        with open(input_file, "r") as file:
            for line in file:
                res.append(line)
    return res


def get_key(cipher, key):
    if cipher == 'caesar':
        try:
            res = int(key)
        except ValueError:
            raise ValueError("key must be an integer")

    elif cipher == 'viginere':
        res = key
        for sym in res:
            if sym not in string.ascii_lowercase and \
               sym not in ciphers.ru_lowercase:
                raise ValueError("Key must be a word in lowercase")

    return res


def get_lang(text):
    for word in text:
        word = word.lower()
        for sym in word:
            if sym in ciphers.ru_lowercase:
                return Language.RUS
            elif sym in string.ascii_lowercase:
                return Language.ENG
    return Language.ENG    


def command(args, command):
    text = get_text(args.input_file, command)
    lang = get_lang(text)
    key = get_key(args.cipher, args.key)
    for i in text:
        if args.cipher == 'caesar':
            i = ciphers.caesar(i, key, command, lang)
        elif args.cipher == 'viginere':       
            i = ciphers.vigenere(i, key, command, lang)
        out(args.output_file, i)
