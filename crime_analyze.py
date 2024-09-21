'''This file reads a crime dataset based on LAPD.
It produces summary statistics and data visualizations'''

from lib import read_zip, print_stats, plot_hist_TimeOcc, geo_plot_CrimeRate, hist_plot_VictAge

df = read_zip()

print_stats(df)

plot_hist_TimeOcc(df)

geo_plot_CrimeRate(df)

hist_plot_VictAge(df)
