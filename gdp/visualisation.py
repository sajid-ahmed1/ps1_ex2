import seaborn as sns
import pandas as pd
import matplotlib


def plot_gdp(df: pd.DataFrame) -> matplotlib.axes.Axes:
    """
    This function takes in a dataframe and plots the GDP of the countries
    in the dataframe.
    """

    return sns.lineplot(data=df, x="Year", y="GDP", hue="Country Name")
