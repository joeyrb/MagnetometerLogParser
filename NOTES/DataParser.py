'''
Parse data read from the files the test logs are stored in

author: Joey Brown
'''
import os
import csv

# ---------- PARSERS ----------
def parseCSV(data):
    parsedData = []
    for d in data:
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
                    
def parseLOG(data):
    parsedData = []
    for d in data:
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

def parseTXT(data):
    pass

