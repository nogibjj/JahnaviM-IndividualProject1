'''This script contains all functions intended to be used on the 
crime dataset for descriptive stats and visuals'''

# Necessary imports
import zipfile
from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def read_zip(zip_file = 'Crime_Data_from_2020_to_Present.csv.zip',
             csv_file = "Crime_Data_from_2020_to_Present.csv"):
    '''Read a zip file that is compressed from csv using pandas'''
    with zipfile.ZipFile(zip_file) as z:
        with z.open(csv_file) as f:
            df = pd.read_csv(f)
    return df

def print_stats(df):
    '''Print basic sturcture and statistics about crime dataset'''
    print('These are the columns in the dataset:')
    print('\t', df.columns)
    print(f'Data Frame Size: {df.shape[0]} rows, {df.shape[1]} columns')
    print('This is what the first five rows look like:')
    display(df.head())

    # Convert the time occurred column to accurate hour of the day
        # with decimal representing accurate minute proportion of the hour
    df['TimeOccHr'] = df['TIME OCC']//100 + df['TIME OCC']%100/60

    print('Summary Statistics by Column:')
    display(df.describe())
    return df.describe()

def plot_hist_time_occ(df):
    '''Plot a histogram of when the crimes occured in LA'''
    plt.figure(figsize = (15,6))
    h = (df['TimeOccHr']).hist(bins = 24)
    h.set(xlabel = "Hour of Day", ylabel = "Crime Occurences",
          title = "Distribution of Crime Occurences over Time of Day")
    plt.xticks(ticks = [2*i for i in range(13)])
    plt.show()
    return df['TimeOccHr'].shape

def geo_plot_crime_rate(df):
    '''Creat a geoplot of the crime rate in LA based on latitude/longitude location'''
    df_graph = df[df['LAT'] != 0].groupby(
        ['AREA NAME', 'LAT', 'LON']).count()[['DR_NO']].reset_index()
    df_graph['Crime Rate'] = df_graph['DR_NO']

    df_graph
    df_graph.dropna(
        axis=0,
        how='any',
        subset=None,
        inplace=True
    )

    color_scale = [(0, 'pink'), (1,'red')]

    fig = px.scatter_mapbox(df_graph,
                            lat="LAT",
                            lon="LON",
                            color="Crime Rate",
                            color_continuous_scale=color_scale,
                            hover_name="AREA NAME",
                            hover_data=["AREA NAME"],
                            size="Crime Rate",
                            zoom=10,
                            height=800,
                            width=800,
                            )

    fig.update_layout(mapbox_style="carto-positron")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()
    return df_graph

def hist_plot_vict_age(df):
    '''Create a histogram of the victim age when crimes had a victim'''
    plt.figure(figsize = (15, 5))
    p = df[df['Vict Age'] > 0]['Vict Age'].hist(bins = 16)
    p.set(xlabel = 'Victim Age', ylabel = 'Number of Victims',
          title = "Distribution of Victim Ages in LAPD")
    plt.xticks(ticks = [10*i for i in range(0,13)])
    plt.xlim(0,120)
    plt.show()
