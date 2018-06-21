'''
Plot the results from the test data log files.

author: Joey Brown
'''
from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show
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
    devkit_res = anlyzr.getResults()
    beacon_res = anlyzr.getResults()

    xAxis = [2,3,4,5,6]


    output_file("log_lines.html")

    s1 = figure(width = 250, plot_height = 250, title=None)
    s1.circle(beacon_res, xAxis, size=10, color="navy", alpha=0.5)

    s2 = figure(width=250, height=250, x_range=s1.x_range, y_range=s1.y_range, title=None)
    s2.triangle(devkit_res, xAxis, size=10, color="firebrick", alpha=0.5)

    s3 = figure(width=250, height=250, x_range=s1.x_range, y_range=s1.y_range, title=None)
    s3.square(simulated_straight, xAxis, size=10, color="olive", alpha=0.5)

    # Put subplots in a grid plot
    p = gridplot([[s1, s2, s3]])


    # Display Plot
    show(p)



if __name__ == '__main__':
    main()