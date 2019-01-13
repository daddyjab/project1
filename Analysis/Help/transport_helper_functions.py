# transport_helper_functions.py
# AUTHOR: Jeff Brown
# 
# A collection of functions used with
# Data Cleaning, Exploration, and Analysis
# in support of Transport Data Analysis with Project 1

# Dependencies
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from scipy import stats
from pprint import pprint

# Functions to find the distance between 2 lat/long coordinates
# Description: https://pypi.org/project/geopy/1.9.1/
# from geopy.distance import (distance, great_circle)

# Function to find the a (lat, long) coord that is closest to a reference point
#  and then return the index of the coord in the provided list of coords
# Note: If the coordinates are duplicated in the list of coordinates,
#        then the index of the first coordinate is returned
# r: reference point as a tuple (lat, long)
# stop_coords: a list of tuples with ('stop_lat', 'stop_lon')
#               generated from the dataframe containing CTA stops

#def closest_coord(coords, r):
    # Find the lat/long tuple closest to the reference point provided
    # close_point = min( coords, key=lambda z: distance( z, r ).feet )
    
    # Get the index of this closest point in the list of coordinates
    # (Note, if there are dups in the list just return the first index)
    # retval = coords.index( close_point )
    # return retval


# Function to generate a linear regression and a set of data points for the trend line
def gen_linear_trend( a_x, a_y , a_start=None, a_stop=None ):    
    # Perform the linear regression
    lr = stats.linregress(a_x[a_start:a_stop], a_y[a_start:a_stop] )

    pprint(lr)
    
    # Generate a set of data points for the trend line
    # trend_line = lr.slope * a_x + lr.intercept
    trend_line = [ x * lr.slope + lr.intercept for x in a_x[a_start:a_stop] ]

    # Create a label describing the trend
    trend_label = f"Trend: Y-value = {lr.slope:.4f} x [ X-value ] + {lr.intercept:.4f}"
    trend_label += f"\nCorrelation (R-Value): {lr.rvalue:.4f}"
    trend_label += f"\n1-(p-Value): {(1-lr.pvalue):.4%}"
    
    return { 'trend_line': trend_line, 'trend_label': trend_label }

# Function to generate an array containing the
#  moving average of the list provided in the argument
def moving_average(values, window_size):
    # Create a "window" based upon the window size with value 1/window_size
    window = np.ones(int(window_size))/float(window_size)
    
    # Calculate the average of the window moving across the elements of "values"
    #  using the convolve function to multiply and add
    return np.convolve( values, window, 'same')

# Function to make a scatter plot of selected columns
# Arguments: a dictionary 'a_plot_dict' with elements
#    'data_df': dataframe with data to plot
#    'y_column': Column to be plotted on y-axis of scatter plot
#    'x_column': Column to be plotted on x-axis of scatter plot
#    'color_list': list of Colors to use for markers (same size as a_color_thresh)
#    'color_thresh': list of y-value thresholds used to select a color
#    'ma_window_size': Window size used for moving average
#    'chart_title': Title of the chart
#    'y_label': Label for the y-axis
#    'x_label': Label for the y-axis
#    'save_file': Save file for the plot

