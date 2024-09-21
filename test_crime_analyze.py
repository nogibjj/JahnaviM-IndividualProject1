from crime_analyze import execute_py

def test_df():
    df = execute_py()
    assert df.shape == (974477, 29)
    return