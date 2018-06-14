'''
Parse data read from the files the test logs are stored in

author: Joey Brown
'''
import os
import csv
import Reader as rdr


def getValues():
    ds = rdr.getData()
    return ds
    


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
    for d in ds:
        if len(d) > 0:
            s_nums = str(d[0]).split("\t")
            nums = []
            for n in s_nums:
                try:
                    nums.append(float(n))
                except Expression as e:
                    pass
            parsedData.append(nums)
    return parsedData


def main():
    v = getValues()
    print(v)

if __name__ == '__main__':
    main()