def gen_scatter_plot(a_plot_dict):
    
    # Extract the arguments from the a_plot_dict arg
    a_chart_title = a_plot_dict['chart_title']
    a_save_file = a_plot_dict['save_file']

    a_data_df = a_plot_dict['data_df']
    a_y_label = a_plot_dict['y_label']
    a_y_column = a_plot_dict['y_column']
    a_color_list = a_plot_dict['color_list']
    a_color_thresh = a_plot_dict['color_thresh']

    a_x_label = a_plot_dict['x_label']
    a_x_column = a_plot_dict['x_column']

    # Optional: Y-axis trend line (primary axis)
    if 'data_trend' in a_plot_dict.keys():
        a_trend_plotflag = True
        a_data_trend = a_plot_dict['data_trend']

        # If a trend_label has been specified then display it
        # Otherwise, no trend label will be displayed
        try:
            a_data_trend_label = a_plot_dict['data_trend_label']
        except KeyError:
            a_data_trend_label = None
            
        # If a trend_label location is specified, use it
        # Otherwise, use defaults
        try:
            a_data_trend_label_loc_h = a_plot_dict['data_trend_label_loc_h']
            a_data_trend_label_loc_v = a_plot_dict['data_trend_label_loc_v']
        except KeyError:
            a_data_trend_label_loc_h = 0.03
            a_data_trend_label_loc_v = 0.05

    else:
        a_trend_plotflag = False
    
    # TODO: Implement this plot on secondary axis - later...
    # Optional: Secondary Y-axis plot
    if 'y2_column' in a_plot_dict.keys():
        a_y2_plotflag = True
        a_y2_label = a_plot_dict['y2_label']
        a_y2_column = a_plot_dict['y2_column']
    else:
        a_y2_plotflag = False        

    # Optional: Moving average plot
    if 'ma_window_size' in a_plot_dict.keys():
        a_ma_plotflag = True
        a_ma_window_size = a_plot_dict['ma_window_size']

        # If a moving average location is specified, use it
        # Otherwise, use defaults
        try:
            a_ma_label_loc_h = a_plot_dict['ma_label_loc_h']
            a_ma_label_loc_v = a_plot_dict['ma_label_loc_v']
        except:
            a_ma_label_loc_h = 0.03
            a_ma_label_loc_v = 0.05
    else:
        a_ma_plotflag = False        

    # Generate Scatter Plots for key metrics vs. 'Total CTA Stops'
    # Add trend lines to each and look for patterns
    # Generate a scatter plot
    fig, ax = plt.subplots(figsize=(10,5))

    # Color scheme for markers
    color_list = a_color_list

    # Thresholds for selecting colors
    color_threshold_list = a_color_thresh

    # Initialize array of marker colors
    marker_colors = []

    # The value to plot on the y-axis
    c_plotcolumn = a_y_column

    # The value to plot on the x-axis
    c_x_column = a_x_column

    # Create the markers by iterating through zipcode
    for ci in a_data_df.index:
        # Set the color of the markers based upon temperature
        c_plotvalue = a_data_df.loc[ci,c_plotcolumn]

        # If the value is not populated for this bin,
        #  continue to move to the next value
        if math.isnan(c_plotvalue):
            continue

        # Select marker color and add it to the list
        try:
            marker_colors.append( color_list[ np.digitize(c_plotvalue, color_threshold_list) ] )
        except IndexError:
            # If the thresholds were defined improperly and
            #  the c_plotvalue is higher than the highest threshold value,
            # Then just set the color to be high highest color in the list
            marker_colors.append( color_list[ -1 ] )
            #print(f"IndexError: ci:{ci}: c_plotvalue:{c_plotvalue} => index for color_list:{np.digitize(c_plotvalue, color_threshold_list)}")

    # Plot a scatter plot
    plt.scatter(a_data_df[c_x_column], a_data_df[c_plotcolumn], c=marker_colors, alpha=0.5)

    # Add a value for this point if it is the maximum and minimum points
    # Get the index values for value is max and min
    # Note: Could end up being multiple data points,
    #  so select the first max, and the last min
    ci_max = a_data_df.loc[ a_data_df[c_plotcolumn] == a_data_df[c_plotcolumn].max() ].index
    ci_min = a_data_df.loc[ a_data_df[c_plotcolumn] == a_data_df[c_plotcolumn].min() ].index

    # Place the values for these points on the scatter plot
    text_offset = 0
    plt.text(float(a_data_df.loc[ci_max[0],c_x_column]),
             float(a_data_df.loc[ci_max[0], c_plotcolumn ]) + text_offset,
             f"{float(a_data_df.loc[ci_max[0], c_plotcolumn ]):.1f}" , ha='center')

    plt.text(float(a_data_df.loc[ci_min[-1],c_x_column]),
             float(a_data_df.loc[ci_min[-1], c_plotcolumn ]) - text_offset,
             f"{float(a_data_df.loc[ci_min[-1], c_plotcolumn ]):.1f}" , ha='center')

    # Set the x tick marks and labels
    # plt.xticks(merged_rest_df.loc[ci_max,c_x_column], merged_rest_df.loc[ci_max,c_x_column], rotation=45)
    # TODO: Change the x_tick labels to match this c_x_column data
    #x_gran = 10.0
    #plt.xticks(np.arange(-90.0,90.0+x_gran,x_gran),
    #           [str(x) for x in np.arange(-90.0,90.0+x_gran,x_gran)],
    #           rotation=90)

    # Set the y access limits to add room for the value labels
    y_bot = a_data_df[c_plotcolumn].min()
    y_top = a_data_df[c_plotcolumn].max()
    y_range = y_top-y_bot

    y_bot -= y_range * 0.15
    y_top += y_range * 0.15
    plt.ylim( bottom=y_bot, top=y_top)

    # Adjust the tick marks to be more granular
    # plt.yticks(np.arange(round(y_bot,-1),round(y_top,-1),step=y_range/10))

    plt.xlabel(a_x_label)
    plt.ylabel(a_y_label)
    plt.title(a_chart_title)

    plt.grid(True, axis='both', color='0.75', alpha=0.5)

    # Add a key for the color coding used on the plot
    for i in range(1,len(color_threshold_list)):
        # Text to display
        box_text = f"{color_threshold_list[i-1]} to {color_threshold_list[i]}"
        box_fmt = {'boxstyle':'square', 'facecolor':color_list[i], 'alpha':0.75}

        # Plot this
        plt.text(0.03, 0.97 -((len(color_threshold_list)-i-1)*0.08),
                 box_text, transform=ax.transAxes, fontsize=11, verticalalignment='top', bbox=box_fmt)

    # Generate a dataframe that is sorted by c_x_column
    # In case it's needed for: Moving Average, Secondary Axis plot
    a_data_sorted_df = a_data_df.sort_values(by=c_x_column).reset_index(drop=True)
     
    # Add a moving average plot on the primary axis if it has been specified
    if a_ma_plotflag:
        # Set the window size for the moving average
        trend_window_size = a_ma_window_size

        # Calculate the moving average
        # Use the sorted dataframe
        trend = moving_average(a_data_sorted_df[c_plotcolumn], trend_window_size)

        # Generate the trend plot
        plt.plot(a_data_sorted_df[c_x_column], trend, color='k', linestyle=':')

        # Add a key for the moving average
        box_text = f"Trend: Moving Average\n(Window Size={trend_window_size})"
        box_fmt = {'boxstyle':'square', 'facecolor':"gray", 'alpha':0.75}
        plt.text(a_ma_label_loc_h, a_ma_label_loc_v,
                 box_text, transform=ax.transAxes,
                 fontsize=9, verticalalignment='bottom', horizontalalignment='left', bbox=box_fmt)

    # Add a horizontal line at the y = 0% level
    # plt.hlines(y=0, xmin=-1, xmax=len(a_data_df.index), alpha='0.5')

    # Add a trend line on the primary axis if it has been specified
    if a_trend_plotflag:
        # For the trend line, let's sort (x,y) pairs in the order of the
        # x-values so that the x-values will be monotonically increasing
        
        # Pair up the x and y values the represent the trend line
        trend_points = zip(a_data_df[c_x_column], a_data_trend )
        
        # Sort the (x,y) pairs based upon the x-values in the pairs
        sorted_trend_points = sorted( trend_points, key=lambda p: p[0])
        
        # Plot the trend line
        plt.plot([x for (x,y) in sorted_trend_points ],
                 [y for (x,y) in sorted_trend_points ],
                 color='k', linestyle='dashed')
        
        # Add a key for the trend line if it has been specified
        if a_data_trend_label != None:
            box_text = a_data_trend_label
            box_fmt = {'boxstyle':'square', 'facecolor':"gray", 'alpha':0.75}
            plt.text(a_data_trend_label_loc_h, a_data_trend_label_loc_v,
                     box_text, transform=ax.transAxes,
                     fontsize=9, verticalalignment='top', horizontalalignment='center', bbox=box_fmt)

    # Add plot on secondary axis if it has been specified
    if a_y2_plotflag:
        # Align the x-axis of the secondary plot with the primary plot
        ax2 = ax.twinx()

        # Create the line plot using same x-axis as primary plot
        ax2.plot(a_data_sorted_df[c_x_column], a_data_sorted_df[a_y2_column],
                 color='brown', marker='o', linestyle='solid')
        
        # Set the label for the y2 secondary axis
        ax2.set_ylabel(a_y2_label, color="brown")

    # Add a horizontal line at the y = 0% level
    # plt.hlines(y=0, xmin=-90, xmax=+90, alpha=0.5)

    plt.tight_layout()
    plt.show()
    
    # Save the plot
    fig.savefig(a_save_file)

