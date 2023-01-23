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
    
    captured_output = StringIO()
    sys.stdout = captured_output
    num_dist_by_cat(cat='cat_empty', num='num_empty', data=test_data_empty)
    assert captured_output.getvalue().strip() == 'Please use a data frame with data inside.\n'.strip()
    
    captured_output = StringIO()
    sys.stdout = captured_output
    num_dist_by_cat(cat='cat_1', num='num_variable', data=test_data)
    assert (captured_output.getvalue().strip() == 'Please consider using prelim_eda_helper.num_dist when only 1 '
                                                  'class is used\n.'.strip())
    
    captured_output = StringIO()
    sys.stdout = captured_output
    num_dist_by_cat(cat='cat_2', num='num_constant', data=test_data)
    assert (captured_output.getvalue().strip() == 'A t test is not performed as the total variance is 0.\n'.strip())
    
    captured_output = StringIO()
    sys.stdout = captured_output
    num_dist_by_cat(cat='cat_2', num='num_variable', data=test_data)
    assert (captured_output.getvalue()[:30].strip() == 'A t-test assuming equal varian'.strip())
    
    captured_output = StringIO()
    sys.stdout = captured_output
    num_dist_by_cat(cat='cat_3', num='num_variance', data=test_data)
    assert (captured_output.getvalue().strip() == 'F statistic is not defined when within group variance is 0 in '
                                                  'at least one of the groups.\n'.strip())
    
    captured_output = StringIO()
    sys.stdout = captured_output
    num_dist_by_cat(cat='cat_3', num='num_variable', data=test_data)
    assert (captured_output.getvalue()[:30].strip() == 'An one-way ANOVA yields an F s'.strip())
    # sys.stdout = sys.__stdout__ # Restore the print output target


def test_num_dist_scatter():
    # check chart type
    assert type(num_dist_scatter('num_variable', 'num_na', test_data, title='test')).__name__ == 'Chart'
    assert type(
        num_dist_scatter('num_variable', 'num_na', test_data, title='test', trend='poly')).__name__ == 'LayerChart'
    
    # check if NaN number correct
    captured_output = StringIO()
    sys.stdout = captured_output
    num_dist_scatter('num_variable', 'num_na', test_data, title='test', stat=True)
    assert captured_output.getvalue().strip()[100:103] == '3.0', 'The number of NaNs in a column is not correct!'
    
    # check if mean calculation is correct
    captured_output = StringIO()
    sys.stdout = captured_output
    num_dist_scatter('num_variable', 'num_na', test_data, title='test', stat=True)
    assert captured_output.getvalue().strip()[57:64] == '113.333', 'The number calculated for mean is incorrect!'
    
    # check if standard deviation calc is correct
    std_test = str(round(statistics.stdev(test_data['num_variance']), 3))
    captured_output = StringIO()
    sys.stdout = captured_output
    num_dist_scatter('num_variable', 'num_variance', test_data, title='test', stat=True)
    assert captured_output.getvalue().strip()[124:129] == std_test, 'Standard deviation test is incorrect!'
    
    # Check NaN replacement warning
    captured_output = StringIO()
    sys.stdout = captured_output
    num_dist_scatter('num_variable', 'num_na', test_data, title='test', stat=True)
    assert captured_output.getvalue().strip()[
           130:166] == '**num2 NaN replaced with mean 8.00**', 'NaN replacment warning not displaying'
    
    # Check Pearson's correlation
    captured_output = StringIO()
    sys.stdout = captured_output
    num_dist_scatter('num_variable', 'num_na', test_data, title='test', stat=True)
    assert captured_output.getvalue().strip()[256:260] == '0.77', "Pearson's correlation calc incorrect!"
    
    # Check Spearman's p-value
    captured_output = StringIO()
    sys.stdout = captured_output
    num_dist_scatter('num_variable', 'num_na', test_data, title='test', stat=True)
    assert captured_output.getvalue().strip()[-6:] == '0.1404', "Spearman's correlation p-value incorrect!"


