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

# FYI: Function zipcode_from_latlong()
# A function to use reverse geocode lookup to find a
#  postal_code (zipcode) associated with a lat/long coord

def zipcode_from_latlong( a_lat, a_long ):
    baseurl = "https://maps.googleapis.com/maps/api/geocode/json?"
    latlong = f"latlng={a_lat},{a_long}"
    api_key = f"&key={key_gmaps}"
    
    full_url = baseurl + latlong + api_key

    # Perform a reverse geocode loopup to find the zipcode associated with this lat/long coord
    g_response = requests.get(full_url)
    g_json = g_response.json()
    
    # Traverse the results to find a zipcode for this address
    zipcode = None
    for a in r_json['results'][0]['address_components']:
        if 'postal_code' in a['types']:
            zipcode = a['long_name']
            
    # Return the zipcode that was found
    return zipcode