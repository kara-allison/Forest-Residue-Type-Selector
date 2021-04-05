#will calculate the average DBH and provide an output file broken down by plot

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import csv files
DBHavgPath = "IndividualTreeDBH.csv"

#load csv files
DBHavg = pd.read_csv(DBHavgPath)

#turning stand and plot numbers into an integer so they can be
#sorted in the array, the multiplication is an attempt to deal with the new nomenclature of 001-1 instead of A-1
plotIDlist = []
for SurveyID in DBHavg["SurveyID"]:
    standID, plotIDstr = SurveyID.split("-")
    plotIDint = int(plotIDstr)
    standIDint = int(standID)
    newstandID = (standIDint * 1)
    newplotID = (plotIDint * 1)
    newIDasint = (newstandID,newplotID)
    plotIDlist.append(newIDasint)

DBHavg["plotID"] = plotIDlist

#computes average DBH of trees in four categories: tree DBH >20 inches,
#trees with DBH 8-20 inches, total number of trees >20 and total number of
#trees between 8-20 inches
plotIDset = list(set(plotIDlist))
plotIDset.sort()
meantreesg20list = []
meantreesl20list = []
countG20list = []
countL20list = []
for plotID in plotIDset:
    treesg20 = DBHavg.loc[(DBHavg["Tree_DBH(in)"] > 20) & (DBHavg["plotID"] == plotID)]
    treesl20 = DBHavg.loc[(DBHavg["Tree_DBH(in)"] <= 20) & (DBHavg["plotID"] == plotID)]
    meantreesg20 = treesg20["Tree_DBH(in)"].mean()
    meantreesl20 = treesl20["Tree_DBH(in)"].mean()
    meantreesg20list.append(meantreesg20)
    meantreesl20list.append(meantreesl20)
    countG20 = treesg20.shape[0]
    countL20 = treesl20.shape[0]
    countG20list.append(countG20)
    countL20list.append(countL20)
    
output = pd.DataFrame()
output["plotID"] = plotIDset
output["Avg 20+"] = meantreesg20list
output["Avg 8-20"] = meantreesl20list
output["# trees 20+"] = countG20list
output["# trees 8-20"] = countL20list
output.to_csv("PlotAreaDBHAvg.csv")

