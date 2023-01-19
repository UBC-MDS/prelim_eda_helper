from prelim_eda_helper.prelim_eda_helper import num_dist_by_cat
import pandas as pd
from io import StringIO
import sys

test_data_empty = pd.DataFrame( { 'cat_empty': [], 'num_empty': []})

test_data = pd.DataFrame(
    {
        'cat_1': [ 1, 1, 1, 1, 1, 1],
        'cat_2': [ 1, 1, 1, 2, 2, 2],
        'cat_3': [ 1, 1, 2, 2, 3, 3],
        'cat_4': [ 'one', 'one', 'two', 'two', 'three', 'three'],
        'cat_5': [ 'one', 'one', 'one', 'two', 'two', 'two'],
        'num_constant': [ 20, 20, 20, 20, 20, 20],
        'num_variance': [ 20, 20, 21, 22, 23, 24],
        'num_variable': [ 10, 20, 50, 100, 200, 300]
    }
)

def test_num_dist_by_cat():
    assert type( num_dist_by_cat( v_cat = 'cat_2', v_num = 'num_variable', data = test_data)).__name__ == 'HConcatChart'

    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_by_cat( v_cat = 'cat_empty', v_num = 'num_empty', data = test_data_empty)
    assert capturedOutput.getvalue().strip() == 'Please use a data frame with data inside.\n'.strip()

    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_by_cat( v_cat = 'cat_1', v_num = 'num_variable', data = test_data)
    assert( capturedOutput.getvalue().strip() == 'Please consider using prelim_eda_helper.num_dist when only 1 class is used\n.'.strip())

    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_by_cat( v_cat = 'cat_2', v_num = 'num_constant', data = test_data)
    assert( capturedOutput.getvalue().strip() == 'A t test is not performed as the total variance is 0.\n'.strip())

    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_by_cat( v_cat = 'cat_2', v_num = 'num_variable', data = test_data)
    assert( capturedOutput.getvalue()[:30].strip() == 'A t-test assuming equal varian'.strip())

    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_by_cat( v_cat = 'cat_3', v_num = 'num_variance', data = test_data)
    assert( capturedOutput.getvalue().strip() == 'F statistic is not defined when within group variance is 0 in at least one of the groups.\n'.strip())

    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_dist_by_cat( v_cat = 'cat_3', v_num = 'num_variable', data = test_data)
    assert( capturedOutput.getvalue()[:30].strip() == 'An one-way ANOVA yields an F s'.strip())
    # sys.stdout = sys.__stdout__ # Restore the print output target
