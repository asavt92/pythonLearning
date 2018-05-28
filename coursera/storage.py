import os
import json
import tempfile
import argparse

parser = argparse.ArgumentParser()

#parser.add_argument('-h','--help', help='1111111')
parser.add_argument('--key', help='This will be option key')
parser.add_argument('--val', help='This will be option val')

args = parser.parse_args()
data = dict()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if(args.key != None):
    try:
        with open(storage_path, 'r+') as f:
            data = json.loads("".join(f.readlines()))
    except:
        pass
    if(args.val != None):
        data.update([(str(args.key), args.val)])
        with open(storage_path, 'w') as f:
            f.writelines(json.dumps(data, sort_keys=True, indent=4))
        print("stored {} = {}".format(args.key,args.val))
    else:
        value = data.get(str(args.key))
        print("get {} = {}".format(args.key,value))
else:
    print("Не указан ни один аргумент командной строки!")