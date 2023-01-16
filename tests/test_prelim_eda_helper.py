from prelim_eda_helper.prelim_eda_helper import num_cat
import pandas as pd
from io import StringIO
import sys

test_data_0_group = pd.DataFrame( { 'cat': [], 'num': []})

test_data = pd.DataFrame(
    {
        'cat_1group': [ 1, 1, 1, 1, 1, 1],
        'cat_2groups': [ 1, 1, 1, 2, 2, 2],
        'cat_3groups': [ 1, 1, 2, 2, 3, 3],
        'num_constant': [ 20, 20, 20, 20, 20, 20],
        'num_0_within_group_variance': [ 20, 20, 21, 22, 23, 24],
        'num': [ 10, 20, 50, 100, 200, 300]
    }
)

def test_num_cat():
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_cat( v_cat = 'cat', v_num = 'num', data = test_data_0_group)
    assert capturedOutput.getvalue().strip() == 'Please use a data frame with data inside.\n'.strip()

    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_cat( v_cat = 'cat_1group', v_num = 'num', data = test_data)
    assert( capturedOutput.getvalue().strip() == 'Please consider using prelim_eda_helper.num_dist when only 1 class is used\n.'.strip())

    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_cat( v_cat = 'cat_2groups', v_num = 'num_constant', data = test_data)
    assert( capturedOutput.getvalue().strip() == 'A t test is not performed as the total variance is 0.\n'.strip())

    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    num_cat( v_cat = 'cat_2groups', v_num = 'num', data = test_data)
    assert( capturedOutput.getvalue()[:30].strip() == 'A t-test assuming equal varian'.strip())
    # sys.stdout = sys.__stdout__ # Restore the print output target
