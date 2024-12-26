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
target_filepath_list.append('/8/stdout.txt')
target_filepath_list.append('/9/stdout.txt')
target_filepath_list.append('/10/stdout.txt')
target_filepath_list.append('/11/stdout.txt')
target_filepath_list.append('/12/stdout.txt')
target_filepath_list.append('/13/stdout.txt')
target_filepath_list.append('/14/stdout.txt')
target_filepath_list.append('/15/stdout.txt')
target_filepath_list.append('/16/stdout.txt')
target_filepath_list.append('/17/stdout.txt')
target_filepath_list.append('/18/stdout.txt')
target_filepath_list.append('/19/stdout.txt')
target_filepath_list.append('/20/stdout.txt')
target_filepath_list.append('/21/stdout.txt')
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
                    if param_key == 'Value':
                        if target_filepath == '/0/stdout.txt':
                            result_filedata_table['location'] = param_value
                        elif target_filepath == '/1/stdout.txt':
                            result_filedata_table['webcam'] = param_value
                        elif target_filepath == '/2/stdout.txt':
                            result_filedata_table['microphone'] = param_value
                        elif target_filepath == '/3/stdout.txt':
                            result_filedata_table['userNotificationListener'] = param_value
                        elif target_filepath == '/4/stdout.txt':
                            result_filedata_table['userAccountInformation'] = param_value
                        elif target_filepath == '/5/stdout.txt':
                            result_filedata_table['contacts'] = param_value
                        elif target_filepath == '/6/stdout.txt':
                            result_filedata_table['appointments'] = param_value
                        elif target_filepath == '/7/stdout.txt':
                            result_filedata_table['phoneCallHistory'] = param_value
                        elif target_filepath == '/8/stdout.txt':
                            result_filedata_table['email'] = param_value
                        elif target_filepath == '/9/stdout.txt':
                            result_filedata_table['userDataTasks'] = param_value
                        elif target_filepath == '/10/stdout.txt':
                            result_filedata_table['chat'] = param_value
                        elif target_filepath == '/11/stdout.txt':
                            result_filedata_table['radios'] = param_value
                        elif target_filepath == '/12/stdout.txt':
                            result_filedata_table['bluetoothSync'] = param_value
                        elif target_filepath == '/13/stdout.txt':
                            result_filedata_table['appDiagnostics'] = param_value
                        elif target_filepath == '/14/stdout.txt':
                            result_filedata_table['documentsLibrary'] = param_value
                        elif target_filepath == '/15/stdout.txt':
                            result_filedata_table['picturesLibrary'] = param_value
                        elif target_filepath == '/16/stdout.txt':
                            result_filedata_table['videosLibrary'] = param_value
                        elif target_filepath == '/17/stdout.txt':
                            result_filedata_table['broadFileSystemAccess'] = param_value
                        elif target_filepath == '/18/stdout.txt':
                            result_filedata_table['phoneCall'] = param_value
                        elif target_filepath == '/19/stdout.txt':
                            result_filedata_table['downloadsFolder'] = param_value
                        elif target_filepath == '/20/stdout.txt':
                            result_filedata_table['graphicsCaptureWithoutBorder'] = param_value
                        elif target_filepath == '/21/stdout.txt':
                            result_filedata_table['graphicsCaptureProgrammatic'] = param_value
                    else:
                        result_filedata_table[param_key] = param_value

result = {}
target_parameter_root_key = 'VAR_WIN_PrivateSetting'
result[target_parameter_root_key] = result_filedata_table
print(json.dumps(result))

