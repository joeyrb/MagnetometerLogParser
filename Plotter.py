'''
Plot the results from the test data log files.Exception

author: Joey Brown
'''
import matplotlib.pyplot as plt
import matplotlib
import Analyzer as anlyzr

simulated_xmas = [409.7,259.2,173.6,123,91.2]
simulated_t = [500,371,283,217,168]


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
    devkit_res = anlyzr.getResults()
    beacon_res = anlyzr.getResults()

    # for r in res[1]:
    #     print(r)
    #     print("\n\n")

    # print(plotAxisAmplitude(res,1))
    # print(plotAxisMin(res,1))
    plt.plot(plotAxisAmplitude(devkit_res,1), color='blue', marker='o')
    plt.plot(plotAxisAmplitude(beacon_res,1), color='red', marker='o')
    plt.plot(simulated_xmas, color='purple', marker='+')
    plt.legend(["DevKit", "Beacon","Simulation"])
    # y_amp = plotAxisAmplitude(res, 1)
    # print(y_amp)
    # plt.plot(y_amp)
    plt.show()

if __name__ == '__main__':
    main()