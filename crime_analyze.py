'''This file reads a crime dataset based on LAPD.
It produces summary statistics and data visualizations'''

from mylib.lib import read_zip, print_stats, plot_hist_Time_Occ, geo_plot_Crime_Rate, hist_plot_Vict_Age

df = read_zip()

print_stats(df)

plot_hist_Time_Occ(df)

geo_plot_Crime_Rate(df)

hist_plot_Vict_Age(df)
