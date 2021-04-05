Code created by Kara Allison and Kali Allison. Data compiled by Kara Allison.

This code computes the closest forest residue type to the user provided data which can be used to create predictive vegetation wildfire hazard conditions for the Pacific Northwest, more specifically western Washington. Baseline data is based on the US Forest Service's "Photo Series for Quantifying Natural Forest Residues in Common Vegetation Types of the Pacific Northwest" (1980). 

The code calculates the distance between the collected user provided plot data and the baseline data to provide the best fit forest residue type. In order to do that, and to take into account differences in magnitude for the different data types (eg 30 average dbh vs 5% tree cover), the average and standard deviation of each data type (eg average number of snags) was used to generate a z-score for each point of data (book or plot derived). The distance between the book and plot derived z-scores is then calculated, and the best fit scenario is saved into the output file.

To assist with the calcuations, a separate bit of code, CalculateAverageDBH, has been created to generate the necessary averages (eg tree DBH) which can then be copied into a csv file to run with FuelLoading.py

Some assumptions: 
The spread rate, flame length, and resistance to control values are assuming a flat area with 4 mph winds, and 4% fuel moisture. This code does not take into account all of the data used to calculate forest residue types and fuel loads. Rather, a selection of relevent data has been adapted to the book data for comparative purposes. 

Currently, all data points are weighted equally at .111 (1/9 or 11.11%). This can be adjusted easily to any value, provided the sum of the different weights always equals 1.