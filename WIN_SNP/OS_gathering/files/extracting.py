import re
import json
import sys
import os

args = sys.argv
if (len(args) < 2):
    sys.exit(1)

path = args[1]
if(path[-1:] == "/"):
    path = path[:-1]

result = {}
type_table = {}

filepath = path + '/command/0/stdout.txt'
if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
    with open(filepath) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line) > 0:
                params = re.split(':', line)
                if len(params) == 2:
                    if params[0].strip() == 'Receive-Side Scaling State':
                        type_table['ReceiveSideScaling'] = params[1].strip()
                    elif params[0].strip() == 'Receive Segment Coalescing State':
                        type_table['ReceiveSegmentCoalescing'] = params[1].strip()

result['VAR_WIN_SNP'] = type_table
print(json.dumps(result))

