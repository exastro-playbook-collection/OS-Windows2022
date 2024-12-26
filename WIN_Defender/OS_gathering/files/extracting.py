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

result_filedata_table = {}

target_filepath_list = []
target_filepath_list.append('/0/stdout.txt')
target_filepath_list.append('/1/stdout.txt')
target_filepath_list.append('/2/stdout.txt')
target_filepath_list.append('/3/stdout.txt')
target_filepath_list.append('/4/stdout.txt')
target_filepath_list.append('/5/stdout.txt')
target_filepath_list.append('/6/stdout.txt')
target_filepath_list.append('/7/stdout.txt')
for target_filepath in target_filepath_list:
    filepath = path + '/command' + target_filepath
    if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath) as file_object:
            reader = json.load(file_object)
            if isinstance(reader, list):
                rows = reader
            else:
                rows = []
                rows.append(reader)
            for row in rows:
                for param_key, param_value in row.items():
                    if param_key == 'DisableNotifications':
                        if target_filepath == '/3/stdout.txt':
                            result_filedata_table['FireWallPublicProfileNotice'] = param_value
                        elif target_filepath == '/4/stdout.txt':
                            result_filedata_table['FireWallStandardProfileNotice'] = param_value
                        elif target_filepath == '/5/stdout.txt':
                            result_filedata_table['FireWallDomainProfileNotice'] = param_value
                    elif param_key == 'PUAProtection':
                        result_filedata_table['BlockApps'] = param_value
                    elif param_key == '(default)':
                        result_filedata_table['BlockDownloads'] = param_value
                    else:
                        result_filedata_table[param_key] = param_value

BlockAppsFlags = True
BlockDownloadsFlags = True
for key,values in  result_filedata_table.items():
    if key == 'BlockApps' and values == 0:
        BlockAppsFlags = False
    elif key == 'BlockDownloads' and values == 0:
        BlockDownloadsFlags = False
if BlockAppsFlags == False and BlockDownloadsFlags == False:
    result_filedata_table['ApplicationBlock'] = 0
else:
    result_filedata_table['ApplicationBlock'] = 1

result = {}
target_parameter_root_key = 'VAR_WIN_Defender'
result[target_parameter_root_key] = result_filedata_table
print(json.dumps(result))

