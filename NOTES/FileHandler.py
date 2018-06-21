'''
Handle the file operations required to analyze data stored in log files in .LOG or .CSV file formats.

author: Joey Brown
'''
import os
import csv
import tkinter as tk
from tkinter import filedialog
import FileReader as FR
import DataParser as DP


'''
These functions open log files and read the data
'''
# Prompts user to select file, returns filepath as string
def getFilePath():
    print("Which file would you like to open?: ")
    root = tk.Tk()
    root.withdraw()
    return str(filedialog.askopenfilename())

# Prompts user to select directory, returns pathname as string
def getDirectory():
    print("Which folder would you like to open?: \n")
    root = tk.Tk()
    root.withdraw()
    return str(filedialog.askdirectory())

def getFileData(f):
    fExt = f[-4:]
    try:
        if fExt == '.csv':
            return readCSVData(f)
        elif fExt == '.log':
            return readLogData(f)
        elif fExt == '.txt':
            return readTxtData(f)
        elif f == 'exit':
            print("\nstopping program...\n")
            exit
        else:
            print('\nFile type not recognized! (use "exit" to quit)\n')
            getFileData(getFilename())
    except Exception as e:
        print('\nError opening file!')
        print('The file ' + str(f) + ' could not be opened...')
        print(e)

def readLogData(f):
    print('readLogData')

def readTxtData(f):
    print('readTxtData()')

def readCSVData(f):
    csvFile = open(f, "r")
    csvReader = csv.reader(csvFile)
    data = []
    for r in csvReader:
        if r:
            d = r
            if d:
                # data.append(d[-3:])
                data.append(d)
    
    # print(data)
    return data

def main():
    # ft = FR.readCSV(getFilePath())
    d = FR.readLOG(getFilePath())
    

if __name__ == '__main__':
    main()