import pandas as pd
from pandas import DataFrame


# 1.1
def read_csv(path: str) -> DataFrame:
    """
    This function reads a csv file and prints the first 5 lines of the file and its structure.
    :param path: path to the csv file
    :return:    pandas dataframe with the data from the csv file
    """
    df = pd.read_csv(path)
    # 5 es el número por defecto de head()
    print(f"Las 5 primeras líneas del dataframe leído de la ubicación {path} son:")
    print(df.head())
    print(f"\nSu estructura es la siguiente:")
    print(df.info())
    return df


# 1.2
def clean_csv(df: DataFrame) -> DataFrame:
    """
    This function cleans the rest of the columns apart from 'month', 'state', 'permit', 'handgun', 'long_gun' from the
    dataset, returning the cleaned dataframe and printing the columns before and after in order to verify the operation
    :param df:  target dataframe to be cleaned
    :return:    cleaned dataframe
    """
    print(f"\nLas columnas antes de limpiar el dataframe son:")
    print(df.columns)
    columns_to_keep = ['month', 'state', 'permit', 'handgun', 'long_gun']
    cleaned_df = df[columns_to_keep]
    print(f"\nLas columnas tras limpiar el dataframe son:")
    print(cleaned_df.columns)
    return cleaned_df


# 1.3
def rename_col(df: DataFrame) -> DataFrame:
    """
    This function renames the column 'long_gun' to 'longgun'
    :param df:  data frame to rename its columns
    :return:    renamed dataframe
    """
    if 'long_gun' in df.columns:
        renamed_df = df.rename(columns={'long_gun': 'longgun'})
        print(f"\nLas columnas del dataframe tras renombrar son:")
        print(renamed_df.columns)
        return renamed_df
    else:
        print(f"\nEl dataframe no tiene la columna long_gun. Se devuelve el dataframe tal cual fue pasado")
        return df
