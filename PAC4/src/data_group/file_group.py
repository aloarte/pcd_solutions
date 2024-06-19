from . import group_operations as go
from pandas import DataFrame


def group_file(df: DataFrame) -> DataFrame:
    """
    Group the dataframe by year and state, then prints the country and year where most handguns / longguns were
    registered respectively
    :param df:  Ungrouped dataframe
    :return:    Grouped dataframe by year and state
    """
    print(f"\n------ EJERCICIO 3------\n")
    grouped_df = go.groupby_state_and_year(df)
    go.print_biggest_handguns(grouped_df)
    go.print_biggest_longguns(grouped_df)
    return grouped_df
