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
        for aux_pos in range(0,10):
            if point_array[pos] not in points_to_remove:
                new_points.append([point_array[pos],point_array[pos]])
            else:
                if len(new_points)>0:
                    new_points.append([new_points[-1][0],point_array[pos]])
                else:
                    new_points.append([point_array[pos], point_array[pos]])

    aux_new_points = []
    for point in range(0,len(new_points)-1):
        grow = (new_points[point+1][0] - new_points[point][0])/10
        for aux2 in range(0,3):
            aux_new_points.append([new_points[point][0] + grow * aux2 ,new_points[point][0]])



    return aux_new_points,new_points_to_remove


def getSlope(x1,x2,y1,y2):
    slope = 0
    x = x1 - x2
    y = y1 - y2
    if x != 0 and y != 0:
        slope = y / x
    else:
        slope = 0
    return slope


main()