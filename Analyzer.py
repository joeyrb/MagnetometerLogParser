'''
Report results from the data gathered while testing.

author: Joey Brown
'''
import Parser as prsr
import math
import matplotlib.pyplot as plt
import matplotlib



def getResults():
    valset = prsr.getValues()
    print(prsr.getValuesByAxis(valset[0], x=True))
    # mins = []
    # for vals in valset:
    #     print(getMin(vals))

def getMin(vs):
    return min(vs)

def getMax(vs):
    return max(vs)

def getCenter(vs):
    return (getMin(vs) + getMax(vs)) / 2

def getAmplitude(vs):
    return math.fabs(getMin(vs) - getCenter(vs))


# 
# 
# 
#       MAIN
# 
# 
# 

def main():
    # print(prsr.getValues())

    values = prsr.getValues()
    for v in values:
        print(v)
        print("\n\n")
    

if __name__ == '__main__':
    main()