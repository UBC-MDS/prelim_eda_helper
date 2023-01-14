def num_cat( v_num, v_cat, data, title = '', lab_num = None, lab_cat = None, violin = True, num_on_x = True, stat = True):
    '''
    Create a pair of charts showing the distribution of the numeric variable in general and when grouped by the categorical variable.
    The one of the left is a histogram while the one on the left will be a boxplot on top of a violin plot.
    Basic test statistics will be printed for user as a reference.

    Parameter
    ---------
    v_num: string
        Name of the column name for the numeric variable.
    v_cat: string
        Name of the column name for the categorial variable.
    data: pandas.DataFrame
        Target data frame for visualization.
    title: string, default ''
        Title for the chart.
    lab_num: string
        Axis label for the numeric variable.
    lab_cat: string
        Axis label for the categorical variable.
    violin: boolean, default True
        Whether include a violin plot or not.
    num_on_x: boolean, default True
        Whether the numeric variable is put on the x-axis in the boxplot.
    stat: boolean, default True
        Whether printing the test statistics and summary or not.
    
    Return
    ------
    altair.Chart
        A concatenated chart consists of a histogram and a boxplot.
    '''


def num_num(num1, num2, data, title = '', lab_num1 = None, lab_num2 = None, trend = None, band = False):
    '''
    Creates a scatter plot given two numerical features. Plot can provide regression trendline and highlight outliers. 
    Spearman and Pearson's correlation will also be returned to aid the user to determining feature relationship.

    Parameter
    ---------
    num1: string
        Name of the column name for the first numeric feature.
    num2: string
        Name of the column name for the second numeric feature.
    data: pandas.DataFrame
        Target data frame for visualization.
    title: string, default ''
        Title for the chart.
    lab_num1: string, default None
        Axis label for the first numeric feature.
    lab_num2: string, default None
        Axis label for the second numeric feature.
    trend: string, default None
        What type of trendline. Options are: 'None', lin', 'poly'.
    band: boolean, default True
        Whether to include 95% confidence interval band.
    
    Return
    ------
    altair.Chart
        A chart consists of a scatterplot with out without trendlines.
    string
        Spearman and Pearson's correlation numbers.
    '''

def cat_cat(cat1, cat2, data, title = '', lab_cat1 = None, lab_cat2 = None, heatmap = True, barchart = True):
    '''
    Create a concatenated charts showing the heatmap of two numeric variables and the barcharts for occurrance of these variables.
    Heatmap will be on the left and the two barcharts will be on the right in the same column.

    Parameter
    ---------
    cat1: string
        Name of the column name for the first categorical variable.
    cat2: string
        Name of the column name for the second categorical variable.
    data: pandas.DataFrame
        Target data frame for visualization.
    title: string, default ''
        Title for the chart.
    lab_cat1: string
        Axis label for the first categorical variable (x-axis).
    lab_cat2: string
        Axis label for the second categorical variable (y-axis).
    heatmap: boolean, default True
        Whether to include a heatmap plot or not.
    barchart: boolean, default True
        Whether to include the barchart or not.

    Return
    ------
    altair.Chart
        A concatenated chart consists of a heatmap and 2 barcharts.
    '''
    
def num_dist( col_num,  data, title = '', lab_num = None,  num_on_x = True, thresh_corr = 0.0, stat = True ):
    '''
    Create a distribution plot of the numeric variable in general and statistical summary  of the feature .
    In addition, the  correlation values  of the variable with other features based on the threshold values 

    Parameter
    ---------
    col_num: string
        Name of the column name for the numeric variable.
    data: pandas.DataFrame
        Target data frame for visualization.
    title: string, default ''
        Title for the chart.
    lab_num: string
        Axis label for the numeric variable.
    thresh_corr: Float, default 0.0
        value to check for correlation 
    stat : Boolean , default True 
        whether to print summary statistic or not 
    
    Return
    ------
    altair.Chart and Table 
        A histogram chart and a table to display correlation and statistical summary
    '''
