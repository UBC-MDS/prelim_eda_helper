# prelim_eda_helper

This package is a preliminary exploratory data analysis (EDA) tool to make useful feature EDA plots and provide relevant information to simplify an otherwise tedious EDA step of any data science project. Specifically this package allows users to target any two features, whether they are numeric or categorical, and create visualization plots supplemented with useful summary and test statistics.

This package provides a streamlined and easy to use solution for basic EDA tasks that would otherwise require significant amount of coding to achieve. Similar packages can be found published on [PyPi](https://pypi.org/search/?q=eda&page=1) such as the following:

- [eda-viz](https://github.com/ajaymaity/eda-viz)
- [QuickDA](https://github.com/sid-the-coder/QuickDA)

`prelim_eda_helper` enables user to write quick visualization queries. At the same time, as we understand visually strong effects on graphs are not necessarily statistically meaningful, `prelim_eda_helper` is designed to combine graphic visualizations with preliminary statistical test results. We aim to create a helper package to really help researchers to get a quick sense of how our data look like, without making charts and doing tests separately in earlier stages of projects. We believe the combination of graphical and statistical output is what makes `prelim_eda_helper` a unique yet handy helper package.

To achive this goal, `prelim_eda_helper` creates charts with the visualization library [`altair`](https://altair-viz.github.io/) and conducts statistical tests with ['scipy'](https://scipy.org/).

## Usage

### Installation

```bash
$ pip install prelim_eda_helper
```

### `num_cat`

Creates a pair of plots showing the distribution of the numeric variable when grouped by the categorical variable. Output includes a histogram and boxplot. In addition, basic test statistics will be provided for user reference.

```py
from prelim_eda_helper import num_cat
num_cat(v_num = 'x', v_cat = 'group', data = data, title_hist = 'Distribution of X', title_boxplot = 'X Seperated by Group', lab_num = 'X', lab_cat = 'Group', num_on_x = True, stat = True)
```

### `num_num`

Creates a scatter plot given two numerical variables. The plot can provide regression trendline and include confidence interval bands. Spearman and Pearson's correlation will also be returned to aid the user to determining feature relationship.

```py
from prelim_eda_helper import num_num
num_num(num1 = 'x', num2 = 'y', data = data, title = 'Scatter plot with X and Y', lab_num1 = 'X', lab_num2 = 'Y', trend = None, band = False)
```

### `cat_cat`

Creates concatenated charts showing the heatmap of two categorical variables and a barchart for occurrance of these variables.

```py
from prelim_eda_helper import cat_cat
cat_cat(cat1 = 'group1', cat2 = 'group2', data = data, title = 'How are Group1 and Group2 distributed?', lab_cat1 = 'group1', lab_cat2 = 'group2', heatmap = True, barchart = True)
```

### `num_dist`

Creates a distribution plot of the given numeric variable and provides a statistical summary of the feature. In addition, the correlation values of the variable with other numeric features will be provided based on a given threshold.

```py
from prelim_eda_helper import num_dist
num_dist(col_num = 'x', data = data, title = 'Distribution of X', lab_num = 'X',  num_on_x = True, thresh_corr = 0.0, stat = True )
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`prelim_eda_helper` was created by Mehwish Nabi, Morris Chan, Xinry LU, Austin Shih. It is licensed under the terms of the MIT license.

## Credits

`prelim_eda_helper` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
