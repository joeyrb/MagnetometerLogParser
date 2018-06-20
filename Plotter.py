'''
Plot the results from the test data log files.

author: Joey Brown
'''
import matplotlib.pyplot as plt
import matplotlib
# Fix the problem with the program freezing after exit the plot window
matplotlib.rcParams['backend'] = "qt4agg"
matplotlib.rcParams['backend.qt4'] = "PySide"
import Analyzer as anlyzr

simulated_straight = [394.6,289.1,222.4,177.2,144.9,120.9,102.5]
simulated_t = [500,422,371,324,283,247,217,191,168]
simulated_xmas = [409.7,324,259.2,210.5,173.6,145.1,123,105.4,91.2]


def getPlotPoints(res, indx):
    pts = []
    for r in res:
        pts.append(r[indx])
    return pts

def plotMin(res):
    return getPlotPoints(res,0)

def plotMax(res):
    return getPlotPoints(res,1)

def plotCenter(res):
    return getPlotPoints(res, 2)

def plotAmplitude(res):
    return getPlotPoints(res,3)

# Axis: x=0, y=1, z=2
def plotAxisMin(res, axis):
    m = plotMin(res)
    return m[axis]

def plotAxisMax(res, axis):
    M = plotMax(res)
    return M[axis]

def plotAxisCenter(res,axis):
    c = plotCenter(res)
    return c[axis]

def plotAxisAmplitude(res, axis):
    a = plotAmplitude(res)
    return a[axis]
# 
# 
# 
#       MAIN
# 
# 
# 

def main():
    # devkit_res = anlyzr.getResults()
    beacon_res = anlyzr.getResults()

    
    # plt.plot(plotAxisAmplitude(devkit_res,2), color='blue', marker='o')
    plt.plot(plotAxisAmplitude(beacon_res,2), color='red', marker='o')
    # plt.plot(simulated_straight, color='purple', marker='+')
    # plt.legend(["DevKit", "Beacon","Simulation"])
    plt.show()
    
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.plot(plotAxisAmplitude(beacon_res,2), color='blue', marker='o')
    # fig.show()


if __name__ == '__main__':
    main()