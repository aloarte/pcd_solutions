from pandas import DataFrame


# 5.1
def groupby_state(df: DataFrame) -> DataFrame:
    """
    Group dataframe by state, accumulating the values of each other column
    :param df:  input dataframe
    :return:    data frame sorted by state
    """
    grouped_df = df.groupby(['state']).sum().reset_index()
    # Al haber agrupado por estado, el acumulado del año o se refleja en un string muy largo o en un
    # número sumado que no tiene sentido, por tanto he eliminado la columna directamente del dataframe
    grouped_df.drop('year', axis=1)
    print(grouped_df.head())
    return grouped_df
