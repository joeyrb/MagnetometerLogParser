'''
Calculate the simulation data for any configuration

author: Joey Brown
'''
# -----MODULE IMPORTS-------------------------------------------------------
import math
# ------------------------------------------------------------

# -----CONSTANTS-------------------------------------------------------------
mu = ( 4 * math.pi * 0.000001 ) #mu_0
I = 200 # amps
A = 2*math.pi # 2pi
C = 1000 # 1000 Gauss / T
# ------------------------------------------------------------

# Convert feet to meters
def ft_2_m(ft):
    return (ft * 12 * 2.54 / 100)

# Return the distance between the device and the current phase
def getR(h, w):
    return math.hypot(h,w)

# Return the degree of angle for the location of the current phase is from the measuring device
def getTheta(h, w):
    return math.atan2(w,h)

def getB(R):
    return ( ( mu * I ) / ( A * R ) ) * C

def getBx(B, h, w):
    return ( math.cos( getTheta( h, w ) ) * B )

def getBy(B, h, w):
    return ( math.sin( getTheta( h, w ) ) * B )




def genSimData(config, distances):
    c = config.upper()
    if c == 'STRAIGHT':
        return Straight(distances)
    elif c == 'TCROSS':
        return TCross(distances)
    elif c == 'TRIANGLE':
        return Triangle(distances)
    elif c == 'XMAS':
        return XMas(distances)
    else:
        print("ERROR: There was a problem generating simulation data.")
        exit

# d = height above sensor, w = width between center and phase
def Straight(distances):
    w = 0
    B1 = []
    B2 = []
    B3 = []
    Bx1 = []
    Bx2 = []
    Bx3 = []
    By1 = []
    By2 = []
    By3 = []
    for d in distances:
        d1 = d
        b1 = getB(getR(d1,w))
        B1.append(b1)
        Bx1.append(getBx(b1, d1, w))
        By1.append(getBy(b1, d1, w))

        d2 = d1+ft_2_m(2)
        b2 = getB(getR(d2, w))
        B2.append(b2)
        Bx2.append(getBx(b2, d2, w))
        By2.append(getBy(b2, d2, w))
        
        d3 = d2+ft_2_m(2)
        b3 = getB(getR(d3, w))
        B3.append(b3)
        Bx3.append(getBx(b3, d3, w))
        By3.append(getBy(b3, d3, w))
    
    return B1, Bx1, By1, B2, Bx2, By2, B3, Bx3, By3



def TCross(distances):
    w = [ft_2_m(3.66666666), 0, ft_2_m(3.66666666)]

def Triangle(distances):
    w = [ft_2_m(3.66666666), 0, ft_2_m(3.66666666)]

def XMas(distances):
    w = [ft_2_m(3.3), ft_2_m(3.3), 0]


def main():
    # Test for phase 1 on t-crossarm
    distances = [2, 3, 4, 5, 6]
    h = []
    for d in distances:
        h.append(ft_2_m(d))
    H = sorted(h)
    
    straight = genSimData('straight', H)
    for s in straight:
        print(sorted(s, reverse=True))
        print()
        print()

if __name__ == '__main__':
    main()