'''
Read the contents of a file and return the formatted information.

author: Joey Brown
'''

import os
import csv
import DataParser as DP

# Reads the contents of a file (f) from a filepath (fp). 
# Returns list of lines in f as string.
def readFile(fp):
    try:
        f = open(fp, "r", encoding="ISO-8859-1")
        next(f) # skip headings
        d = []
        csvReader = csv.reader(f)
        for l in csvReader:
            d.append(l)
        f.close()
        print(DP.parseCSV(d))
        return d
    except Exception as e:
        print(e)

# Opens a .CSV file and returns the contents as a string list.
# Each list element is a line.
def readCSV(fp):
    try:
        return readFile(fp)
    except Exception as e:
        print("There was an error with the CSV file: \n" + str(e))

# Opens a .LOG file and returns the contents as a string list.
# Each list element is a line.
def readLOG(fp):
    try:
        # return readFile(fp)
        d = []
        with open(fp, 'r', encoding="ISO-8859-1") as f:
            next(f) # skip headings
            fReadr = csv.reader(f)
            for row in fReadr:
                if len(row) > 0:
                    d.append(row)
        f.close()
        DP.parseLOG(d)
        return d
    except Exception as e:
        print("There was an error with the LOG file: \n" + str(e))

# Opens a .TXT file and returns the contents as a string list.
# Each list element is a line.
def readTXT(fp):
    try:
        return readFile(fp)
    except Exception as e:
        print("There was an error with the TXT file: \n" + str(e))

# Returns the file extention as string (CSV, LOG, TXT)
def getFileType(fp):
    return str(fp[-3:]).upper()
    

def main():
    pass

if __name__ == '__main__':
    main()