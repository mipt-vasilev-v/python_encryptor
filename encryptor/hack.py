import train
import coding
import ciphers

def hack(args):
    alphabet_len = {"eng" : 26, "ru" : 33}
    d = vars(args)
    d["text_file"] = args.input_file
    stat, lang = train.analyze(args)[0], train.analyze(args)[1]
    model = []
    with open(args.model_file, "r") as f:
        for line in f:
            model.append(float(line.split()[1]))
    min_dependence = 1
    min_key = -1
    for key in range(alphabet_len[lang]):
        dependence = 0
        for i in range(alphabet_len[lang]):
            dependence += (model[i] - stat[(i + key) % alphabet_len[lang]]) ** 2
        if dependence < min_dependence:
            min_key = key
            min_dependence = dependence
    d["cipher"] = "caesar"
    d["key"] = min_key
    coding.command(args, "decode")
