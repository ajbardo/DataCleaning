import scipy as scipy
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import fft,fftfreq,rfft,rfftfreq,irfft

def main():
    error_range = 0.0009

    for pos in range(1,4):
        file = "DataSet_"+str(pos)+".csv"
        print("Starting:"+file)
        fileManager = open(file,"r")
        data = fileManager.read().replace(",",".")
        fileManager.close()
        valueArray = []
        for aux in data.split("\n")[1:-1]:
            valueArray.append(float(aux))
        result = cleanValues(valueArray,error_range)[0]
        PrintFile(result,"ResultSet_"+str(pos)+".csv")

        if pos == 1:
            fouResult = fourier(valueArray,error_range)
            result=appendData(result,fouResult)
            PrintFile(result, "ResultSet_" + str(pos) +"_E0.0009_Fourier_logical_original"+ ".csv")

def appendData(array1,array2):
    size = 0
    toReturn = []
    if len(array1) > len(array2):
        size = len(array1)
    else:
        size = len(array2)

    for pos in range(0,size):
        toAppend = []
        if pos < len(array1):
            for data in array1[pos]:
                toAppend.append(data)
        if pos < len(array2):
            for data in array2[pos]:
                toAppend.append(data)
        toReturn.append(toAppend)

    return toReturn

def fourierV2(valueArray,error):
    pass


def fourier(valueArray,error):
    SampleRate = 0
    Duration = 0
    yf = rfft(valueArray)
    hits = []
    for SampleRate in range(1,100):
        for Duration in range(1,100):
            N = SampleRate * Duration
            xf = rfftfreq(N, 1 / SampleRate)
            if xf.size == len(yf):
                hits.append((SampleRate,Duration))

    fouriers = []
    freqToClear= 0.5
    for hit in hits:
        N = hit[0] * hit[1]
        xf = rfftfreq(N, 1 / hit[0])
        points_per_freq = len(xf) / (hit[0] / 2)
        target_idx = int(points_per_freq * freqToClear)
        yf[target_idx:] = 0
        fouriers.append(irfft(yf))
        #plt.plot(irfft(yf))
        #plt.show()
    acumSlope = 0

    for pos in range(0, len(valueArray) - 1):
        acumSlope += valueArray[pos] - valueArray[pos + 1]

    medSlope = acumSlope / len(valueArray)
    medFou = []
    for pos1 in range(0, len(valueArray)):
        acum = 0
        med = 0
        for pos2 in range(0, len(fouriers)):
            acum += fouriers[pos2][pos1]
        med = acum / len(fouriers)
        medFou.append([med])
    return medFou

def PrintFile(data,file):
    to_print = "NewValue;OldValue\n"
    for aux1 in data:
        for aux2 in aux1:
            to_print += str(aux2)+";"
        to_print += "\n"
    f = open(file,"w")
    f.write(to_print.replace(".",","))
    f.close()

def cleanValues(point_array,error):
    acum_slope = 0

    for pos in range(0,len(point_array)-1):
        acum_slope += point_array[pos] - point_array[pos+1]

    med_slope = acum_slope/len(point_array)

    points_to_remove = []
    pos1 = 0

    for pos in range(0,len(point_array)-1):
        slope = (point_array[pos1] - point_array[pos1+1])
        if slope > med_slope + error or slope < med_slope - error:
            points_to_remove.append(point_array[pos1+1])
        pos1 += 1
    new_points = []
    new_points_to_remove = []

    for pos in range(0, len(point_array) - 2):
        if point_array[pos] not in points_to_remove:
            new_points.append([point_array[pos],point_array[pos]])
        else:
            if len(new_points)>0:
                new_points.append([new_points[-1][0],point_array[pos]])
            else:
                new_points.append([point_array[pos], point_array[pos]])
    return new_points,new_points_to_remove


def getSlope(x1,x2,y1,y2):
    slope = 0
    x = x1 - x2
    y = y1 - y2
    if x != 0 and y != 0:
        slope = y / x
    else:
        slope = 0
    return slope

if __name__ == '__main__':
    main()