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
result_tmp = {}
type_table32 = {}

filepath = path + '/command/0/stdout.txt'
if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
    with open(filepath) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line) > 0:
                params = re.split(':', line)
                if len(params) == 2:
                    if params[0].strip() == 'RegisteredOrganization':
                        type_table32['RegisteredOrganization'] = params[1].strip()
                    elif params[0].strip() == 'RegisteredOwner':
                        type_table32['RegisteredOwner'] = params[1].strip()

type_table64 = {}
filepath = path + '/command/1/stdout.txt'
if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
    with open(filepath) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line) > 0:
                params = re.split(':', line)
                if len(params) == 2:
                    if params[0].strip() == 'RegisteredOrganization':
                        type_table64['RegisteredOrganization'] = params[1].strip()
                    elif params[0].strip() == 'RegisteredOwner':
                        type_table64['RegisteredOwner'] = params[1].strip()

result_tmp['OwnerAndOrganization32'] = type_table32
result_tmp['OwnerAndOrganization64'] = type_table64
result['VAR_WIN_OwnerAndOrganization'] = result_tmp
print(json.dumps(result))

