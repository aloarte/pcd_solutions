from pandas import DataFrame


def breakdown_date(df: DataFrame) -> DataFrame:
    """
    Splits the column 'month' from the original dataframe into 2 new columns 'year' and 'day'
    :param df:  input dataframe
    :return:    modified dataframe with the 2 new columns 'year' and 'day'
    """
    # Para cada item de la columna 'month' hago un split por -, que es el caracter que separa el año y el mes
    df[['year', 'month']] = df['month'].str.split('-', expand=True)
    print(f"Las 5 primeras líneas del dataframe tras la modificación de la fecha son:")
    print(df.head())
    return df


def erase_month(df: DataFrame) -> DataFrame:
    """
    Removes the column 'month' from the dataframe
    :param df:  input dataframe
    :return:    modified dataframe without the 'month' column
    """
    df = df.drop(columns=['month'])
    print(f"Las 5 primeras líneas del dataframe tras el limpiado del mes son:")
    print(df.head())
    print(f"Las columnas del dataframe tras el limpiado del mes son:")
    print(df.columns)
    return df
