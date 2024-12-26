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
type_table_tmp = {}

filepath = path + '/command/0/stdout.txt'
if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
    with open(filepath) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line) > 0:
                params = re.split(':', line)
                if len(params) == 2:
                    if params[0].strip() == 'VisualFXSetting':
                        type_table_tmp['visual_type'] = int(params[1].strip())
                        break
else:
    type_table_tmp['visual_type'] = None

filepath = path + '/command/1/stdout.txt'
if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
    with open(filepath) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line) > 0:
                params = re.split(':', line)
                if len(params) == 2:
                    if params[0].strip() == 'IconsOnly':
                        if int(params[1].strip()) == 1:
                            type_table['IconsOnly'] = 'no'
                        else:
                            type_table['IconsOnly'] = 'yes'
                    elif params[0].strip() == 'ListviewAlphaSelect':
                        if int(params[1].strip()) == 0:
                            type_table['ListviewAlphaSelect'] = 'no'
                        else:
                            type_table['ListviewAlphaSelect'] = 'yes'
                    elif params[0].strip() == 'ListviewShadow':
                        if int(params[1].strip()) == 0:
                            type_table['ListviewShadow'] = 'no'
                        else:
                            type_table['ListviewShadow'] = 'yes'
                    elif params[0].strip() == 'TaskbarAnimations':
                        if int(params[1].strip()) == 0:
                            type_table['TaskbarAnimations'] = 'no'
                        else:
                            type_table['TaskbarAnimations'] = 'yes'

filepath = path + '/command/2/stdout.txt'
if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
    with open(filepath) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line) > 0:
                params = re.split(':', line)
                if len(params) == 2:
                    if params[0].strip() == 'MinAnimate':
                        if int(params[1].strip()) == 0:
                            type_table['MinAnimate'] = 'no'
                        else:
                            type_table['MinAnimate'] = 'yes'

filepath = path + '/command/3/stdout.txt'
if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
    with open(filepath) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line) > 0:
                params = re.split(':', line)
                if len(params) == 2:
                    if params[0].strip() == 'EnableAeroPeek':
                        if int(params[1].strip()) == 0:
                            type_table['EnableAeroPeek'] = 'no'
                        else:
                            type_table['EnableAeroPeek'] = 'yes'
                    elif params[0].strip() == 'AlwaysHibernateThumbnails':
                        if int(params[1].strip()) == 0:
                            type_table['AlwaysHibernateThumbnails'] = 'no'
                        else:
                            type_table['AlwaysHibernateThumbnails'] = 'yes'


filepath = path + '/command/4/stdout.txt'
if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
    with open(filepath) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line) > 0:
                params = re.split(':', line)
                if len(params) == 2:
                    if params[0].strip() == 'FontSmoothing':
                        if int(params[1].strip()) == 0:
                            type_table['FontSmoothing'] = 'no'
                        else:
                            type_table['FontSmoothing'] = 'yes'
                    elif params[0].strip() == 'DragFullWindows':
                        if int(params[1].strip()) == 0:
                            type_table['DragFullWindows'] = 'no'
                        else:
                            type_table['DragFullWindows'] = 'yes'

UserPreferencesMask = []
filepath = path + '/command/5/stdout.txt'
if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
    with open(filepath) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line) > 0:
                UserPreferencesMask.append(int(line.strip()))

bin_item = ''
if len(UserPreferencesMask) > 0:
  for index in range(len(UserPreferencesMask)):
    if index == 0:
        bin_item = str(bin(UserPreferencesMask[index]))
        if bin_item[-2] == '0':
            type_table['menu_view'] = 'no'
        elif bin_item[-2] == '1':
            type_table['menu_view'] = 'yes'
        if bin_item[-3] == '0':
            type_table['slide'] = 'no'
        elif bin_item[-3] == '1':
            type_table['slide'] = 'yes'
        if bin_item[-4] == '0':
            type_table['smooth'] = 'no'
        elif bin_item[-4] == '1':
            type_table['smooth'] = 'yes'
    if index == 1:
        bin_item = str(bin(UserPreferencesMask[index]))
        if bin_item[-3] == '0':
            type_table['fade_menu'] = 'no'
        elif bin_item[-3] == '1':
            type_table['fade_menu'] = 'yes'
        if bin_item[-4] == '0':
            type_table['fade_view'] = 'no'
        elif bin_item[-4] == '1':
            type_table['fade_view'] = 'yes'
        if len(bin_item) > 7:
            if bin_item[-6] == '1':
                type_table['mouse_shadows'] = 'yes'
            elif bin_item[-6] == '0':
                type_table['mouse_shadows'] = 'no'
        if len(bin_item) <= 7:
            type_table['mouse_shadows'] = 'no'
    if index == 2:
        bin_item = str(bin(UserPreferencesMask[index]))
        if len(bin_item) > 4:
            if bin_item[-3] == '1':
                type_table['window_shadows'] = 'yes'
            elif bin_item[-3] == '0':
                type_table['window_shadows'] = 'no'
        if len(bin_item) <= 4:
            type_table['window_shadows'] = 'no'
    if index == 4:
        bin_item = str(bin(UserPreferencesMask[index]))
        if len(bin_item) > 3:
            if bin_item[-2] == '1':
                type_table['window_animation'] = 'yes'
            elif bin_item[-2] == '0':
                type_table['window_animation'] = 'no'
        if len(bin_item) <= 3:
            type_table['window_animation'] = 'no'

if type_table_tmp['visual_type'] is not None and type_table_tmp['visual_type'] == 3:
    type_table_tmp['custom_value'] = {}
    type_table_tmp['custom_value'] = type_table

filepath = path + '/command/6/stdout.txt'
if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
    with open(filepath) as file_object:
        lines = file_object.readlines()
        for line in lines:
            if len(line.strip()) == 1:
                type_table_tmp['DataExecutionPrevention'] = int(line.strip())

result['VAR_WIN_VisualEffects'] = type_table_tmp
print(json.dumps(result))

