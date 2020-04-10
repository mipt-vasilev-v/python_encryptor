import argparse

def count_string_stat(text, stat, lang = "eng"):
    text = text.lower()
    for i in text:
        if 'a' <= i <= 'z':
            stat[ord(i) - ord('a')] += 1
        elif "а" <= i <= "я":
            stat[ord(i) - ord('а')] += 1
        else:
            pass


def analyze_lang(str):
    for i in str:
        if 'a' <= i <= 'z':
            return 'eng'
        if "а" <= i <= "я":
            return 'ru' 


def analyze(args):
    alphabet_len = {"eng" : 26, "ru" : 33}
    lang = None
    if args.text_file == 0:
        print("Enter text")
        text = input()
        lang = "eng"
        stat = []
        for i in range(alphabet_len[lang]):
            stat.append(0)
        count_string_stat(text, stat, lang)
    else:
        f = open(args.text_file, "r")
        for line in f:
            if lang == None:
                lang = "eng"
                stat = []
                for i in range(alphabet_len[lang]):
                    stat.append(0)
            count_string_stat(line, stat, lang)
        f.close()
    all_symbs = sum(stat)
    for i in range(len(stat)):
        stat[i] /= all_symbs
    return stat


def train(args, lang = "eng"):
    stat = analyze(args)
    f = open(args.model_file, "w")
    for i in range(len(stat)):
        if lang == "ru":
            f.write(chr(ord('а') + i) + " " + str(stat[i]) + "\n")
        elif lang == "eng":
            f.write(chr(ord('a') + i) + " " + str(stat[i]) + "\n")
