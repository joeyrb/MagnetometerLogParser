'''
Report results from the data gathered while testing.

author: Joey Brown
'''
import Parser as prsr
import math

def getResults():
    pass

def getMin(vs):
    return min(vs)

def getMax(vs):
    pass

def getCenter(vs):
    pass

def getAmplitude(vs):
    pass

def Axis_To_Int(axis):
    a = axis.upper()
    if a == 'X':
        i = 0
    elif a == 'Y':
        i = 1
    elif a == 'Z':
        i = 2
    else:
        i = -1
    return i

def getValueByAxis(ds, axis):
    try:
        return ds[Axis_To_Int(axis)]
    except Expression as e:
        print(e)

def main():
    print(getMin(prsr.getValues()[0]))

if __name__ == '__main__':
    main()