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
TimeZone = {}

filepath0 = path + '/command/0/stdout.txt'
if os.path.isfile(filepath0) and os.path.getsize(filepath0) > 0:
    with open(filepath0) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line) > 0:
                params = re.split(':', line.strip())
                if len(params) == 2:
                    if params[0].strip() == 'Id':
                        TimeZone['Id'] = params[1].strip()
                        break
                        
result['VAR_WIN_TimeZone'] = TimeZone
print(json.dumps(result))

