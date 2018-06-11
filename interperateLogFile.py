'''
Date: 5-7-2018
Author: Joey Brown
Description: Simple program that opens a .log file in an
    expected format, parses the contents into readable
    data, outputs the contents to the screen.

NOTE(S): * .log file must be in the same directory this program is executed from
'''
import os

VarNames = {'axav' : 0,
            'axmn' : 0,
            'axmx' : 0,
            'ayav' : 0,
            'aymn' : 0,
            'aymx' : 0,
            'azav' : 0,
            'azmn' : 0,
            'azmx' : 0,
            'gxav' : 0,
            'gxmn' : 0,
            'gxmx' : 0,
            'gyav' : 0,
            'gymn' : 0,
            'gymx' : 0,
            'gzav' : 0,
            'gzmn' : 0,
            'gzmx' : 0,
            'mxav' : 0,
            'mxmn' : 0,
            'mxmn' : 0,
            'mxmx' : 0,
            'myav' : 0,
            'mymn' : 0,
            'mymx' : 0,
            'mzav' : 0,
            'mzmn' : 0,
            'mzmx' : 0,
            'btmp' : 0,
            'bite' : 0,
            'bvol' : 0,
            'time' : 0,
            'imei' : 0}

# Open input .log file and return list containing only relevent data
def getDataSet(inputFile):
    dataList = []
    location = 'C:\Users\Altium\Desktop' 
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
    # dsDict = VarNames.copy()
    for d in ds:
        dsDict = VarNames.copy()
        for i in range(0,len(d)):
            s = d[i].split('=')
            dsDict[str(s[0])] = s[1]
            print(dsDict[s[0]])
        parsedDS.append(dsDict)
        # dsDict.clear()
    return parsedDS

# MAIN #
def main():
    fn = 'UwTerminalX.log'  # filename to read from

    ds = getDataSet(fn)     # dataset returned from the .log file
    pds = parseDataSet(ds)  # parse the dataset as a list of dictionaries
    print(pds)              # print parsed dataset

if __name__ == '__main__':
    main()