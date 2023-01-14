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