# Function to make a bar plot of selected columns
# Arguments: a dictionary 'a_plot_dict' with elements
#    'chart_title': Title of the chart
#    'save_file': Save file for the plot

#    'data_df': dataframe with binned data to plot on primary axis
#    'data_sem_df': dataframe standard errors of mean for the binned data to plot in data_df
#    'y_label': Label for the y-axis
#    'y_column': Column to be plotted on y-axis of plot
#    'color_list': list of Colors to use for markers (same size as a_color_thresh)
#    'color_thresh': list of y-value thresholds used to select a color

#    'data_trend': List (or Series) with trend line to plot on primary axis

#    'y2_label': Label for the secondary y-axis
#    'y2_column': Column to be plotted on secondary y-axis

#    'x_label': Label for the x-axis
#    'x_column': Column to be plotted on x-axis of scatter plot

def gen_bar_plot(a_plot_dict):
    
    # Extract the arguments from the a_plot_dict arg
    # Chart level parameters
    a_chart_title = a_plot_dict['chart_title']
    a_save_file = a_plot_dict['save_file']

    # X-axis parameters
    a_x_label = a_plot_dict['x_label']
    a_x_column = a_plot_dict['x_column']
 
    # Y-axis parameters (primary axis)
    a_data_df = a_plot_dict['data_df']
    a_data_sem_df = a_plot_dict['data_sem_df']
    a_y_label = a_plot_dict['y_label']
    a_y_column = a_plot_dict['y_column']
    a_color_list = a_plot_dict['color_list']
    a_color_thresh = a_plot_dict['color_thresh']
    
    # Optional: Y-axis trend line (primary axis)
    if 'data_trend' in a_plot_dict.keys():
        a_trend_plotflag = True
        a_data_trend = a_plot_dict['data_trend']

        # If a trend_label has been specified then display it
        # Otherwise, no trend label will be displayed
        try:
            a_data_trend_label = a_plot_dict['data_trend_label']
        except KeyError:
            a_data_trend_label = None
            
        # If a trend_label location is specified, use it
        # Otherwise, use defaults
        try:
            a_data_trend_label_loc_h = a_plot_dict['data_trend_label_loc_h']
            a_data_trend_label_loc_v = a_plot_dict['data_trend_label_loc_v']
        except KeyError:
            a_data_trend_label_loc_h = 0.03
            a_data_trend_label_loc_v = 0.05

    else:
        a_trend_plotflag = False
    
    # Optional: Secondary Y-axis plot
    if 'y2_column' in a_plot_dict.keys():
        a_y2_plotflag = True
        a_y2_label = a_plot_dict['y2_label']
        a_y2_column = a_plot_dict['y2_column']
    else:
        a_y2_plotflag = False        

    # Generate the plot
    fig, ax = plt.subplots(figsize=(10,5))

    # Color scheme for markers
    color_list = a_color_list

    # Thresholds for selecting colors
    color_threshold_list = a_color_thresh

    # Generate bars by iterating through each bin
    for ci in a_data_df.index:

        # Set color bars based upon temperature
        c_plotvalue = a_data_df.loc[ci,a_y_column]

        # If temperature is not populated for this bin,
        #  continue to move to the next bin
        if math.isnan(c_plotvalue):
            continue

        # Set the error bars using the standard deviation of the mean (sem)
        c_sem = a_data_sem_df.loc[ci,a_y_column]

        # Select bar color 
        try:
            c_color = color_list[ np.digitize(c_plotvalue, color_threshold_list) ]
        except IndexError:
            # If the thresholds were defined improperly and
            #  the c_plotvalue is higher than the highest threshold value,
            # Then just set the color to be high highest color in the list
            c_color = color_list[ -1 ]
     
        # Set the placement location for the value text
        text_offset = 0
        c_textloc = c_plotvalue + text_offset

        # Get the value associated with this bar
        c_valuetext = f"{c_plotvalue:.1f}"

        # Plot a bar
        plt.bar(ci, c_plotvalue, color=c_color, yerr=c_sem, error_kw={'alpha':0.75})

        # Place the value on this bar
        plt.text(ci, c_textloc, c_valuetext , ha='left')

    plt.xticks(range(len(a_data_df.index)), a_data_df[a_x_column], rotation=45)

    # Set the y access limits to add room for the value labels
    y_bot = a_data_df[a_y_column].min()
    y_top = a_data_df[a_y_column].max() + 0.5*a_data_sem_df[a_y_column].max()
    y_range = y_top-y_bot

    y_bot -= y_range * 0.15
    y_top += y_range * 0.15
    plt.ylim( bottom=y_bot, top=y_top)

    # Adjust the tick marks to be more granular
    #plt.yticks(np.arange(round(y_bot,-1),round(y_top,-1),step=10))

    plt.xlabel(a_x_label)
    plt.ylabel(a_y_label)
    plt.title(a_chart_title)

    plt.grid(True, axis='y', color='0.75', alpha=0.5)
    # plt.legend(loc="best")

    # Add a key for the color coding used on the plot
    for i in range(1,len(color_threshold_list)):
        # Text to display
        box_text = f"{color_threshold_list[i-1]} to {color_threshold_list[i]}"
        box_fmt = {'boxstyle':'square', 'facecolor':color_list[i], 'alpha':0.75}

        # Plot this
        plt.text(0.99, 0.97 -((len(color_threshold_list)-i-1)*0.08),
                 box_text, transform=ax.transAxes, fontsize=11,
                 verticalalignment='top', horizontalalignment='right', bbox=box_fmt)

    # Add a horizontal line at the y = 0% level
    # plt.hlines(y=0, xmin=-1, xmax=len(a_data_df.index), alpha='0.5')

    # Add a trend line on the primary axis if it has been specified
    if a_trend_plotflag:
        plt.plot(range(len(a_data_trend)), a_data_trend,
                 color='k', linestyle='dashed')
        
        
        # Add a key for the trend line if it has been specified
        if a_data_trend_label != None:
            box_text = a_data_trend_label
            box_fmt = {'boxstyle':'square', 'facecolor':"gray", 'alpha':0.75}
            plt.text(a_data_trend_label_loc_h, a_data_trend_label_loc_v,
                     box_text, transform=ax.transAxes,
                     fontsize=9, verticalalignment='top', horizontalalignment='center', bbox=box_fmt)

    # Add plot on secondary axis if it has been specified
    if a_y2_plotflag:
        # Align the x-axis of the secondary plot with the primary plot
        ax2 = ax.twinx()
        
        # Create the line plot using same x-axis as primary plot
        ax2.plot(range(len(a_data_df.index)), a_data_df[a_y2_column],
                 color='brown', marker='o', linestyle='solid')
        
        # Set the label for the y2 secondary axis
        ax2.set_ylabel(a_y2_label, color="brown")
    
    plt.tight_layout()
    plt.show()
        
    # Save the plot
    fig.savefig(a_save_file)

