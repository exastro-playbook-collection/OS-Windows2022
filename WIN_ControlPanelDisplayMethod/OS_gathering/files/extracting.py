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
ControlPanelDisplayMethod = {}

filepath = path + '/command/0/stdout.txt'
if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
    with open(filepath) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line) > 0:
                params = re.split(':', line)
                if len(params) == 2:
                    if params[0].strip() == 'AllItemsIconView':
                        type_table['AllItemsIconView'] = int(params[1].strip())
                    elif params[0].strip() == 'StartupPage':
                        type_table['StartupPage'] = int(params[1].strip())

if len(type_table) > 0:
    for param_key,param_value in type_table.items():
        if param_key == 'AllItemsIconView':
            AllItemsIconView = param_value
        elif param_key == 'StartupPage':
            StartupPage = param_value
    if StartupPage == 0:
        ControlPanelDisplayMethod['DisplayMethod'] = 'category'
    elif AllItemsIconView == 0 and StartupPage == 1:
        ControlPanelDisplayMethod['DisplayMethod'] = 'large'
    elif AllItemsIconView == 1 and StartupPage == 1:
        ControlPanelDisplayMethod['DisplayMethod'] = 'small'
else:
    ControlPanelDisplayMethod['DisplayMethod'] = None

result['VAR_WIN_ControlPanelDisplayMethod'] = ControlPanelDisplayMethod
print(json.dumps(result))

