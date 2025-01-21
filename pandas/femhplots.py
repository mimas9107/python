import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.mosaicplot import mosaic

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
def sort_by_frequency(df, column):
    """
    Sort a dataframe by the frequency of a specified column.

    Parameters:
    df (pandas.DataFrame): The dataframe to sort.
    column (str): The column to count and sort by.

    Returns:
    pandas.DataFrame: The sorted dataframe.
    """
    counts_df = df[column].value_counts().reset_index()
    counts_df.columns = [column, 'count']
    df = df.merge(counts_df, on=column).copy()
    df = df.sort_values('count', ascending=False)
    df.drop(['count'], axis=1, inplace=True)
    return df


def create_box_and_violin_plots(df, x, y, pathname=None):
    """
    Create a box plot and a violin plot for two variables in a dataframe.

    Parameters:
    df (pandas.DataFrame): The dataframe containing the data.
    x (str): The name of the variable to plot on the x-axis.
    y (str): The name of the variable to plot on the y-axis.
    pathname: The path for saving the plots.

    Returns:
    None
    """
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    sns.boxplot(x=y, y=x, data=df)
    plt.title(f'Box Plot of {x} by {y}')

    plt.subplot(1, 2, 2)
    sns.violinplot(x=y, y=x, data=df)
    plt.title(f'Violin Plot of {x} by {y}')

    plt.tight_layout()

    if pathname is not None:
        plt.savefig(pathname)

    return plt


def create_count_plots(df, x, y, pathname=None):
    """
    Create two count plots for a binary outcome variable in a dataframe.

    Parameters:
    df (pandas.DataFrame): The dataframe containing the data.
    x (str): The name of the variable to plot on the x-axis.
    y (str): The name of the binary outcome variable to plot by.
    pathname: The path for saving the plots.

    Returns:
    None
    """
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # Stacked Bar Plot
    sns.countplot(x=x, hue=y, data=df, ax=axs[0])
    axs[0].set_title(f'Stacked Bar Plot of {x} and {y}')
    axs[0].set_xlabel(f'{x}')
    axs[0].set_ylabel('Count')
    if x in ['SURGERY_DEPT', 'SURGICAL_TYPE']:
        axs[0].set_xticklabels(axs[0].get_xticklabels(), rotation=90)  # Rotate x-axis labels

    # Create a contingency table
    contingency_table = pd.crosstab(df[x], df[y])

    # Mosaic Plot
    mosaic(contingency_table.stack(), ax=axs[1])
    axs[1].set_title(f'Mosaic Plot of {x} and {y}')
    axs[1].set_xlabel(f'{y}')
    axs[1].set_ylabel(f'{x}')
    if x in ['SURGERY_DEPT', 'SURGICAL_TYPE']:
        axs[1].set_xticklabels(axs[1].get_xticklabels(), rotation=90)  # Rotate x-axis labels

    # # Count Plot of {x} by {y}=False
    # sns.countplot(x=x, hue=y, data=df[df[y] == False], ax=axs[1, 0])
    # axs[1, 0].set_title(f'Count Plot of {x} by {y}=False')
    # if x in ['SURGERY_DEPT', 'SURGICAL_TYPE']:
    #     axs[1, 0].set_xticklabels(axs[1, 0].get_xticklabels(), rotation=90)  # Rotate x-axis labels
    #
    # # Count Plot of {x} by {y}=True
    # sns.countplot(x=x, hue=y, data=df[df[y] == True], ax=axs[1, 1])
    # axs[1, 1].set_title(f'Count Plot of {x} by {y}=True')
    # if x in ['SURGERY_DEPT', 'SURGICAL_TYPE']:
    #     axs[1, 1].set_xticklabels(axs[1, 1].get_xticklabels(), rotation=90)  # Rotate x-axis labels

    plt.tight_layout()

    if pathname is not None:
        plt.savefig(pathname)

    return plt


def create_scatter_plot(df, x1, x2, y, pathname=None):
    """
    Create a scatter plot for two continuous variables in a dataframe, colored by a binary outcome variable.

    Parameters:
    df (pandas.DataFrame): The dataframe containing the data.
    x1 (str): The name of the first variable to plot on the x-axis.
    x2 (str): The name of the second variable to plot on the y-axis.
    y (str): The name of the binary outcome variable to color by.
    pathname: The path for saving the plot.

    Returns:
    None
    """
    df = sort_by_frequency(df, y)

    plt.figure(figsize=(12, 6))
    sns.scatterplot(x=x1, y=x2, hue=y, style=y, data=df)
    plt.title(f'Scatter Plot of {x1} vs {x2} by {y}')

    if pathname is not None:
        plt.savefig(pathname)

    return plt


def create_corr_heatmap(df, variables, title='Correlation Heatmap', pathname=None):
    """
    Create a correlation heatmap for a set of variables in a dataframe.

    Parameters:
    df (pandas.DataFrame): The dataframe containing the data.
    variables (list): The list of variables to include in the correlation heatmap.
    title (str): The title of the heatmap. Default is 'Correlation Heatmap'.

    Returns:
    None
    """
    plt.figure(figsize=(18, 13.5))
    df = df[variables].copy()
    corr = df[variables].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt='.2f')
    plt.title(title)

    if pathname is not None:
        plt.savefig(pathname)

    return plt
def create_dist_plot(df, x, pathname=None):
    """
    Create a distribution plot for a continuous variable in a dataframe.

    Parameters:
    df (pandas.DataFrame): The dataframe containing the data.
    x (str): The name of the variable to plot.
    pathname: The path for saving the plot.

    Returns:
    None
    """
    plt.figure(figsize=(12, 6))
    sns.displot(df[x], kde=True, bins=30, color='blue')
    plt.title(f'Distribution Plot of {x}')

    if pathname is not None:
        plt.savefig(pathname)

    return plt