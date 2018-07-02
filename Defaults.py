'''
This file contains all of the default directories to make compiling the data quicker and easier.
The directories used in this file are the most recent data logs. The original (unchanged) 
data logs can also be found within the Testing directory.

author: Joey Brown
'''
# -----MODULE IMPORTS-------------------------------------------------------
import os
from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show
import Analyzer as anlyzr
# ------------------------------------------------------------


# -----DEFAULT DIR-------------------------------------------------------
# Default directory = current working directory (CWD)
CWD = os.getcwd()
# ------------------------------------------------------------


# -----SIMULATION DATA-------------------------------------------------------
# Simulated data results (taken from excel sheets by Brian Hemmelman)
# 9 POINTS
# sim_straight = [394.6,222.4,144.9,120.9,102.5]
# sim_tcross = [500,422,371,324,283,247,217,191,168]
# sim_triangle = [0, 0, 0, 0, 0, 0, 0, 0]
# sim_xmas = [409.7,324,259.2,210.5,173.6,145.1,123,105.4,91.2]
# 5 POINTS
sim_straight = [394.6, 222.4, 144.9, 120.9, 102.5]
sim_tcross = [500, 371, 283, 217, 168]
sim_triangle = [0, 0, 0, 0, 0]
sim_xmas = [409.7, 259.2, 173.6, 123, 91.2]

SIMULATED_DATA = [sim_straight, sim_tcross, sim_triangle, sim_xmas]
# ------------------------------------------------------------


# -----CONFIG DIRS-------------------------------------------------------
# Default utility pole configuration directory names
straight = "straight/"
tcross = "tcross/"
triangle = "triangle/"
xmas = "xmas/"
# ------------------------------------------------------------


# -----DEVICE DIRS-------------------------------------------------------
# Default beacon and devkit directories for distance and phase data
dev_dir = str(CWD) + "/DevKit/"
dev_dir_dist = dev_dir + "DISTANCE/"
dev_dir_phase = dev_dir + "PHASE/"
bcon_dir = str(CWD) + "/Beacon/"
bcon_dir_dist = bcon_dir + "DISTANCE/"
bcon_dir_phase = bcon_dir + "PHASE/"
# ------------------------------------------------------------


# -----DISTANCE-------------------------------------------------------
# DEFAULT DEVKIT directories for distance data
dev_straight = dev_dir_dist + "straight/"
dev_tcross = dev_dir_dist + "tcross/"
dev_triangle = dev_dir_dist + "triangle/"
dev_xmas = dev_dir_dist + "xmas/"
DEVKIT_DIST_DIRS = [dev_straight, dev_tcross, dev_triangle, dev_xmas]

# DEFAULT SMRTGrid BEACON directories for distance data
bcon_straight = bcon_dir_dist + "straight/"
bcon_tcross = bcon_dir_dist + "tcross/"
bcon_triangle = bcon_dir_dist + "triangle/"
bcon_xmas = bcon_dir_dist + "xmas/"
BEACON_DIST_DIRS = [bcon_straight, bcon_tcross, bcon_triangle, bcon_xmas]

# List of default directories for distance data
DIST_DIRS = [BEACON_DIST_DIRS, DEVKIT_DIST_DIRS]
# ------------------------------------------------------------


# -----PHASE-------------------------------------------------------
# DEFAULT DEVKIT directories for phase data
devPhase_straight = dev_dir_phase + straight
devPhase_tcross = dev_dir_phase + tcross
devPhase_triangle = dev_dir_phase + triangle
devPhase_xmas = dev_dir_phase + xmas
DEVKIT_PHASE_DIRS = [devPhase_straight, devPhase_tcross, devPhase_triangle, devPhase_xmas]

# DEFAULT SMRTGrid BEACON directories for phase data
bconPhase_straight = bcon_dir_phase + straight
bconPhase_tcross = bcon_dir_phase + tcross
bconPhase_triangle = bcon_dir_phase + triangle
bconPhase_xmas = bcon_dir_phase + xmas
BEACON_PHASE_DIRS = [bconPhase_straight, bconPhase_tcross, bconPhase_triangle, bconPhase_xmas]

# List of default directories for distance data
PHASE_DIRS = [BEACON_PHASE_DIRS, DEVKIT_PHASE_DIRS]
# ------------------------------------------------------------








# -----ACCESSORS-----------------------------------------------------
# Return list of all test directories
def getTestDirs():
    return [getDistanceTestData(), getPhaseTestData()]

# Return all beacon and devkit distance directories
def getDistTestDirs():
    return DIST_DIRS
# Return all beacon and devkit phase directories
def getPhaseTestDirs():
    return PHASE_DIRS

# Return all beacon test directories
def getBeaconDirs():
    return [getBeaconDistDirs, getBeaconPhaseDirs]
# Return all beacon distance directories
def getBeaconDistDirs():
    return BEACON_DIST_DIRS
# Return all beacon phase test directories
def getBeaconPhaseDirs():
    return BEACON_PHASE_DIRS

# Return all beacon test directories
def getDevKitDirs():
    return [getDevKitDistDirs, getDevKitPhaseDirs]
# Return all beacon distance directories
def getDevKitDistDirs():
    return DEVKIT_DIST_DIRS
# Return all beacon phase test directories
def getDevKitPhaseDirs():
    return DEVKIT_PHASE_DIRS

# Return directory listing for both devices by configuration
# DISTANCE
def getStraightDirs_Dist(device = ''):
    D = device.upper()
    if D == '':
        return [BEACON_DIST_DIRS[0], DEVKIT_DIST_DIRS[0]]
    elif D == 'BEACON':
        return BEACON_DIST_DIRS[0]
    elif D == 'DEVKIT':
        return DEVKIT_DIST_DIRS[0]
    else:
        print("ERROR: There was a problem retrieving straight up configuration directories")
        exit
def getTCrossDirs_Dist():
    return [BEACON_DIST_DIRS[1], DEVKIT_DIST_DIRS[1]]
def getTriangleDirs_Dist():
    return [BEACON_DIST_DIRS[2], DEVKIT_DIST_DIRS[2]]
def getXMasDirs_Dist():
    return [BEACON_DIST_DIRS[3], DEVKIT_DIST_DIRS[3]]
# PHASE
def getStraightDirs_Phase():
    i = 0 
    return [BEACON_PHASE_DIRS[i], DEVKIT_PHASE_DIRS[i]]
def getTCrossDirs_Phase():
    i = 1
    return [BEACON_PHASE_DIRS[i], DEVKIT_PHASE_DIRS[i]]
def getTriangleDirs_Phase():
    i = 2
    return [BEACON_PHASE_DIRS[i], DEVKIT_PHASE_DIRS[i]]
def getXmasDirs_Phase():
    i = 3
    return [BEACON_PHASE_DIRS[i], DEVKIT_PHASE_DIRS[i]]
# SIMULATED
def getSimulatedData():
    return SIMULATED_DATA
def getSimulatedData(config):
    c = config.upper()
    i = -1
    if c == 'STRAIGHT':
        i = 0
    elif c == 'TCROSS':
        i = 1
    elif c == 'TRIANGLE':
        i = 2
    elif c == 'XMAS':
        i = 3
    else:
        print('ERROR: There was a problem trying to return simulated data...')
        exit
    return sorted(SIMULATED_DATA[i], reverse=True)
# ------------------------------------------------------------



def main():
    pass

if __name__ == '__main__':
    main()