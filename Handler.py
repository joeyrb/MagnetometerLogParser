'''
Handle the file operations required to analyze data stored in log files in .LOG or .CSV file formats.

author: Joey Brown
'''
import os
import csv
import tkinter as tk
from tkinter import filedialog
import Reader as rdr
import Parser as DP

CWD = os.getcwd()

'''
These functions open log files and read the data
'''

def handleFiles():
    return getFiles()

# Prompt user for directory
def getFiles():
    w_dir = getDirFromUser()
    fl = getFilesFrom(w_dir)
    return fl

# Pass in directory and return a sorted list of files
def getFilesFrom(wDir):
    fl = getFileList(wDir)
    fl.sort()
    return fl

# Prompts user to select directory, returns pathname as string
def getCWD():
    return CWD

# Prompt user to select directory with data files.
def getDirFromUser():
    print("Which folder would you like to open?: ")
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory()

# Returns the file path (fp) of a file
def getFilePath(wDir, fn):
    return wDir + "/" + fn

# Return unsorted list of files from directory
def getFileList(wDir):
    file_list = []
    for fn in os.listdir(wDir):
        fp = getFilePath(wDir, fn)
        file_list.append(getFilePath(wDir, fn))
    return file_list

# Returns path name from a file path string
def getPathName(fp):
    file_path = fp.split(sep="/")
    s = '/'
    return s.join(file_path[:len(file_path)-2]) + "/"

# Returns file name from a file path string
def getFileName(fp):
    file_path = fp.split(sep="/")
    return file_path[-1]

# Returns the file extention as string (CSV, LOG, TXT)
# return: fx = "file extention"
def getFileType(f):
    return str(f[-3:]).upper()

def getFileExtension(f):
    return str(f[-4:]).lower()

# Returns TRUE if file type is acceptable
def isType(f):
    ft = getFileType(f)
    if ft == "CSV" or ft == "LOG":
        return True
    else:
        return False

# Returns TRUE if file extension is acceptable
def isExtn(f):
    fx = getFileExtension(f)
    if fx == ".csv" or fx == ".log":
        return True
    else:
        return False

def isCSV(f):
    return isDataFile(f, "csv")

def isLOG(f):
    return isDataFile(f, "log")

def isDataFile(f, f_type):
    ft = str(f_type).upper()
    fx = "." + str(f_type).lower()
    if isType(f) and isExtn(f):
        if getFileType(f) == ft or getFileExtension(f) == fx:
            return True
        else:
            return False
    else:
        return False

# 
# 
# 
#       MAIN
# 
# 
# 

def main():
    print(handleFiles())

if __name__ == '__main__':
    main()