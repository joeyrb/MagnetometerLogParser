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
    # print(ds['LOG'])    # gets list of dictionaries. Keys = file names, values = file entries
    sets = ds[getParseType(ds)]
    return parseValueSet(sets)

def getValuesByAxis(vs, x=False, y=False, z=False):
    axis_values = []
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