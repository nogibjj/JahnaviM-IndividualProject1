'''test functions in lib for accurate functionality'''

from lib import plot_hist_TimeOcc, geo_plot_CrimeRate, hist_plot_VictAge, print_stats, read_zip

def test_read_zip():
    '''test read_zip function'''
    df = read_zip()
    assert df.shape == (974477, 29)

def test_print_stats():
    '''test print_stats function'''
    df = read_zip()
    df_descr = print_stats(df)
    assert df_descr.shape == (8,16)

def test_plot_hist_TimeOcc():
    '''test plot_hist_TimeOcc function'''
    df = read_zip()
    df_time = plot_hist_TimeOcc(df)
    assert df_time.shape == (974477,)

def test_hist_plot_VictAge():
    '''test hist_plot_VictAge function'''
    df = read_zip()
    df_vict_age = hist_plot_VictAge(df)
    assert df_vict_age.shape == (974477,)

def test_geo_plot_CrimeRate():
    '''test geo_plot_CrimeRate function'''
    df = read_zip()
    df_graph = plot_hist_TimeOcc(df)
    assert df_graph.shape == (78024, 5)