class CatDistHeatmapTest(unittest.TestCase):
    def test_exc(self):
        with self.assertRaises(Exception) as context:
            cat_dist_heatmap(cat_1='cat_1', cat_2='cat_2', data=test_data_empty, heatmap=True, barchart=True)
        self.assertTrue("Dataset must have at least one row of data." in context.exception.__str__())

        with self.assertRaises(Exception) as context:
            cat_dist_heatmap(cat_1='num_variable', cat_2='cat_2', data=test_data, heatmap=True, barchart=True)
        self.assertTrue("num_variable does not appear to be a valid categorical column. Please double check the "
                        "input." in context.exception.__str__())

        with self.assertRaises(Exception) as context:
            cat_dist_heatmap(cat_1='cat_1', cat_2='cat_2', data=test_data, heatmap=False, barchart=False)
        self.assertTrue("At least one of the plot options (heatmap or barchart) needs to be selected (set to TRUE)."
                        in context.exception.__str__())

    def test_heatmap(self):
        output_chart = cat_dist_heatmap(cat_1='cat_1', cat_2='cat_2', data=test_data, heatmap=True, barchart=False)
        output_chart_json = output_chart.to_dict()

        self.assertTrue(output_chart_json['mark'] == 'rect')
        self.assertTrue(output_chart_json['encoding']['color']['aggregate'] == 'count')
        self.assertTrue(output_chart_json['encoding']['color']['type'] == 'quantitative')
        self.assertTrue(output_chart_json['encoding']['x']['axis']['title'] == 'cat_1')
        self.assertTrue(output_chart_json['encoding']['x']['field'] == 'cat_1')
        self.assertTrue(output_chart_json['encoding']['y']['axis']['title'] == 'cat_2')
        self.assertTrue(output_chart_json['encoding']['y']['field'] == 'cat_2')

    def test_barcharts(self):
        # test parameters
        cat_1 = 'cat_4'
        cat_2 = 'cat_5'
        
        # run func to get output
        output_chart = cat_dist_heatmap(cat_1='cat_4', cat_2='cat_5', data=test_data, heatmap=False, barchart=True)
        output_chart_json = output_chart.to_dict()

        self.assertTrue(output_chart_json['spec']['mark'] == 'bar')
        self.assertTrue(output_chart_json['spec']['encoding']['x']['aggregate'] == 'count')
        self.assertTrue(output_chart_json['spec']['encoding']['x']['type'] == 'quantitative')
        self.assertTrue(output_chart_json['spec']['encoding']['y']['axis']['title'] == cat_1)
        self.assertTrue(output_chart_json['spec']['encoding']['y']['field'] == cat_1)
        self.assertTrue(output_chart_json['spec']['encoding']['color']['field'] == cat_1)
        self.assertTrue(output_chart_json['facet']['row']['field'] == cat_2)


def num_dist_summary():
    
    assert type( num_dist_summary( num='num_constant', data = test_data, title ='Distribution', lab = None, thresh_corr = 0.2, stat = True)).__name__ == 'Chart'
    assert  num_dist_summary( num='abc', data = test_data, title ='Distribution', lab = None, thresh_corr = 0.2, stat = True) == 'abc not present in the dataset' 
    assert type( num_dist_summary( num='num_constant', data = test_data, title ='Distribution', lab = None, thresh_corr = 0.2, stat = False)).__name__ == 'Chart' 
    assert type( num_dist_summary( num='num_constant', data = test_data, title ='Distribution', lab = None, thresh_corr = 1, stat = False)).__name__ == 'Chart'
    assert  num_dist_summary( num = 1, data = test_data, title ='Distribution', lab = None, thresh_corr = 0.2, stat = True) == 'Please enter the column name as string'
    assert num_dist_summary( num='num_constant', data = test_data_empty, title ='Distribution', lab = None, thresh_corr = 0.2, stat = True) == 'Please use a data frame with data inside.'
    assert  num_dist_summary( num='num_constant', data = test_data, title = 1, lab = None, thresh_corr = 0.2, stat = True) == "Please enter the title as string"
    assert  num_dist_summary( num='num_constant', data = test_data, title = 'Distribution', lab = 1, thresh_corr = 0.2, stat = True) == "Please enter axis label as string"
    assert  num_dist_summary( num='num_constant', data = test_data, title = 'Distribution', lab = 1, thresh_corr = 0.2, stat = False) == "Please enter the value for stat be true or false"
    assert num_dist_summary( num='num_constant', data = test_data, title = 'Distribution', lab = 'p', thresh_corr = '0.2', stat = True) =='Please use a numeric value for threshold'
    
    
    output_chart =  num_dist_summary( num='num_constant', data = test_data, title ='Distribution', lab = "Numeric", thresh_corr = 0.2, stat = True)
    output_chart_json = output_chart.to_dict()


    assert output_chart_json['mark']  == 'bar'
    assert output_chart_json['title'] =='Distribution'
    assert output_chart_json['encoding']['x']['field']  == 'num_constant'
    assert output_chart_json['encoding']['x']['title']  == 'Numeric'
    assert output_chart_json['encoding']['y']['aggregate']  == 'count'
    assert output_chart_json['encoding']['y']['type'] == 'quantitative'
    assert output_chart_json['encoding']['y']['title'] == 'Count'

if __name__ == '__main__':
    unittest.main()
