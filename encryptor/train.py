import string
import ciphers
import coding

def count_string_stat(text, stat, lang = "eng"):
    text = text.lower()
    consts = ciphers.get_contants(lang)
    for i in text:
        if i in consts["lowercase"]:
            stat[consts["LOW"][i] - 1] += 1
        else:
            pass


def analyze(args):
    text = coding.get_text(args.text_file, "train")
    lang = coding.get_lang(text)
    stat = []
    for i in range(ciphers.deltas[lang]):
        stat.append(0)
    for i in text:
        count_string_stat(i, stat, lang)
    all_symbs = sum(stat)
    for i in range(len(stat)):
        stat[i] /= all_symbs
    return [stat, lang]


def train(args, lang = "eng"):
    a = analyze(args)
    stat, lang = a[0], a[1] 
    
    f = open(args.model_file, "w")
    consts = ciphers.get_contants(lang)
    for i in range(1, len(stat) + 1):
        f.write(consts["LOWER_INV"][i] + " " + str(stat[i - 1]) + "\n")
