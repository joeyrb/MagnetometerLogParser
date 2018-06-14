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
    print(ds.items())
    p = list[ds.keys()]
    parser = p[0]
    # data = ds[1:]
    # print(data)
    parsed_data_set = parseData(parser[0], data)
    return parsed_data_set

def parseData(p, ds):
    parsed_data = []
    if p.upper() == "CSV":
        parsed_data = parseCSV(ds[0:])
    elif p.upper() == "LOG":
        parsed_data = parseLOG(ds[0:])
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
    for dss in ds:
        # print(d)
        for d in dss:
            s_nums = str(d[0]).split("\t")
            # print(s_nums)
            nums = []
            for n in s_nums:
                try:
                    nums.append(float(n))
                    parsedData.append(nums)
                except Exception as e:
                    pass
    return parsedData

def parseL(ds):
    pass

def main():
    v = getValues()
    print(v)

if __name__ == '__main__':
    main()