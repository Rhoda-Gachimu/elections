import arcgis
import pandas as pd
import os
# import arcpy


elections_data_path = "DATA\countypres_2000-2020.csv"
election_results = pd.read_csv(elections_data_path)

print(election_results)