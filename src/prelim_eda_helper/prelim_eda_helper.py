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