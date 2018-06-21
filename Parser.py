'''
Parse data read from the files the test logs are stored in

author: Joey Brown
'''
import os
import csv
import Handler as hdlr
import Reader as rdr

# Returned parsed data
def getValues():
    ds = rdr.getData()
    return parseDataSet(ds)

# Return parsed data from specified directory
def getValuesFrom(directory):
    ds = rdr.getDataFrom(directory)
    return parseDataSet(ds)
    
def parseDataSet(ds):
    # print(ds['LOG'])    # gets list of dictionaries. Keys = file names, values = file entries
    sets = ds[getParseType(ds)]
    if isLOG(ds):
        return scale(parseValueSet(sets), 1000)
    else:
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

def isLOG(ds):
    if getParseType(ds) == 'LOG':
        return True
    else:
        return False

def isCSV(ds):
    if getParseType(ds) == 'CSV':
        return True
    else:
        return False

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
    # Generate list of keys to access dictionary elements
    keychain = getKeychain(sets)
    # Create a set of values to be returned
    value_set = []
    # For every element of the dataset, access values with keys from keychain
    for d in sets:
        # Test every key in keychain until a key works, or move on to next d
        for i in range(0, len(keychain)):
            # Once a key match is found, extract values
            if keychain[i] in d:
                axis_values = []
                # Convert every item (axes) of every element from string to float
                for n in d[keychain[i]]:
                    # Only include expected data formats (e.g. exclude labels/text)
                    if len(n) > 0 and len(n) < 5:
                        try:
                            axis_values.append([float(x) for x in n if x != []])
                        except Exception as e:
                            pass
                value_set.append(axis_values)
    return value_set

# 
def scale(ds, scale_factor):
    scaledDS = []
    for ss in ds:
        scaledSS = []
        for e in ss:
            scaledE = []
            for i in range(0, len(e)):
                scaledE.append(e[i] * scale_factor)
            scaledSS.append(scaledE)
        scaledDS.append(scaledSS)
    return scaledDS
# 
# 
# 
#       MAIN
# 
# 
# 

def main():
    print(getValues())
    # ds = getValues()

    # print(scale(ds, 1000))

    # # Uncomment to view data set list
    # data_list = getValues()
    # for dl in data_list:
    #     print(dl)
    #     print("\n\n")

if __name__ == '__main__':
    main()