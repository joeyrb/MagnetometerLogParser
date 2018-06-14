'''
Parse data read from the files the test logs are stored in

author: Joey Brown
'''
import os
import csv
import Handler as hdlr
import Reader as rdr


def getValues():
    ds = rdr.getData()
    return parseDataSet(ds)
    
def parseDataSet(ds):
    # print(ds.items())
    parser = getParseType(ds)
    data = ds.values()
    print(data)
    parsed_data_set = parseData(parser, data)
    return parsed_data_set

def parseData(p, ds):
    parsed_data = []
    if p.upper() == "CSV":
        parsed_data = parseCSV(ds)
    elif p.upper() == "LOG":
        parsed_data = parseLOG(ds)
    else:
        print("Error parsing file")
        exit
    return parsed_data

def parseCSV(ds):
    parsedData = []
    for d in ds:
        if len(d) > 0:
            nums = []
            for i in range(0, len(d)):
                if d[i]:
                    try:
                        nums.append(float(d[i]))
                    except Exception as e:
                        pass
            parsedData.append(nums)
    return parsedData
                    
def parseLOG(ds):
    parsedData = []
    
    return parsedData

def getParseType(ds):
    if "LOG" in ds:
        return 'LOG'
    elif "CSV" in ds:
        return 'CSV'
    else:
        print("Error getting parse type.")
        exit

# 
# 
# 
#       MAIN
# 
# 
# 

def main():
    v = getValues()
    print(v)

if __name__ == '__main__':
    main()