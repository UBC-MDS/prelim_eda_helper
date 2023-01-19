import numpy as np
import pandas as pd
import altair as alt
from scipy import stats
from tabulate import tabulate

def initialize_helper():
    """
    A function to enable plotting for large data sets.
    """
    alt.data_transformers.enable( 'data_server')

def num_dist_by_cat(num, cat, data, title_hist ='', title_boxplot ='', lab_num = None, lab_cat = None, num_on_x = True, stat = True):
    """
    Create a pair of charts showing the distribution of the numeric variable and when grouped by the categorical variable.
    The one of the left is a histogram while the one on the left will be a boxplot on top of a violin plot.
    Basic test statistics will be printed for user reference.

    Parameter
    ---------
    num: string
        Name of the column name for the numeric variable.
    cat: string
        Name of the column name for the categorial variable.
    data: pandas.DataFrame
        Target data frame for visualization.
    title_hist: string, default ''
        Title for the histogram.
    title_boxplot: string, default ''
        Title for the boxplot
    lab_num: string
        Axis label for the numeric variable.
    lab_cat: string
        Axis label for the categorical variable.
    num_on_x: boolean, default True
        Whether the numeric variable is put on the x-axis in the boxplot.
    stat: boolean, default True
        Whether printing the test statistics and summary or not.
    
    Return
    ------
    altair.Chart
        A concatenated chart consists of a histogram and a boxplot.
    string
        Test statistics
    """
    hist = alt.Chart( data, title = title_hist).mark_bar().encode(
        x = alt.X(num, bin = alt.Bin(maxbins = 20), title = lab_num),
        y = alt.Y( 'count()', title = lab_cat)
    ).properties(
        height = 300,
        width = 300
    )
    
    if num_on_x == True:
        boxplot = alt.Chart( data, title = title_boxplot).mark_boxplot( size = 50).encode(
            x = alt.X(num, scale = alt.Scale(zero = False), title = lab_num),
            y = alt.Y( f'{v_cat}:N', title = lab_cat)
        ).properties(
            height = 300,
            width = 300
        )
    else:
        boxplot = alt.Chart( data, title = title_boxplot).mark_boxplot( size = 50).encode(
            y = alt.Y(num, scale = alt.Scale(zero = False), title = lab_num),
            x = alt.X( f'{v_cat}:N', title = lab_cat)
        ).properties(
            height = 300,
            width = 300
        )
    
    group_list = data[ v_cat].unique()
    n_group = len( group_list)

    if n_group == 0:
        print( 'Please use a data frame with data inside.\n')
    elif n_group == 1:
        print( 'Please consider using prelim_eda_helper.num_dist when only 1 class is used\n.')
    elif stat == True:
        if n_group == 2:
            if np.var(data[ num]) == 0:
                print( 'A t test is not performed as the total variance is 0.\n')
            else:
                group_a = data[ data[ v_cat] == group_list[ 0]]
                group_b = data[ data[ v_cat] == group_list[ 1]]
                t_eq, p_eq = stats.ttest_ind(group_a[ num], group_b[ num])
                t_w, p_w = stats.ttest_ind(group_a[ num], group_b[ num], equal_var = False)
                table = [ [ 'Equal var. assumed', t_eq, p_eq], [ 'Equal var. not assumed', t_w, p_w]]
                print( f'A t-test assuming equal variance yields a t value of {t_eq:.2f} with a p-value of {p_eq:.4f}.')
                print( f'Assuming inequal variances, the Welch\'s t-test yields a t value of {t_w:.2f} with a p-value of {p_w:.4f}.')
                print( tabulate( table, headers = [ 'Test', 't', 'p']))
        elif n_group > 2:
            vectors = dict()
            for i in group_list:
                vectors[ i] = data[ data[ v_cat] == i][ num]
            if (np.array( [ np.var( i) for i in list( vectors.values())]) == 0).any():
                print( 'F statistic is not defined when within group variance is 0 in at least one of the groups.\n')
            else:
                F, p = stats.f_oneway( *[ list( i) for i in vectors.values()])
                table = [ [ 'One-way ANOVA', F, p]]
                print( f'An one-way ANOVA yields an F score of {F:.2f} with a p-value of {p:.4f}.')
                print( tabulate( table, headers = [ 'Test', 'F', 'p']))
        print()
        
    return hist | boxplot


