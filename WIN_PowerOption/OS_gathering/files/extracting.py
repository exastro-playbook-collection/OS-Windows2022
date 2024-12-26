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
PowerOption = {}

guid = 0
filepath0 = path + '/command/0/stdout.txt'
if os.path.isfile(filepath0) and os.path.getsize(filepath0) > 0:
    with open(filepath0) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line) > 0:
                params = re.split(':', line.strip())
                if len(params) == 2:
                    guid_split = params[1].strip().split('(')
                    if len(guid_split)>1:
                        guid = guid_split[0].strip()
guidName = ''
filepath1 = path + '/command/1/stdout.txt'
if os.path.isfile(filepath1) and os.path.getsize(filepath1) > 0:
    with open(filepath1) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line) > 0 and guid != 0:
                guidName_split = re.split(guid, line.strip())
                if len(guidName_split) > 1:
                    guidName = guidName_split[1].strip()
if guidName != '':
  if guidName == 'SCHEME_BALANCED':
      PowerOption['PowerPlanSelection'] = 1
  elif guidName == 'SCHEME_MIN':
      PowerOption['PowerPlanSelection'] = 2
  elif guidName == 'SCHEME_MAX':
      PowerOption['PowerPlanSelection'] = 3

acTime = -1
filepath2 = path + '/command/2/stdout.txt'
if os.path.isfile(filepath2) and os.path.getsize(filepath2) > 0:
    with open(filepath2) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line) > 0:
                acTime_split = re.split('現在の AC 電源設定のインデックス:', line.strip())
                if len(acTime_split) > 1:
                    acTime = int(int(acTime_split[1].strip(), 16)/60)
if acTime != -1:
    PowerOption['OffDisplayTime'] = acTime

result['VAR_WIN_PowerOption'] = PowerOption
print(json.dumps(result))

