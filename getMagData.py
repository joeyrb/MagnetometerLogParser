import os
import math
import csv
import fileData as FD
import matplotlib.pyplot as plt

# beacon = [696,626.5,586,563.5,544.5,530.5,518,503.5,483.5]


simulated_straight = [394.6,289.1,222.4,177.2,144.9,120.9,102.5]
simulated_t = [500,422,371,324,283,247,217,191,168]
simulated_xmas = [409.7,324,259.2,210.5,173.6,145.1,123,105.4,91.2]


'''
These functions open log files and read the data
'''

def getFilename():
    return raw_input("Which log file would you like to open?: ")

def getFileData(f):
    fExt = f[-4:]
    try:
        if fExt == '.csv':
            return readCSVData(f)
        elif fExt == '.log':
            return readLogData(f)
        elif fExt == '.txt':
            return readTxtData(f)
        elif f == 'exit':
            print("\nstopping program...\n")
            exit
        else:
            print('\nFile type not recognized! (use "exit" to quit)\n')
            getFileData(getFilename())
    except Exception as e:
        print('\nError opening file!')
        print('The file ' + f + ' could not be opened...')
        print(e)

def readLogData(f):
    print('readLogData')

def readTxtData(f):
    print('readTxtData()')

def readCSVData(f):
    csvFile = open(f, "r")
    csvReader = csv.reader(csvFile)
    data = []
    for r in csvReader:
        if r:
            d = r
            if d:
                # data.append(d[-3:])
                data.append(d)
    
    # print(data)
    return data

# UNUSED?
def getAxisVals(axis, ds):
    if axis == 'x' or axis == 'X':
        return getVals(ds, 2)
    elif axis == 'y' or axis == 'Y':
        return getVals(ds, 3)
    elif axis == 'z' or axis == 'Z':
        return getVals(ds, 4)
    else:
        print("Error finding values for axis ", axis)
        exit

# Return axis values
def getVals(ds, axis):
    vals = []
    for d in ds:
        # print(d[-3:-2])
        try:
            data = d[axis]
            # data = float(d[-3:-2])
            vals.append(float(data))
            # vals.append(data)
        except Exception as e:
            print(e)
    return vals

'''
These functions operate on the dataset gathered from the functions above
'''

def findMin(ds):
    return min(ds)

def findMax(ds):
    return max(ds)

def findCenter(min, max):
    return (min + max) / 2

def findAmplitude(min, center):
    return math.fabs(min - center)

def findRatio(amp_curr, amp_prev):
    return (amp_curr / amp_prev)

def findYRatio(ds):
    res = []
    for i in range(0, len(ds)-1):
        try:
            if ds[i]:
                print(ds[i+1][getAxis('y')][3] , ds[i][getAxis('y')][3])
                res.append(ds[i+1][getAxis('y')][3] / ds[i][getAxis('y')][3])
        except Exception as e:
            print(e)
    return res

'''
These functions display results calculated from the dataset
'''

# Compile data gathered from an axis and return the min, max, center, and amplitude as a list
def formResultSet(axis_data):
    mn = findMin(axis_data)
    mx = findMax(axis_data)
    cent = findCenter(mn, mx)
    amp = findAmplitude(mn, cent)
    return [mn, mx, cent, amp]

def printResults(sets):
    print("\nRESULTS:\n-----------")
    for s in sets:
        print('\n')
        printSet(s)
        print('\n')

def printSet(s):
    for res in s:
        print(res)

def printCompiledSet(s):
    for c in s:
        print(c)

'''
These functions perform all of the above functions for an entire test with multiple log files
'''

# Calculate result sets for every log file in a directory
def compileLogList(log_list):
    test_distances = [] # each element is a file
    for fn in log_list:
        try:
            data_set = getFileData(fn)
            X = getAxisVals('x',data_set)
            Y = getAxisVals('y',data_set)
            Z = getAxisVals('z', data_set)
            f_name = fn.split('/')
            result = [
                f_name[-1:],
                formResultSet(getAxisVals('x',data_set)),
                formResultSet(getAxisVals('y',data_set)),
                formResultSet(getAxisVals('z',data_set))
            ]
            test_distances.append(result)
        except Exception as e:
            print(e)
            exit
    return test_distances

# Return the index of the axis
def getAxis(axis):
    axes = -1
    if axis.upper() == 'X':
        axes = 1
    elif axis.upper() == 'Y':
        axes = 2
    elif axis.upper() == 'Z':
        axes = 3
    else:
        print('Axis not recognized...')
        exit
    return axes

# return the X,Y,Z min values of a log file (single location)
def getMin(log_res):
    return getParams(log_res, 0)

# return the X,Y,Z MAX values of a log file (single location)
def getMax(log_res):
    return getParams(log_res, 1)

def getCenter(log_res):
    return getParams(log_res, 2)

def getAmplitude(log_res):
    return getParams(log_res, 3)

# Return a list of parameters to plot
def getParams(log_res, p_index):
    P = []
    for r in log_res:
        if type(r[p_index]) == float:
            P.append(r[p_index])
    return P

# Return parameter list based on axis
def getParamsByAxis(log_res, axis, p_index):
    # return getParams(log_res[getAxis(axis)])
    pass

def plotMin(log_res):
    plt.plot(getMin(log_res))
    plt.show()

def plotMax(log_res):
    pass

def plotCenter(log_res):
    pass

def plotAmplitude(log_res):
    pass

# Plot results based on parameter
def plotCompiledData(log_res, p_list):
    plt.plot(p_list)

def plotResultsByAxis(res, axis):
    params = getParamsByAxis(res, axis)
    plt.plot(params)

# Add line to the plot
# dataParam = column corresponding to min(0), max(1), center(2), amplitude(3)
def addPlotCurve(log_res, axis='', dataParam=3):
    plotData = []
    if axis != '':
        for i in range(0, len(log_res)):
            plotData.append(log_res[i][getAxis(axis)][dataParam])
    else:
        for j in range(0, len(log_res)):
            plotData.append(log_res[j])
    return plotData


'''
MAIN----------------------------------------------------------------------------------
'''

def main():
    
    devkit_filelist = FD.getLogFilenamesFrom(os.getcwd() + "/devkit_linetest/")

    # devkit_filelist = FD.getLogFilenamesFrom(os.getcwd() + "/devkit_xmas/")
    # devkit_filelist = FD.getLogFilenamesFrom(os.getcwd() + "/devkit_straight/")
    # devkit_filelist = FD.getLogFilenamesFrom(os.getcwd() + "/devkit_t/")



    compiled_data = compileLogList(devkit_filelist)
    # findYRatio(compiled_data)
    
    # # plt.plot(beacon,'g')

    plt.plot(addPlotCurve(compiled_data, 'Y', 3), 'b')
    plt.plot(addPlotCurve(simulated_xmas), "r")

    # plt.plot(findYRatio(compiled_data))
    # plt.plot(findYRatio(simulated_xmas))
    
    # plt.title('Y-Axis Amplitude Comparison')
    plt.show()



if __name__ == '__main__':
    main()