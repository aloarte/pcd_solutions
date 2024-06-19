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
    grouped_df = grouped_df.drop('year', axis=1)
    print(f"Las 5 primeras líneas del dataframe tras haberlo agrupado por estado son:")
    print(grouped_df.head())
    return grouped_df


# 5.2
def clean_states(df: DataFrame) -> DataFrame:
    """
    Clean the states 'Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands' from the dataframe
    :param df:  dataframe grouped by state
    :return:    dataframe with the desired states removed
    """
    cleaned_df = df[~df['state'].isin(['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands'])]
    print(f"Antes de limpiar los estados había {len(df)}. Tras borrar, quedan {len(cleaned_df)} estados.")
    return cleaned_df
