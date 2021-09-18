import plotly.express as px 
import csv 
import numpy as np

def getDataSource(data_path):
    Marks=[]
    Days_present=[]
    with open(data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            Marks.append(float(row["Marks In Percentage"]))
            Days_present.append(float(row["Days Present"]))
    return{"x":Marks,"y":Days_present}

def findCorrelation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("correlation is", correlation[0,1])
def setup():
    data_path="project_correlation.csv"
    data_source=getDataSource(data_path)
    findCorrelation(data_source)
setup()