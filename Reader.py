#!/usr/bin/python/python3
'''
Read the contents of a file and return the information as a string list.

author: Joey Brown
'''

import os
import csv
import Handler as hndlr

CWD = os.getcwd()
# DEFAULT_DIR_CSV = str(CWD) + "/devkit_xmas/"
# DEFAULT_DIR_LOG = str(CWD) + "/beacon_xmas/"

# Used with DISTANCE/ directory
# Return data read from files
def getData():
    return readFileList(hndlr.getFiles())

# Used with PHASE/ directory
# Return data read from files 
def getPhaseData(device, config):
    return readFileList(hndlr.getPhaseFiles(device, config))

# Return read data from specified directory
def getDataFrom(wDir):
    file_list = hndlr.getFilesFrom(wDir)
    data = readFileList(file_list)
    return data

# Read data from all files in the file list
def readFileList(fl):
    data = []
    for i in range(0, len(fl)):
        fp = fl[i]
        data.append(readFile(fp))
    return {str(hndlr.getFileType(fl[0])) : data}

# Reads the contents of a file (f) from a filepath (fp). 
# Returns list of lines in f as string.
def readFile(fp):
    try:
        f = {}
        if hndlr.isCSV(fp):
            f = {str(hndlr.getFileName(fp)) : readCSV(fp)}
        elif hndlr.isLOG(fp):
            f = {str(hndlr.getFileName(fp)) : readLOG(fp)}
        return f
    except Exception as e:
        print("Error reading file: \n" + str(e))
        exit

# Opens a .CSV file and returns the contents as a string list.
# Each list element is a line.
def readCSV(fp):
    try:
        f = open(fp, "r", encoding="ISO-8859-1")
        next(f) # skip headings
        d = []
        csvReader = csv.reader(f)
        for l in csvReader:
            values = []
            for v in l[-4:-1]:
                values.append(v)
            d.append(values)
        f.close()
        return d
    except Exception as e:
        exit

# Opens a .LOG file and returns the contents as a string list.
# Each list element is a line.
def readLOG(fp):
    try:
        d = []
        with open(fp, 'r', encoding="ISO-8859-1") as f:
            next(f)
            fReadr = csv.reader(f)
            for row in fReadr:
                if len(row) > 0:
                    val = row[0].split("\t")
                    if len(val) == 3:
                        d.append(val)
        f.close()
        return d
    except Exception as e:
        print("***\nError reading LOG file: \n" + str(e) + "\n***\n")
        exit

    
# 
# 
# 
#       MAIN
# 
# 
# 

def main():
    ''' DISTANCE/ example: '''
    # print(getData())

    ''' PHASE/ example: '''
    print(getPhaseData('Beacon', 'straight'))
    

if __name__ == '__main__':
    main()