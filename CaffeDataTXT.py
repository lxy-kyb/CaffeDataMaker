# -*- coding: utf-8 -*-
import sys, getopt
import random
import os

global_folder = ''
global_scale = -1

def SetParameter():
    try:
        options,args = getopt.getopt(sys.argv[1:], 'hf:s:', ['help','folder','scale'])
    except getopt.GetoptError, e:
        print 'Error Mesg:', e
        print 'Not get right parameters. Please add -h see the help.'
        sys.exit(2)
    if len(options) == 0:
        print 'This script need parameters. \nYou can add -h to see the help.'
        sys.exit(1)
    
    opt_Index = 0
    for name, value in options:
        if name in ('-h', '--help'):
            PrintHelp()
            sys.exit(0)
        if name in ('-f', '--folder'):
            global global_folder
            global_folder = value
            opt_Index+=1
        if name in ('-s', '--scale'):
            global global_scale
            try:
                global_scale = float(value)
                opt_Index+=1
            except ValueError, e:
                print e
                sys.exit(-1)
    if opt_Index is not 2:
        print 'Need more parameters. Please add -h to see the help.'
        sys.exit(1)
    

def PrintHelp():
    print '-h   --help          See the help.'
    print '-f   --folder        The main folder of the pictures.'
    print '-s   --scale         The scale of train and validation.'

def InitTxt():
    with open('train.txt', 'w') as f:
        pass
    with open('val.txt', 'w') as f:
        pass

def AppendTrainTxt(pic_list, tag):
    with open('train.txt', 'a') as f:
        for pic in pic_list:
            f.writelines(str.format('{0} {1}\n', pic, tag))

def AppendValTxt(pic_list, tag):
    with open('val.txt', 'a') as f:
        for pic in pic_list:
            f.writelines(str.format('{0} {1}\n', pic, tag))

def GenerateTXT():
    tags = 0
    dict_folder_tags = {}
    dict_folder_pic = {}
    global global_folder
    global global_scale
    if not os.path.isdir(global_folder):
        print 'Parameter -folder', global_folder, 'is not a realy folder.'
        sys.exit(-1)
    folders = os.listdir(global_folder)
    for folder in folders:
        if os.path.isdir(os.path.join(global_folder,folder)):
            dict_folder_tags[folder] = tags
            tags+=1
            dict_folder_pic[folder] = os.listdir(os.path.join(global_folder,folder))       
    InitTxt()
    for key in dict_folder_pic:
        random.shuffle(dict_folder_pic[key])
        trainCount = int(len(dict_folder_pic[key]) * global_scale)
        AppendTrainTxt(dict_folder_pic[key][:trainCount], dict_folder_tags[key])
        AppendValTxt(dict_folder_pic[key][trainCount:], dict_folder_tags[key])

if __name__ == '__main__':
    SetParameter()
    GenerateTXT()