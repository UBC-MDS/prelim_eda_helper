# prelim_eda_helper

This package is a preliminary exploratory data analysis tool to make useful feature comparison plots and provide relevant information to simplify an otherwise tedious EDA step of any data science project. Specifically this package allows users to target any two features, whether they are numeric or categorical, and create comparison plots that provide useful information such as Spearman and Pearson's correlation numbers.

This package provides a streamlined and easy to use solution for basic EDA tasks that would otherwise require significant amount of coding to achieve. Similar packages can be found published on [PyPi](https://pypi.org/search/?q=eda&page=1) such as the following:

- [eda-viz](https://github.com/ajaymaity/eda-viz)
- [QuickDA](https://github.com/sid-the-coder/QuickDA)

## Installation

```bash
$ pip install prelim_eda_helper
```

## Main Functions

- `num_cat`: Create a pair of plots showing the distribution of the numeric variable when grouped by the categorical variable. Output includes a histogram and boxplot. In addition, basic test statistics will be provided for user reference.

- `num_num`: Creates a scatter plot given two numerical variables. The plot can provide regression trendline and include confidence interval bands. Spearman and Pearson's correlation will also be returned to aid the user to determining feature relationship.

- `cat_cat`: Creates concatenated charts showing the heatmap of two categorical variables and a barchart for occurrance of these variables.

- `num_dist`: Creates a distribution plot of the given numeric variable and provides a statistical summary of the feature. In addition, the correlation values of the variable with other numeric features will be provided based on a given threshold.

## Usage

Milestone 2

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`prelim_eda_helper` was created by Mehwish Nabi, Morris Chan, Xinry LU, Austin Shih. It is licensed under the terms of the MIT license.

## Credits

`prelim_eda_helper` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
