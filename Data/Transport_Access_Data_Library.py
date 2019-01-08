# File: Transport_Access_Data_Library.py
# Author: Jeff Brown
#
# Placeholder for functions for making use of Datasets and/or APIs
# associated with Transportation Access data sources
#

# Dependencies and Setup
import pandas as pd

# Read in the Chicago CTA stop + zipcode info previously cleaned
i_file = "./chicago_cta_stops.csv"

# Read the data into a dataframe
c_cta_stops_df = pd.read_csv(i_file)

# Data types
# Note: 'stop_code' and 'parent_station' both are type 'float64' since these columns may have NaN values.
# (For some reason, NaN results in an error if the data type is 'int64')
print ( c_cta_stops_df.dtypes )

# Quick preview of the data
print ( c_cta_stops_df.head() )
