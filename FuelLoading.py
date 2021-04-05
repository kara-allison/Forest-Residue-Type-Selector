# load Fuel loading data and process data to show best fit with baseline data

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# path to fuel loading data, required baseline and user plot-data
baselinePath = "FuelLoadingBaseline.csv"
plotDataPath = "PlotData.csv"

# load actual csv files
# Must be in utf-8 encoding! Excel can save it in this format.
baseline = pd.read_csv(baselinePath)
plots = pd.read_csv(plotDataPath)

# compute z-scores
zscore_base = (baseline.iloc[:,5:] - baseline.iloc[:,5:].mean()) / baseline.iloc[:,5:].std()
zscore_plot = (plots.iloc[:,1:] - baseline.iloc[:,5:].mean()) / baseline.iloc[:,5:].std()

Nbases = len(baseline.index)
Nplots = len(plots.index)
best = []
plotIDlist = []
for plotID in range(0,Nplots):
  # compute distance between baseline and plot data
  temp = (zscore_base - zscore_plot.iloc[plotID,:])**2
  dist = temp.sum(axis=1)
  minidx = dist.idxmin()
  best.append(minidx)
  plotIDlist.append(plots.iloc[plotID,0])


output = baseline.iloc[best, 0:5]
bestFitRow = np.array(best) + 2
output.insert(0,"best fit row",bestFitRow)
output["plotIDs"] = plotIDlist
output.to_csv("best_fit_FuelLoading.csv",index=False)

