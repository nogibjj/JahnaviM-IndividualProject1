'''This file reads a crime dataset based on LAPD.
It produces summary statistics and data visualizations'''

from mylib.lib import print_stats,plot_hist_time_occ,geo_plot_crime_rate,hist_plot_vict_age

df = read_zip()

print_stats(df)

plot_hist_time_occ(df)

geo_plot_crime_rate(df)

hist_plot_vict_age(df)
