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
    # for d in ds['CSV']:
    #     print(d)
    #     print("\n\n")
    return parseDataSet(ds)
    
def parseDataSet(ds):
    # print(ds['LOG'])    # gets list of dictionaries. Keys = file names, values = file entries
    sets = ds[getParseType(ds)]

    # prints each file, with its data, seperately
    # for s in sets:
        # print(s)
        # print("\n\n")

    # # print(sets)
    # kc = getKeychain(sets)
    # vs = []
    # # for k in kc:
    # for s in sets:
    #     for k in kc:
    #         if k in s:
    #             # print(s[k])
    #             vs = (getValueList(s[k]))
    #             # print(getValueList(s[k]))
    #             # print("\n\n")
    # # print(vs)
    # print(parseValueSet(sets))

    # for i in range(0, len(kc)):
    #     # print(kc[i])
    #     k = kc[i]
    #     for s in sets:
    #         if k in s:
    #             try:
    #                 # print(float(s[k]))
    #                 j = 0
    #             except Exception as e:
    #                 pass
    # print(getKeychain(sets))

    # prints all data set keys (file names)
    # for val in ds.keys():
        ## print(val.keys())
        # print(val)

    # parser = getParseType(ds)
    # data = ds.values()
    # # print(data)
    # parsed_data_set = parseData(parser, data)
    # return parsed_data_set
    return parseValueSet(sets)

def getValuesByAxis(vs, x=False, y=False, z=False):
    axis_values = []
    print(len(vs))
    try:
        for v in vs:
            if x:
                axis_values.append(v[0])
            elif y:
                axis_values.append(v[1])
            elif z:
                axis_values.append(v[2])
            else:
                print("No axis value selected.")
                exit
    except Exception as e:
        pass
    return axis_values

def getXValues(vs):
    return getValuesByAxis(vs,x=True)

def getYValues(vs):
    return getValuesByAxis(vs,y=True)

def getZValues(vs):
    return getValuesByAxis(vs,z=True)

# def parseData(p, ds):
#     parsed_data = []
#     if p.upper() == "CSV":
#         # parsed_data = parseCSV(ds)
#         parsed_data.append(parseCSV(ds))
#     elif p.upper() == "LOG":
#         parsed_data = parseLOG(ds)
#     else:
#         print("Error parsing file")
#         exit
#     return parsed_data

# def parseCSV(ds):
#     parsedData = []
#     for d in ds:
#         if len(d) > 0:
#             nums = []
#             for i in range(0, len(d)):
#                 if d[i]:
#                     try:
#                         # nums.append(float(d[i]))
#                         nums = 
#                     except Exception as e:
#                         pass
#             parsedData.append(nums)
#     return parsedData
                    
# def parseLOG(ds):
#     parsedData = []
    
#     return parsedData

def getParseType(ds):
    if "LOG" in ds:
        return 'LOG'
    elif "CSV" in ds:
        return 'CSV'
    else:
        print("Error getting parse type.")
        exit

# Return list of keys within the data set (keys = file names)
def getKeychain(ds):
    keychain = []
    for k in ds:
        for v in k.keys():
            keychain.append(v)
        # keychain.append(k.keys())
    return keychain

def getValueList(vs):
    data_values = []
    for v in vs:
        data_values.append(v)
    return data_values

# def parseValueSet(vs):
#     vals = []
#     for v in vs:
#         nums = []
#         for i in range(0, len(v)):
#             try:
#                 if v[i] != '':
#                     nums.append(float(v[i]))
#             except Exception as e:
#                 pass
#         vals.append(nums)
#     return vals

def parseValueSet(sets):
    keychain = getKeychain(sets)
    data_list = []
    for d in sets:
        for i in range(0, len(keychain)):
            if keychain[i] in d:
                axis_values = []
                for n in d[keychain[i]]:
                    if len(n) > 0 and len(n) < 5:
                        try:
                            axis_values.append([float(x) for x in n if x != []])
                        except Exception as e:
                            pass
                data_list.append(axis_values)
    return data_list
    # cleanedVals = []
    # for i in range(0, len(keychain)):
    #     vals = []
    #     k = keychain[i]
    #     for s in sets:
    #         if k in s:
    #             for n in s[k]:
    #                 nums = []
    #                 for j in range(0, len(n)):
    #                     try:
    #                         # Ignore labels
    #                         if len(n[j]) > 0 and len(n[j]) < 5:
    #                             nums.append(float(n[j]))
    #                         else:
    #                             nums.append(float(n[j]))
    #                     except Exception as e:
    #                         pass
    #                 vals.append(nums)
    # cleanedVals.append([v for v in vals if v !=[]])
    # return cleanedVals
# 
# 
# 
#       MAIN
# 
# 
# 

def main():
    print(getValues())

    # # Uncomment to view data set list
    # data_list = getValues()
    # for dl in data_list:
    #     print(dl)
    #     print("\n\n")

if __name__ == '__main__':
    main()