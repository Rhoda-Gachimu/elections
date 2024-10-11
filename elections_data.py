import arcgis
import pandas as pd
import os
# import arcpy


rename_cols = {
    "state_po":"state_abbr",
    "county_fips":"FIPS",
    "party":"pol_identity"
}

elections_data_path = "DATA\countypres_2000-2020.csv"
election_results = pd.read_csv(elections_data_path, dtype={"county_fips":object})
election_results.rename(columns=rename_cols, inplace=True)
election_results.head()


print(election_results)
print()