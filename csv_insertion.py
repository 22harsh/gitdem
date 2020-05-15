import csv
import random
from os import path
import json
from aggregation import aggregationModel

def csvInsertion(fileName,dayType,taskList,moodList,prod):
    fileExists=0
    result="0"
    if(path.exists(fileName+".csv")):
       fileExists=1
    count=1
    with open(fileName+'.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        if(fileExists==0):
            columnList=["day", "dayType"]
            for i in range(25):
                columnList.append("time"+str(i))
                columnList.append("mood"+str(i))
            columnList.append("avgProd")
            writer.writerow(columnList)
        with open(fileName+'.csv', 'r', newline='') as rFile:
            reader = csv.reader(rFile)
            count=len(list(reader))
            if(count==0):
                count+=1
        newRow=[count,dayType]
        for i in range(25):
            newRow.append(taskList[i])
            newRow.append(moodList[i])     
        newRow.append(prod)
        if(count%30==0):
            result=aggregationModel(fileName)
        writer.writerow(newRow)
    return result
