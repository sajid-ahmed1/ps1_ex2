import polars as pl
from pathlib import Path
from typing import List


# fuction that creates a path to the data folder and then reads in the csv file
def read_data(file_name: str, skip_rows: int = 4) -> pl.DataFrame:
    """
    This function reads in a csv file and returns a polars DataFrame.

    Args:
    file_name: str
    skip_rows: int
    """
    path = Path(__file__).parent.parent / "data" / file_name
    return pl.read_csv(path, skip_rows=skip_rows)


def data_cleaner(
    df: pl.DataFrame, countries: List[str], start: int, end: int
) -> pl.DataFrame:
    """
    This function takes in a dataframe and a list of country codes
    and returns a cleaned dataframe
    with only the countries in the list and the years from start to end.

    Args:
    df: pl.DataFrame
    countries: List[str]
    start: int
    end: int

    Returns:
    df_small: pl.DataFrame
    """

    df_small = df.filter(pl.col("Country Code").is_in(countries))
    cols_to_keep = ["Country Name"] + [str(i) for i in range(start, end)]
    df_small = df_small.select(cols_to_keep)
    df_small = df_small.unpivot(
        index=["Country Name"], variable_name="Year", value_name="GDP"
    )
    df_small = df_small.with_columns(
        pl.col("Year").cast(pl.Int32),
        pl.col("GDP").cast(pl.Float64),
    )
    return df_small.sort("Country Name", "Year")
