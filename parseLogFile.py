'''
Date: 5-7-2018
Author: Joey Brown
Description: Simple program that opens a .log file in an
    expected format, parses the contents into readable
    data, outputs the contents to the screen.

NOTE(S): * .log file must be in the same directory this program is executed from
'''
import os
from logFileVarNames import getVarNames
VarNames = getVarNames()
fn = 'UwTerminalX.log'  # filename to read from


# Open input .log file and return list containing only relevent data
def getDataSet(inputFile):
    dataList = []
    # location = 'C:\Users\Altium\Desktop\SMRTGrid Beacon Tests\SMRTGrid Python Log Parser' 
    location = 'C:\Users\joey\Desktop\SMRTGrid Python Log Parser'
    for filename in os.listdir(location):
        if filename == 'UwTerminalX.log':
            f = open(os.path.join(location, 'UwTerminalX.log'), "r")
            for s in f:
                if len(s.split()) > 30:
                    try:
                        a = s.split()
                        dataList.append(a)
                    except Exception as e:
                        print(e)
    return dataList

# Parse the data set that was read from the .log file, return as list of dicts
def parseDataSet(ds):
    parsedDS = []
    for d in ds:
        dsDict = VarNames.copy()
        for i in range(0,len(d)):
            s = d[i].split('=')
            dsDict[str(s[0])] = s[1]
        parsedDS.append(dsDict)
    return parsedDS

# return list of parameters (e.g. all 'axav' of a data set)
# input: list of dictionaries
# output: list of all values that match the key = parameter
def getParams(parameter):
    ds = parseDataSet(getDataSet(fn))
    paramList = []
    for d in ds:
        try:
            paramList.append(d[parameter])
        except Exception as e:
            print(e)
            exit
    return paramList

# returns list of parameter values from the input data set 
def getParamsFromDataSet(parameter, ds):
    pList = []
    for d in ds:
        try:
            pList.append(d[parameter])
        except Exception as e:
            print(e)
            exit
    return pList



# MAIN #
def main():
    # fn = 'UwTerminalX.log'  # filename to read from

    ds = getDataSet(fn)     # dataset returned from the .log file
    pds = parseDataSet(ds)  # parse the dataset as a list of dictionaries
    print(pds)              # print parsed dataset
    # print(getParameters('gyav'))
    print(getParamsFromDataSet('gyav',pds))

if __name__ == '__main__':
    main()