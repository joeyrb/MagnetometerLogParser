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
    pass

# Prompt user for directory
def getFiles():
    w_dir = getDirFromUser()
    fl = getFileList(w_dir)
    return w_dir, fl

# Pass in directory and return a sorted list of files
def getFilesFrom(wDir = ""):
    if wDir == "":
        wDir = CWD
    return getFileList(wDir).sort()

# Return unsorted list of files from directory
def getFileList(wDir):
    file_list = []
    for f in os.listdir(wDir):
        file_list.append(f)
    return file_list

# Returns the file extention as string (CSV, LOG, TXT)
# return: fx = "file extention"
def getFileType(f):
    return str(f[-3:]).upper()

def getFileExtension(f):
    return str(f[-4:]).lower()

# Prompts user to select directory, returns pathname as string
def getCWD():
    return CWD

# Prompt user to select directory with data files.
def getDirFromUser():
    print("Which folder would you like to open?: ")
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory()

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






def main():
    pass

if __name__ == '__main__':
    main()