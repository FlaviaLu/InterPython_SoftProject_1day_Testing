"""Tests for statistics functions within the Model layer."""

import pandas as pd
import pytest

# def test_max_mag_integers():
#     # Test that max_mag function works for integers
#     from lcanalyzer.models import max_mag

#     test_input_df = pd.DataFrame(data=[[1, 5, 3], 
#                                        [7, 8, 9], 
#                                        [3, 4, 1]], columns=list("abc"))
#     test_input_colname = "a"
#     test_output = 7

#     assert max_mag(test_input_df, test_input_colname) == test_output

# def test_max_mag_zeros():
#     # Test that max_mag function works for zeros
#     from lcanalyzer.models import max_mag

#     test_input_df = pd.DataFrame(data=[[0, 0, 0], 
#                                        [0, 0, 0], 
#                                        [0, 0, 0]], columns=list("abc"))
#     test_input_colname = "b"
#     test_output = 0

#     assert max_mag(test_input_df, test_input_colname) == test_output

@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (pd.DataFrame(data=[[1, 5, 3], 
                            [7, 8, 9], 
                            [3, 4, 1]], 
                      columns=list("abc")),
        "a",
        7),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        0),
    ])

def test_max_mag(test_df, test_colname, expected):
    """Test max function works for array of zeroes and positive integers."""
    from lcanalyzer.models import max_mag
    assert max_mag(test_df, test_colname) == expected

    

# def test_min_mag_positive():
#     # Test that min_mag function works only for positive values

#     from lcanalyzer.models import min_mag
    
#     test_input_df = pd.DataFrame(data=[[-1,2,3],
#                                        [5,8,-4],
#                                        [1,-5,5]],columns=list('abc'))
#     test_input_colname='a'
#     test_output = -1
#     assert min_mag(test_input_df,test_input_colname) == test_output




@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (pd.DataFrame(data=[[-1, 5, 3], 
                            [7, 8, 9], 
                            [3, 4, 1]], 
                      columns=list("abc")),
        "a",
        -1),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        0),
    ])

def test_min_mag(test_df, test_colname, expected):
    """Test max function works for array of zeroes and positive integers."""
    from lcanalyzer.models import min_mag
    from pytest import approx
    assert min_mag(test_df, test_colname) == approx(expected,1)
    