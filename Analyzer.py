'''
Report results from the data gathered while testing.

author: Joey Brown
'''
import Parser as prsr
import math
import matplotlib.pyplot as plt
import matplotlib


# Return results from data as min, max, center, amplitude for x, y, and z
def getResults():
    values = prsr.getValues()
    
    x_vals = []
    y_vals = []
    z_vals = []

    for v in values:
        x_vals.append(prsr.getXValues(v))
        y_vals.append(prsr.getYValues(v))
        z_vals.append(prsr.getZValues(v))
    return getXResults(x_vals), getYResults(y_vals), getZResults(z_vals)

def getMin(vs):
    return min(vs)

def getMax(vs):
    return max(vs)

def getCenter(vs):
    return (getMin(vs) + getMax(vs)) / 2


def getAmplitude(vs):
    return math.fabs(getMin(vs) - getCenter(vs))

def getXResults(vs):
    xmin = []
    xmax = []
    xcenter = []
    xamplitude = []
    for v in vs:
        xmin.append(getMin(v))
        xmax.append(getMax(v))
        xcenter.append(getCenter(v))
        xamplitude.append(getAmplitude(v))
    return [xmin, xmax, xcenter, xamplitude]

def getYResults(vs):
    ymin = []
    ymax = []
    ycenter = []
    yamplitude = []
    for v in vs:
        ymin.append(getMin(v))
        ymax.append(getMax(v))
        ycenter.append(getCenter(v))
        yamplitude.append(getAmplitude(v))
    return [ymin, ymax, ycenter, yamplitude]

def getZResults(vs):
    zmin = []
    zmax = []
    zcenter = []
    zamplitude = []
    for v in vs:
        zmin.append(getMin(v))
        zmax.append(getMax(v))
        zcenter.append(getCenter(v))
        zamplitude.append(getAmplitude(v))
    return [zmin, zmax, zcenter, zamplitude]

# 
# 
# 
#       MAIN
# 
# 
# 

def main():
    print(getResults())

if __name__ == '__main__':
    main()