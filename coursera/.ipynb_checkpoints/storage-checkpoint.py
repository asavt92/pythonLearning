import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--key', help='This will be option key')
parser.add_argument('--val', help='This will be option val')
print("OK")
print(parser.parse_args())