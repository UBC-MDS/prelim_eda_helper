import sys
import unittest
import statistics
import pandas as pd

from io import StringIO
from prelim_eda_helper.prelim_eda_helper import num_dist_by_cat, cat_dist_heatmap, num_dist_scatter

test_data_empty = pd.DataFrame({'cat_empty': [], 'num_empty': []})

test_data = pd.DataFrame(
    {
        'cat_1': [1, 1, 1, 1, 1, 1],
        'cat_2': [1, 1, 1, 2, 2, 2],
        'cat_3': [1, 1, 2, 2, 3, 3],
        'cat_4': ['one', 'one', 'two', 'two', 'three', 'three'],
        'cat_5': ['one', 'one', 'one', 'two', 'two', 'two'],
        'num_constant': [20, 20, 20, 20, 20, 20],
        'num_variance': [20, 20, 21, 22, 23, 24],
        'num_variable': [10, 20, 50, 100, 200, 300],
        'num_na': [None, 4, None, 8, None, 12]
    }
)


def test_num_dist_by_cat():
    assert type(num_dist_by_cat(cat='cat_2', num='num_variable', data=test_data)).__name__ == 'HConcatChart'
    
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_by_cat(cat='cat_empty', num='num_empty', data=test_data_empty)
    assert capturedOutput.getvalue().strip() == 'Please use a data frame with data inside.\n'.strip()
    
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_by_cat(cat='cat_1', num='num_variable', data=test_data)
    assert (
                capturedOutput.getvalue().strip() == 'Please consider using prelim_eda_helper.num_dist when only 1 class is used\n.'.strip())
    
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_by_cat(cat='cat_2', num='num_constant', data=test_data)
    assert (capturedOutput.getvalue().strip() == 'A t test is not performed as the total variance is 0.\n'.strip())
    
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_by_cat(cat='cat_2', num='num_variable', data=test_data)
    assert (capturedOutput.getvalue()[:30].strip() == 'A t-test assuming equal varian'.strip())
    
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_by_cat(cat='cat_3', num='num_variance', data=test_data)
    assert (
                capturedOutput.getvalue().strip() == 'F statistic is not defined when within group variance is 0 in at least one of the groups.\n'.strip())
    
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_by_cat(cat='cat_3', num='num_variable', data=test_data)
    assert (capturedOutput.getvalue()[:30].strip() == 'An one-way ANOVA yields an F s'.strip())
    # sys.stdout = sys.__stdout__ # Restore the print output target


def test_num_dist_scatter():
    # check chart type
    assert type(num_dist_scatter('num_variable', 'num_na', test_data, title='test')).__name__ == 'Chart'
    assert type(
        num_dist_scatter('num_variable', 'num_na', test_data, title='test', trend='poly')).__name__ == 'LayerChart'
    
    # check if NaN number correct
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_scatter('num_variable', 'num_na', test_data, title='test', stat=True)
    assert capturedOutput.getvalue().strip()[100:103] == '3.0', 'The number of NaNs in a column is not correct!'
    
    # check if mean calculation is correct
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_scatter('num_variable', 'num_na', test_data, title='test', stat=True)
    assert capturedOutput.getvalue().strip()[57:64] == '113.333', 'The number calculated for mean is incorrect!'
    
    # check if standard deviation calc is correct
    std_test = str(round(statistics.stdev(test_data['num_variance']), 3))
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_scatter('num_variable', 'num_variance', test_data, title='test', stat=True)
    assert capturedOutput.getvalue().strip()[124:129] == std_test, 'Standard deviation test is incorrect!'
    
    # Check NaN replacement warning
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_scatter('num_variable', 'num_na', test_data, title='test', stat=True)
    assert capturedOutput.getvalue().strip()[
           130:166] == '**num2 NaN replaced with mean 8.00**', 'NaN replacment warning not displaying'
    
    # Check Pearson's correlation
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_scatter('num_variable', 'num_na', test_data, title='test', stat=True)
    assert capturedOutput.getvalue().strip()[196:201] == '0.771', "Pearson's correlation calc incorrect!"
    
    # Check Spearman's p-value
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_scatter('num_variable', 'num_na', test_data, title='test', stat=True)
    assert capturedOutput.getvalue().strip()[-5:] == '0.140', "Spearman's correlation p-value incorrect!"
