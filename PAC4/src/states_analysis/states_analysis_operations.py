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
    """
    Merge two dataframes passed as arguments by their common value 'state'
    :param firearm_df:      dataframe with data of firearms in the USA
    :param population_df:   dataframe with data of population in the USA
    :return:                merged dataframe with all the data together
    """
    print(f"\n5.3:")
    merged_df = pd.merge(firearm_df, population_df, on='state')
    print(f"\nLas 5 primeras líneas del dataframe que mezcla los dos dataframes son:")
    print(merged_df.head())
    return merged_df


# 5.4
def calculate_relative_values(df: DataFrame) -> DataFrame:
    """
    Calculates and creates 3 new columns with the relative values between permits, longguns, handguns and the population
    :param df:  input dataframe
    :return:    dataframe with the 3 new columns
    """
    print(f"\n5.4:")
    df['permit_perc'] = (df['permit'] * 100) / df['pop_2014']
    df['longgun_perc'] = (df['longgun'] * 100) / df['pop_2014']
    df['handgun_perc'] = (df['handgun'] * 100) / df['pop_2014']
    return df


# 5.5
def filter_outliers(df: DataFrame) -> DataFrame:
    """
    Performs an analysis over the previous calculated data
    :param df:  dataframe with the previous calculated data
    """
    print(f"\n5.5:")
    std_before = round(df['permit_perc'].std(), 2)
    permit_mean = round(df['permit_perc'].mean(), 2)
    print(f"\n 1- La media de permisos de armas es de {permit_mean}%:")
    print(f"\n 2- El contenido del estado de Kentucky es el siguiente:")
    print(df[df['state'] == 'Kentucky'])
    df.loc[df['state'] == 'Kentucky', 'permit_perc'] = permit_mean
    print(f"\n 3- El contenido del estado de Kentucky tras modificar 'permit_perc' es el siguiente:")
    print(df[df['state'] == 'Kentucky'])
    permit_mean = round(df['permit_perc'].mean(), 2)
    print(f"\n 4- La media de permisos de armas tras modificar Kentucky es de {permit_mean}%:")
    std_after = round(df['permit_perc'].std(), 2)
    print(f"\n 5- Se ha reducido significativamente el valor de la media. Podemos utilizar un valor como la desviación "
          f"estándar para esa columna (antes: {std_before}, después: {std_after}) para tener más información.\n"
          f"Con estos valores podemos ver que hay una dispersión altísima de los datos (causada por los datos de"
          f" Kentucky)"
          f"\nLa conclusión es que, efectivamente, un valor atípico a la alza o a la baja varía mucho el resultado de"
          f" la media y es peligroso fiarnos solo de este valor sin analizar otros como la desviación estándar.")
    # Devuelvo el dataframe habiendo eliminado el valor atípico para ejercicios posteriores
    return df