def num_dist_scatter(num_1, num_2, data, title ='', lab_1 = None, lab_2 = None, trend = None, band = False):
    """
    Creates a scatter plot given two numerical features. Plot can provide regression trendline and highlight outliers.
    Spearman and Pearson's correlation will also be returned to aid the user to determining feature relationship.

    Parameter
    ---------
    num_1: string
        Name of the column name for the first numeric feature.
    num_2: string
        Name of the column name for the second numeric feature.
    data: pandas.DataFrame
        Target data frame for visualization.
    title: string, default ''
        Title for the chart.
    lab_1: string, default None
        Axis label for the first numeric feature.
    lab_2: string, default None
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
    """

def cat_dist_heatmap(cat_1, cat_2, data, title = '', lab_1 = None, lab_2 = None, heatmap = True, barchart = True):
    """
    Create concatenated charts showing the heatmap of two categorical variables and the barcharts for occurrance of these variables.
    Heatmap will be on the left and the two barcharts will be on the right in the same column.

    Parameter
    ---------
    cat_1: string
        Name of the column name for the first categorical variable.
    cat_2: string
        Name of the column name for the second categorical variable.
    data: pandas.DataFrame
        Target data frame for visualization.
    title: string, default ''
        Title for the chart.
    lab_1: string
        Axis label for the first categorical variable (x-axis).
    lab_2: string
        Axis label for the second categorical variable (y-axis).
    heatmap: boolean, default True
        Whether to include a heatmap plot or not.
    barchart: boolean, default True
        Whether to include the barchart or not.

    Return
    ------
    altair.Chart
        A concatenated chart consists of a heatmap and 2 barcharts.
    """

import altair as alt 
def num_dist_summary(num, data, title ='', lab = None, thresh_corr = 0.0, stat = True):
    """
    Create a distribution plot of the numeric variable in general and statistical summary of the feature.
    In addition, the correlation values of the input variable with other features based on a threshold will also be returned.

    Parameter
    ---------
    num: string
        Name of the column name for the numeric variable.
    data: pandas.DataFrame
        Target data frame for visualization.
    title: string, default ''
        Title for the chart.
    lab: string
        Axis label for the numeric variable.
    thresh_corr: Float, default 0.0
        value to check for correlation
    stat : Boolean , default True
        whether to print summary statistic or not
    
    Return
    ------
    altair.Chart and Table
        A histogram chart and a table to display correlation and statistical summary
    string
        correlation values to other features
    """
    if data.shape[0] ==0 : 
        return 'Please use a data frame with data inside.'
    column_names = data.columns.tolist()
    numeric_col = data.select_dtypes(include=np.number).columns.tolist()
    if  not isinstance(num, str) :
        return "Please enter the column name as string"
    if  num not in column_names :
        return  num +  " not present in the dataset"
    elif num  not in numeric_col : 
        return num + " is not a numeric feature " 
    else : 
        hist = alt.Chart(data , title = title).mark_bar().encode(
            x = alt.X(num, bin = alt.Bin(maxbins = 20), title = lab),
            y = alt.Y( 'count()', title = 'Count')
        ).properties(
            height = 300,
            width = 300
        )

        ## find the correlation values based on the threshold and add them to the chart 
        corr_list = ["Correlation values "]
        for col in numeric_col : 
            r = data[num].corr(data[col])
            if r >= thresh_corr  and r != 1: 
                out = col + " : " + str(round(r,2))
                corr_list.append(out)
                
        if len(corr_list) > 1  : 
            text_corr = alt.Chart({'values':[{}]}).mark_text(
                align="left", baseline="top", fontSize=16
                ).encode(
                x=alt.value(40),  # pixels from left
                y=alt.value(30),  # pixels from top
                text=alt.value(corr_list))

            if stat == True : 
                mean = data[num].mean()
                median = data[num].median()
                std = data[num].std()
                text = alt.Chart({'values':[{}]}).mark_text(
                align="left", baseline="top", fontSize=16
                ).encode(
                x=alt.value(40),  # pixels from left
                y=alt.value(30),  # pixels from top
                text=alt.value(["Summary Statistic", f"mean: {mean:.2f}", f"median: {median:.2f}", f"std: {std:.2f}",]))

                return hist |text | text_corr
            
            else : 
                return hist | text_corr

        return hist 
    
