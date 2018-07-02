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
def genDistXLabels(dds, offset=2):
    xs = []
    for i in range(0, len(dds)+offset):
        xs.append(i+2)
    return xs
# Generate the x-axis lables for the plot of the phase dataset (pds).
def genPhaseXLabels(pds):
    pass

# Generate a new figure to plot
def genFigure(ds, ttl=''):
    if ttl=='':
        p = figure(title=None, plot_width=500, plot_height=300)
    else:
        p = figure(title=ttl, plot_width=500, plot_height=300)
    return p
# Generate a distance plot from datasets
def genDistPlot(beacon, devkit, sim):
    bcn_xs = genDistXLabels(beacon)
    dev_xs = genDistXLabels(devkit)
    sim_xs = genDistXLabels(sim,0)
    
    bc_pts = plotYAmplitude(beacon)
    dk_pts = plotYAmplitude(devkit)

    bc_fig = genFigure(bc_pts, "Beacon")
    dk_fig = genFigure(dk_pts, "DevKit")
    sim_fig = genFigure(sim, "Simulated")
    
    bc_fig.line(bcn_xs, bc_pts, line_width = 2, color="lime", alpha = 0.5)
    dk_fig.line(dev_xs, dk_pts, line_width = 2, color="navy", alpha = 0.5)
    sim_fig.line(sim_xs, sim, line_width = 2, color="orange", alpha = 0.5)

    return gridplot([[bc_fig, dk_fig, sim_fig]])
# Generate a phase outage plot from datasets
def genPhasePlot(bcon, dev, sim, config_type):
    pass
# Generate plot based on specified configuration
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

def genMultiLine(bcon, dev, sim):
    p = figure(plot_width=500, plot_height=500)
    xs = [genDistXLabels(bcon), genDistXLabels(dev), genDistXLabels(sim)]
    ys = [bcon, dev, sim]
    res_colors = ["lime", "navy", "red"]
    return p.multi_line(xs, ys, color=res_colors)

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

''' 
Create a single plot with multiple lines.
INPUT:
  *Each element of min, max, center, & amplitude 
      contains values for x, y, & z as [x, y, z]
  beacon = [[min], [max], [center], [amplitude]]
  devkit = [[min], [max], [center], [amplitude]]
  sim    = [[y-amplitude]]
  axis   = (0 | 1 | 2)    // x=0, y=1, z=2
  config = ('straight' | 'tcross' | 'triangle' | 'xmas')
OUTPUT:
  [p.line(beacon), p.line(devkit). p.line(sim)]
DESCRIPTION:
  return a list of line curves as figures for 
  the beacon, devkit, and simulation data. The
  returned result can be used by show() to 
  plot all three curves on a single plot. 
'''
def genSingleDistPlot(axis, config, title):
    # prepare title if requested
    if title=='' or title==None:
        t = None
    else:
        t = title
    # prepare y_range if requested
    yR=900
    
    # create analyzed data sets from file logs by searching by directory (y values)
    # beacon = anlyzr.getResultsFrom(dflts.getStraightDirs_Dist('beacon'))
    # devkit = anlyzr.getResultsFrom(dflts.getStraightDirs_Dist('devkit'))
    beacon = anlyzr.getResultsFrom(dflts.getDistDirs(config, 'beacon'))
    devkit = anlyzr.getResultsFrom(dflts.getDistDirs(config, 'devkit'))
    sim = dflts.getSimulatedData(config)  # simulated data is hard coded; no directory

    # generate x-axis labels for the plot intervals (x values)
    xs_bcon = genDistXLabels(beacon)
    xs_dev = genDistXLabels(devkit)
    xs_sim = genDistXLabels(sim, 0)

    # create list of lists with y values (ys) and x values (xs)
    ys = [plotAxisAmplitude(beacon,axis), plotAxisAmplitude(devkit,axis), sim]
    xs = [xs_bcon, xs_dev, xs_sim]

    # define settings for the single plot that will contain the 3 curves
    p=figure(
        plot_height=500, 
        plot_width=500,
        title=t,
        x_axis_label="Distance (feet)", 
        y_axis_label="EM Intensity (mGauss)")

    # define settings of plot with respect to the figures it contains (beacon, devkit, sim)
    legends = ["Beacon", "DevKit", "Simulation"]
    colors = ["lime", "navy", "firebrick"]
    
    # generate a line figure for each data set and add it to the plot
    for i in range(0, 3):
        p.line(xs[i], ys[i], color=colors[i], legend=legends[i])
    
    # return final generated plot that contains 3 curves (with legend)
    return p
        
# Generate a full page of all test configs
def genAllConfigsPlot():
    str8X = genSingleDistPlot(0,'Straight',"Straight Up (X-axis)")
    str8Y = genSingleDistPlot(1,'Straight',"Straight Up (Y-axis)")
    str8Z = genSingleDistPlot(2,'Straight',"Straight Up (Z-axis)")
    str8=[str8X,str8Y,str8Z]

    tcrossX = genSingleDistPlot(0,'tcross',"T-Crossarm (X-axis)")
    tcrossY = genSingleDistPlot(1,'tcross',"T-Crossarm (Y-axis)")
    tcrossZ = genSingleDistPlot(2,'tcross',"T-Crossarm (Z-axis)")
    T = [tcrossX,tcrossY,tcrossZ]

    triX = genSingleDistPlot(0,'triangle',"Triangle (X-axis)")
    triY = genSingleDistPlot(1,'triangle',"Triangle (Y-axis)")
    triZ = genSingleDistPlot(2,'triangle',"Triangle (Z-axis)")
    tri = [triX,triY,triZ]
    
    xmasX = genSingleDistPlot(0,'xmas',"XMas (X-axis)")
    xmasY = genSingleDistPlot(1,'xmas',"XMas (Y-axis)")
    xmasZ = genSingleDistPlot(2,'xmas',"XMas (Z-axis)")
    xmas = [xmasX,xmasY,xmasZ]

    return [str8, T, tri, xmas]

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

    # output_file("./HTML/allconfigsdistances.html")

    
    # Generate and Display data results
    #   (uncomment sections below to run that configuration)

    # STRAIGHT UP
    # output_file("./HTML/straight.html", title="Straight Up")
    # output_file("./HTML/straight_singleaxis.html", title="Straight Up")
    # show(genStraightPlot())
    # show(genSingleDistPlot(2, 'straight', "Straight Up (Z)"))

    # TCROSS
    # output_file("./HTML/tcross_singleaxis.html", title="T-Crossarm")
    # show(genTCrossPlot())
    # show(genSingleDistPlot(2, 'tcross', "T-Crossarm (X)"))

    # TRIANGLE
    # output_file("./HTML/triangle.html", title="Triangle")
    # show(genTrianglePlot())

    # XMAS
    # output_file("./HTML/xmas.html", title="X-Mas Tree")
    # show(genXMasPlot())



    # ALL CONFIGS PLOT
    output_file( "./HTML/singleplot_allaxes_allconfigs.html", title="All Configs" )
    show( gridplot(genAllConfigsPlot(), sizing_mode="fixed" ) )


if __name__ == '__main__':
    main()