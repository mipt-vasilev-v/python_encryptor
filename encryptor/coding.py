import string 
import ciphers

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
    if cipher == "caesar":
        try:
            res = int(key)
        except ValueError:
            raise ValueError("key must be an integer")

    elif cipher == "vigenere":
        res = key
        for i in res:
            if not i in string.ascii_lowercase:
                raise ValueError("Key must be a word in lowercase")

    return res

def get_lang(text):
    for i in text:
        i = i.lower()
        for j in i:
            if j in ciphers.ru_lowercase:
                return "ru"
            elif j in string.ascii_lowercase:
                return "eng"
    return "eng"    

def command(args, command):
    text = get_text(args.input_file, command)
    lang = get_lang(text)
    key = get_key(args.cipher, args.key)
    for i in text:
        if args.cipher == "caesar":
            i = ciphers.caesar(i, key, command, lang)
        elif args.cipher == "vigenere":       
            i = ciphers.vigenere(i, key, command, lang)
        out(args.output_file, i)
