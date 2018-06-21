'''
Plot the results from the test data log files.

author: Joey Brown
'''
from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show
import Analyzer as anlyzr
import Defaults as dflts

# Extract points from result data set (res) in a format that is compatible with bokeh plot module
def getPlotPoints(res, indx):
    pts = []
    for r in res:
        pts.append(r[indx])
    return pts

# Return the min of the results data as plot points
def plotMin(res):
    return getPlotPoints(res,0)

# Return the MAX of the results data as plot points
def plotMax(res):
    return getPlotPoints(res,1)

# Return the center of the results data as plot points
def plotCenter(res):
    return getPlotPoints(res, 2)

# Return the amplitude of the results data as plot points
def plotAmplitude(res):
    return getPlotPoints(res,3)

# ----------------------------------------
#           AXIS FUNCTIONS
# 
# Axis: x=0, y=1, z=2
# ----------------------------------------

# Plot the min data by specified axis
def plotAxisMin(res, axis):
    m = plotMin(res)
    return m[axis]

# Plot the MAX data by specified axis
def plotAxisMax(res, axis):
    M = plotMax(res)
    return M[axis]

# Plot the center data by specified axis
def plotAxisCenter(res,axis):
    c = plotCenter(res)
    return c[axis]

# Plot the amplitude data by specified axis
def plotAxisAmplitude(res, axis):
    a = plotAmplitude(res)
    return a[axis]

# PLOT BY X
def plotXmin(res):
    return plotAxisMin(res,0)
def plotXMAX(res):
    return plotAxisMax(res, 0)
def plotXCenter(res):
    return plotAxisCenter(res, 0)
def plotXAmplitude(res):
    return plotAxisAmplitude(res, 0)
# PLOT BY Y
def plotYmin(res):
    return plotAxisMin(res,1)
def plotYMAX(res):
    return plotAxisMax(res, 1)
def plotYCenter(res):
    return plotAxisCenter(res, 1)
def plotYAmplitude(res):
    return plotAxisAmplitude(res, 1)
# PLOT BY Z
def plotZmin(res):
    return plotAxisMin(res,2)
def plotZMAX(res):
    return plotAxisMax(res, 2)
def plotZCenter(res):
    return plotAxisCenter(res, 2)
def plotZAmplitude(res):
    return plotAxisAmplitude(res, 2)

# ----------------------------------------
#       PLOT GENERATION FUNCTIONS
# 
# ----------------------------------------

# Generate the x-axis lables for the plot of the distance dataset (dds).
def genDistXLabels(dds):
    xs = []
    for i in range(0, len(dds)+2):
        xs.append(i+2)
    return xs

# Generate the x-axis lables for the plot of the phase dataset (dds).
def genPhaseXLabels(pds):
    pass

# Generate a new figure to plot
def genFigure(ds, ttl=''):
    if ttl=='':
        p = figure(title=None, plot_width=500, plot_height=300)
    else:
        p = figure(title=ttl, plot_width=500, plot_height=300)
    return p

def genDistPlot(beacon, devkit, sim):
    bcn_xs = genDistXLabels(beacon)
    dev_xs = genDistXLabels(devkit)
    sim_xs = genDistXLabels(sim)
    
    bc_pts = plotYAmplitude(beacon)
    dk_pts = plotYAmplitude(devkit)

    bc_fig = genFigure(bc_pts, "Beacon")
    dk_fig = genFigure(dk_pts, "DevKit")
    sim_fig = genFigure(sim, "Simulated")
    
    bc_fig.line(bcn_xs, bc_pts, line_width = 2, color="lime", alpha = 0.5)
    dk_fig.line(dev_xs, dk_pts, line_width = 2, color="navy", alpha = 0.5)
    sim_fig.line(sim_xs, sim, line_width = 2, color="orange", alpha = 0.5)

    return gridplot([[bc_fig, dk_fig, sim_fig]])

def genPhasePlot(bcon, dev, sim, config_type):
    pass

def genConfigPlot(bcon, dev, sim, config_type):
    c = config_type.upper()
    if isStraight(c):
        return 
    elif isTCross(c):
        return
    elif isTriangle(c):
        return
    elif isXMas(c):
        return
    else:
        print("ERROR: there was a problem with the plot configuration.")
        exit

def genStraightPlot():
    beacon = anlyzr.getResultsFrom(dflts.getStraightDirs_Dist()[0])
    devkit = anlyzr.getResultsFrom(dflts.getStraightDirs_Dist()[1])
    sim = dflts.getSimulatedData('straight')
    return genDistPlot(beacon, devkit, sim)

def genTCrossPlot():
    beacon = anlyzr.getResultsFrom(dflts.getTCrossDirs_Dist()[0])
    devkit = anlyzr.getResultsFrom(dflts.getTCrossDirs_Dist()[1])
    sim = dflts.getSimulatedData('tcross')
    return genDistPlot(beacon, devkit, sim)

def genTrianglePlot():
    beacon = anlyzr.getResultsFrom(dflts.getTriangleDirs_Dist()[0])
    devkit = anlyzr.getResultsFrom(dflts.getTriangleDirs_Dist()[1])
    sim = dflts.getSimulatedData('triangle')
    return genDistPlot(beacon, devkit, sim)

def genXMasPlot():
    beacon = anlyzr.getResultsFrom(dflts.getXMasDirs_Dist()[0])
    devkit = anlyzr.getResultsFrom(dflts.getXMasDirs_Dist()[1])
    sim = dflts.getSimulatedData('xmas')
    return genDistPlot(beacon, devkit, sim)

def isConfigType(config, type_check):
    c = config.upper()
    if c == type_check:
        return True
    else:
        return False

def isStraightUp(c):
    return isConfigType(c, 'STRAIGHT')

def isTCross(c):
    return isConfigType(c, 'TCROSS')

def isTriangle(c):
    return isConfigType(c, 'TRIANGLE')

def isXMas(c):
    return isConfigType(c , 'XMAS')

# 
# 
# 
#       MAIN
# 
# 
# 

def main():
    # GET USER INPUT TO SELECT DIRECTORY
    # devkit_res = anlyzr.getResults()
    # beacon_res = anlyzr.getResults()

    output_file("./HTML/allconfigsdistances.html")

    
    # Generate and Display data results
    #   (uncomment sections below to run that configuration)

    # STRAIGHT UP
    # output_file("./HTML/straight.html")
    show(genStraightPlot())

    # TCROSS
    # output_file("./HTML/tcross.html")
    show(genTCrossPlot())

    # TRIANGLE
    # output_file("./HTML/triangle.html")
    show(genTrianglePlot())

    # XMAS
    # output_file("./HTML/xmas.html")
    show(genXMasPlot())


if __name__ == '__main__':
    main()