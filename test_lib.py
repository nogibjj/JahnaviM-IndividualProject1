'''test functions in lib for accurate functionality'''

from mylib.lib import plot_hist_time_occ, geo_plot_crime_rate, hist_plot_vict_age, print_stats, read_zip

def test_read_zip():
    '''test read_zip function'''
    df = read_zip()
    assert df.shape == (974477, 29)

def test_print_stats():
    '''test print_stats function'''
    df = read_zip()
    df_descr = print_stats(df)
    assert df_descr.shape == (8,16)

def test_plot_hist_time_occ():
    '''test plot_hist_TimeOcc function'''
    df = read_zip()
    df_time = plot_hist_time_occ(df)
    assert df_time.shape == (974477,)

def test_hist_plot_vict_age():
    '''test hist_plot_VictAge function'''
    df = read_zip()
    df_vict_age = hist_plot_vict_age(df)
    assert df_vict_age.shape == (974477,)

def test_geo_plot_crime_rate():
    '''test geo_plot_CrimeRate function'''
    df = read_zip()
    df_graph = plot_hist_time_occ(df)
    assert df_graph.shape == (78024, 5)
