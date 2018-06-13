'''
Read the contents of a file and return the information as a string list.

author: Joey Brown
'''

import os
import csv
import Handler as H

CWD = os.getcwd()
DEFAULT_DIR_CSV = str(CWD) + "/devkit_xmas/"
DEFAULT_DIR_LOG = str(CWD) + "/beacon_xmas/"


def getData():
    return getDataFrom(getFiles())

def getDataFrom(wDir):
    fl = H.getFilesFrom(wDir)
    print(fl)
    # for f in fl:
    #     fp = wDir + "/" + f
    #     print(fp)

# Reads the contents of a file (f) from a filepath (fp). 
# Returns list of lines in f as string.
def readFile(fp):
    try:
        f = []
        if H.isCSV(fp):
            f = readCSV(fp)
        elif H.isLOG(fp):
            f = readLOG(fp)
        return f
    except Exception as e:
        print("Error reading file: \n" + str(e))
        exit

# Read data from all files in the file list
def readFileList(fl):
    data = []
    for f in fl:
        print(readFile(f))
        # data.append(readFile(f))

# Opens a .CSV file and returns the contents as a string list.
# Each list element is a line.
def readCSV(fp):
    try:
        f = open(fp, "r", encoding="ISO-8859-1")
        next(f) # skip headings
        d = []
        csvReader = csv.reader(f)
        for l in csvReader:
            d.append(l)
        f.close()
        return d
    except Exception as e:
        print("***\nError reading CSV file: \n" + str(e) + "\n***\n")
        exit

# Opens a .LOG file and returns the contents as a string list.
# Each list element is a line.
def readLOG(fp):
    print("dadsfasdfasdfasdf")
    try:
        # return readFile(fp)
        d = []
        with open(fp, 'r', encoding="ISO-8859-1") as f:
            fReadr = csv.reader(f)
            for row in fReadr:
                if len(row) > 0:
                    d.append(row)
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
    w_dir, fl = H.getFiles()
    readFileList(fl)

if __name__ == '__main__':
    main()