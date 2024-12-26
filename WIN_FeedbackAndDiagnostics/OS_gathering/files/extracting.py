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
type_table['ExperiencesAdjust'] = 0
PeriodInNanoSeconds = -1
NumberOfSIUFInPeriod = -1

filepath = path + '/command/0/stdout.txt'
if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
    with open(filepath) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line) > 0:
                params = re.split(':', line)
                if len(params) == 2:
                    if params[0].strip() == 'PeriodInNanoSeconds':
                        PeriodInNanoSeconds = int(params[1].strip())
                    elif params[0].strip() == 'NumberOfSIUFInPeriod':
                        NumberOfSIUFInPeriod = int(params[1].strip())
                        break

if PeriodInNanoSeconds == -1 and NumberOfSIUFInPeriod == -1:
  type_table['FeedbackFrequency'] = 1
elif PeriodInNanoSeconds == 100000000 and NumberOfSIUFInPeriod == -1:
  type_table['FeedbackFrequency'] = 2
elif PeriodInNanoSeconds == 864000000000 and NumberOfSIUFInPeriod == 1:
  type_table['FeedbackFrequency'] = 3
elif PeriodInNanoSeconds == 6048000000000 and NumberOfSIUFInPeriod == 1:
  type_table['FeedbackFrequency'] = 4
elif (PeriodInNanoSeconds == -1 or PeriodInNanoSeconds == 0) and NumberOfSIUFInPeriod == 0:
  type_table['FeedbackFrequency'] = 5

filepath = path + '/command/1/stdout.txt'
if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
    with open(filepath) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line) > 0:
                params = re.split(':', line)
                if len(params) == 2:
                    if params[0].strip() == 'AllowTelemetry':
                        type_table['AllowTelemetry'] = int(params[1].strip())
                        break

filepath = path + '/command/2/stdout.txt'
if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
    with open(filepath) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line) > 0:
                params = re.split(':', line)
                if len(params) == 2:
                    if params[0].strip() == 'TailoredExperiencesWithDiagnosticDataEnabled':
                        type_table['ExperiencesAdjust'] = int(params[1].strip())
                        break

result['VAR_WIN_FeedbackAndDiagnostics'] = type_table
print(json.dumps(result))

