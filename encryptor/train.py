import string
from enumerators import Language
from enumerators import lang_len
import ciphers
import coding


def count_string_stat(text, stat, lang = Language.ENG):
    text = text.lower()
    consts = ciphers.get_contants(lang)
    for i in text:
        if i.islower():
            stat[consts["LOW"][i] - 1] += 1


def analyze(args):
    text = coding.get_text(args.text_file, "train")
    lang = coding.get_lang(text)
    stat = [0] * lang_len[lang]
    for i in text:
        count_string_stat(i, stat, lang)
    all_symbs = sum(stat)
    for i in range(len(stat)):
        stat[i] /= all_symbs
    return [stat, lang]


def train(args, lang = Language.ENG):
    stat, lang = analyze(args)
    
    with open(args.model_file, "w") as f:
        consts = ciphers.get_contants(lang)
        for i in range(1, len(stat) + 1):
            f.write(consts["LOWER_INV"][i] + " " + str(stat[i - 1]) + "\n")
