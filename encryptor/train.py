import string
from enumerators import Language
from enumerators import lang_len
import ciphers 
import coding


def count_string_stat(text, stat, lang = Language.ENG):
    text = text.lower()
    lowercase, UP, LOW, UPPER_INV, LOWER_INV = \
        ciphers.get_contants(lang)
    for sym in text:
        if sym.islower():
            stat[LOW[sym] - 1] += 1


def analyze(args):
    text = coding.get_text(args.text_file, "train")
    lang = coding.get_lang(text)
    stat = [0] * lang_len[lang]
    for sym in text:
        count_string_stat(sym, stat, lang)
    all_symbs = sum(stat)
    for i in range(len(stat)):
        stat[i] /= all_symbs
    return stat, lang


def train(args, lang = Language.ENG):
    stat, lang = analyze(args)
    lowercase, UP, LOW, UPPER_INV, LOWER_INV = \
        ciphers.get_contants(lang)
    with open(args.model_file, "w") as f:
        consts = ciphers.get_contants(lang)
        for i in range(1, len(stat) + 1):
            f.write(LOWER_INV[i] + " " + str(stat[i - 1]) + "\n")
