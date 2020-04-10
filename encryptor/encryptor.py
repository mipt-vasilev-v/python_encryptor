import argparse
import encode
import decode
import train
import hack

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_encode = subparsers.add_parser("encode")
parser_encode.add_argument("command", action="store_const", const="encode")
parser_encode.add_argument("--cipher", choices=["caesar", "vigenere"], required=True)
parser_encode.add_argument("--key", required=True)
parser_encode.add_argument("--input-file", default=0)
parser_encode.add_argument("--output-file",default=0)

parser_decode = subparsers.add_parser("decode")
parser_decode.add_argument("command", action="store_const", const="decode")
parser_decode.add_argument("--cipher", choices=["caesar", "vigenere"], required=True)
parser_decode.add_argument("--key", required=True)
parser_decode.add_argument("--input-file", default=0)
parser_decode.add_argument("--output-file",default=0)

parser_train = subparsers.add_parser("train")
parser_train.add_argument("command", action="store_const", const="train")
parser_train.add_argument("--text-file", default=0)
parser_train.add_argument("--model-file", default="model.txt", required=True)

parser_hack = subparsers.add_parser("hack")
parser_hack.add_argument("command", action="store_const", const="hack")
parser_hack.add_argument("--input-file", default=0)
parser_hack.add_argument("--output-file", default=0)
parser_hack.add_argument("--model-file", default="model.txt", required=True)

args = parser.parse_args()
if (args.command == "encode"):
    encode.encode(args)
elif(args.command == "decode"):
    decode.decode(args)
elif(args.command == "train"):
    train.train(args)
else:
    hack.hack(args)