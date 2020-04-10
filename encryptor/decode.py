import encode
import string
import argparse

def caesar_decode(text, key, lang = "eng"):
    if lang == "eng":
        delta = ord('z') - ord('a') + 1
    return encode.caesar(text, delta - key, lang)

def vigenere_decode(text, key, lang = "eng"):    #def key:b
    res = ""

    amount_of_symbs = 0
    for i in text:
        if lang == "eng":
            if i in string.ascii_letters:
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
        if lang == "eng":
            if i in string.ascii_letters:
                res += caesar_decode(i, ord(key[cnt]) - ord('a'))
                cnt += 1
            else:
                res += i
    return res


def decode(args):

    def out(file, *args):
        if file == 0:
            print(*args)
        else:
            with open(file, "w") as f:
                f.write(*args)

    
    if args.cipher == "caesar":
        try:
            key = int(args.key)
        except ValueError:
            raise ValueError("key must be an integer")

        if args.input_file == 0:
            print("Enter text to encode")
            text = input()
            text = caesar_decode(text, key)
            out(args.output_file, text)
        else:
            with open(args.input_file, "r") as file:
                for line in file:
                    line = caesar_decode(line, key)
                    out(args.output_file, line)
    elif args.cipher == "vigenere":
        key = args.key
        for i in key:
            if not 'a' <= i <= 'z':
                raise ValueError("Key must be a word")

        if args.input_file == 0:
            print("Enter text to encode")
            text = input()
            text = vigenere_decode(text, key)
            out(args.output_file, text)
        else:
            with open(args.input_file, "r") as file:
                for line in file:
                    line = vigenere_decode(line, key)
                    out(args.output_file, line)
