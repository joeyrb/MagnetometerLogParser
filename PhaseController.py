'''
    Controls the PHASE data for analysis, plotting, etc.
    Each configuration is arranged as follows:
        * beacon_s -> [x, y, z]
        * beacon_s[i] -> [2ft, 3ft, ..., 6ft]
        * beacon_s[i][j] -> len() = 150

    author: Joey Brown
'''
from bokeh.layouts import gridplot, row, column
from bokeh.plotting import figure, output_file, show

import Handler as hndlr
import Reader as rdr
import Parser as prsr
import Analyzer as anlyzr
import Plotter as plttr
import Defaults as dflts


CONFIGS = ['straight', 'tcross', 'triangle', 'xmas']    # General configuration name refs




'''
    Assemble PHASE datasets for processing
'''
# Return all phase data for all configurations measured with the beacon and devkit
def phaseData():
    return [beacon(), devkit()]



'''
    BEACON
'''
def beacon_all():
    beacon_s = anlyzr.getResults('Beacon', 'straight')  # beacon:straight-up
    beacon_T = anlyzr.getResults('Beacon', 'tcross')    # beacon:t-crossarm
    beacon_t = anlyzr.getResults('Beacon', 'triangle')  # beacon:triangle
    beacon_x = anlyzr.getResults('Beacon', 'xmas')      # beacon:xmas-tree
    return [beacon_s, beacon_T, beacon_t, beacon_x]
def beacon(config):
    if isinstance(config, str) == False:
        i = int(config)
        if i < 4 and i > -1:
            return beacon(CONFIGS[i])
        else:
            print("There was a problem with beacon(i)...")
            exit
    else:
        c = config.lower()
        if c == 'straight':
            return anlyzr.getResults('Beacon', 'straight', raw=True)  # beacon:straight-up
        elif c == 'tcross':
            return anlyzr.getResults('Beacon', 'tcross', raw=True)    # beacon:t-crossarm
        elif c == 'triangle':
            return anlyzr.getResults('Beacon', 'triangle', raw=True)  # beacon:triangle
        elif c == 'xmas':
            return anlyzr.getResults('Beacon', 'xmas', raw=True)      # beacon:xmas-tree
        else:
            print("There as a problem with beacon(config)...")
            exit



'''
    DEVKIT
'''
def devkit_all():
    devkit_s = anlyzr.getResults('DevKit', 'straight')  # devkit:straight-up
    devkit_T = anlyzr.getResults('DevKit', 'tcross')    # devkit:t-crossarm
    devkit_t = anlyzr.getResults('DevKit', 'triangle')  # devkit:triangle
    devkit_x = anlyzr.getResults('DevKit', 'xmas')      # devkit:xmas-tree
    return [devkit_s, devkit_T, devkit_t, devkit_x]
def devkit(config):
    if isinstance(config, str) == False:
        i = int(config)
        if i < 4 and i > -1:
            return devkit(CONFIGS[i])
        else:
            print("There was a problem with devkit(i)...")
            exit
    else:
        c = config.lower()
        if c == 'straight':
            return anlyzr.getResults('DevKit', 'straight', raw=True)  # devkit:straight-up
        elif c == 'tcross':
            return anlyzr.getResults('DevKit', 'tcross', raw=True)    # devkit:t-crossarm
        elif c == 'triangle':
            return anlyzr.getResults('DevKit', 'triangle', raw=True)  # devkit:triangle
        elif c == 'xmas':
            return anlyzr.getResults('DevKit', 'xmas', raw=True)      # devkit:xmas-tree
        else:
            print("There was a problem with devkit(config)...")
            exit



'''
    CONFIGURATION
    access individual configurations within the device datasets
'''
# Return all data from both devices of specified config
def getConfig(config):
    try:
        if isinstance(config, str):
            c = str(config)
        elif isinstance(config, int):
            c = int(config)
        return [beacon(c), devkit(c)]
    except Exception as e:
        print("There was a error with getConfig(config)...")
        print(e)
        exit


'''
    AXIS
    access individual axes of device datasets
'''
# Return the dataset associated with the input axis
def getAxis(ds, axis):
    a = axis.lower()
    i = -1
    if a == 'x':
        i = 0
    elif a == 'y':
        i = 1
    elif a == 'z':
        i = 2
    else:
        print("there was an error with getAxis()")
        exit
    return ds[i]
def getX(ds):
    return getAxis(ds, 'x')
def getY(ds):
    return getAxis(ds, 'y')
def getZ(ds):
    return getAxis(ds, 'z')


'''
    PLOT ASSEMBLY
    prepare figures to plot data
'''
def gen_xs(ds):
    xs = []
    for i in range(0, len(ds)):
        xs.append(i)
    return xs
def gen_ys(ds):
    pass
def gen_fig_line(X, Y, H, W, clr='navy'):
    f = figure(plot_height=H, plot_width=W, toolbar_location="below")
    return f.line(x=X, y=Y, color=clr)
# Generate a chart for each axis (x,y,z) for input config
def gen_config_row(device, config, H=500, W=500):
    C = getConfig(config)
    d = device.lower()
    if d == 'beacon':
        device_x,device_y,device_z,xs_Dx,xs_Dy,xs_Dz = gen_beacon_row(C)
    elif d == 'devkit':
        device_x,device_y,device_z,xs_Dx,xs_Dy,xs_Dz = gen_devkit_row(C)
    else:
        print("There was a problem with gen_config_row()...")
        exit

    x = figure(plot_height=H, plot_width=W, toolbar_location="below")
    y = figure(plot_height=H, plot_width=W, toolbar_location="below")
    z = figure(plot_height=H, plot_width=W, toolbar_location="below")

    x.line(x=xs_Dx, y=device_x[0], color="lime")
    y.line(x=xs_Dy, y=device_y[0], color="navy")
    z.line(x=xs_Dz, y=device_z[0], color="firebrick")

    return x, y, z

def gen_beacon_row(C):
    bcon_x = getX(C[0])
    bcon_y = getY(C[0])
    bcon_z = getZ(C[0])
    xs_Bx = gen_xs(bcon_x[0])
    xs_By = gen_xs(bcon_y[0])
    xs_Bz = gen_xs(bcon_z[0])
    return bcon_x,bcon_y,bcon_z,xs_Bx,xs_By,xs_Bz
def gen_devkit_row(C):
    dev_x = getX(C[1])
    dev_y = getY(C[1])
    dev_z = getZ(C[1])
    xs_Dx = gen_xs(dev_x[0])
    xs_Dy = gen_xs(dev_y[0])
    xs_Dz = gen_xs(dev_z[0])
    return dev_x,dev_y,dev_z,xs_Dx,xs_Dy,xs_Dz

'''
    MAIN
'''
def main():
    C = getConfig('straight')
    
    output_file("./HTML/TEST/straight_phase.html", title='Straight Phase')
    
    M = 450
    X, Y, Z = gen_config_row('beacon','straight', M, M)
    F = figure(plot_height=M, plot_width=M)
    device_x,device_y,device_z,xs_Dx,xs_Dy,xs_Dz = gen_beacon_row(C)
    
    # F.multi_line(xs=[xs_Dx,xs_Dy,xs_Dz], ys=[device_x[0], device_y[0], device_z[0]])
    
    # r1 = row([X,Y,Z])
    # r2 = row([F])
    # c1 = column([r1, r2])
    # show(c1)

    # show(row([X,Y,Z,F]))
    

if __name__ == '__main__':
    main()