import train
import coding
import ciphers
from enumerators import Language
from enumerators import lang_len

def hack(args):
    d = vars(args)
    d["text_file"] = args.input_file
    stat, lang = train.analyze(args)
    model = []
    with open(args.model_file, "r") as f:
        for line in f:
            model.append(float(line.split()[1]))
    min_dependence = 1
    min_key = -1
    for key in range(lang_len[lang]):
        dependence = 0
        for i in range(lang_len[lang]):
            dependence += (model[i] - stat[(i + key) % lang_len[lang]]) ** 2
        if dependence < min_dependence:
            min_key = key
            min_dependence = dependence
    d["cipher"] = "caesar"
    d["key"] = min_key
    coding.command(args, "decode")
