from pandas import DataFrame
import pandas as pd


# 5.1
def groupby_state(df: DataFrame) -> DataFrame:
    """
    Group dataframe by state, accumulating the values of each other column
    :param df:  input dataframe
    :return:    data frame sorted by state
    """
    print(f"\n5.1:")
    grouped_df = df.groupby(['state']).sum().reset_index()
    # Al haber agrupado por estado, el acumulado del año o se refleja en un string muy largo o en un
    # número sumado que no tiene sentido, por tanto he eliminado la columna directamente del dataframe
    grouped_df = grouped_df.drop('year', axis=1)
    print(f"\nLas 5 primeras líneas del dataframe tras haberlo agrupado por estado son:")
    print(grouped_df.head())
    return grouped_df


# 5.2
def clean_states(df: DataFrame) -> DataFrame:
    """
    Clean the states 'Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands' from the dataframe
    :param df:  dataframe grouped by state
    :return:    dataframe with the desired states removed
    """
    print(f"\n5.2:")
    cleaned_df = df[~df['state'].isin(['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands'])]
    print(f"\nAntes de limpiar los estados había {len(df)}. Tras borrar, quedan {len(cleaned_df)} estados.")
    return cleaned_df


# 5.3
def merge_datasets(firearm_df: DataFrame, population_df: DataFrame) -> DataFrame:
    print(f"\n5.3:")
    merged_df = pd.merge(firearm_df, population_df, on='state')
    print(f"\nLas 5 primeras líneas del dataframe que mezcla los dos dataframes son:")
    print(merged_df.head())
    return merged_df
