from pandas import DataFrame


# 3.1
def groupby_state_and_year(df: DataFrame) -> DataFrame:
    """
    Group the dataframe by state and year, returning the grouped dataframe
    :param df:  input dataframe to be grouped
    :return:    grouped dataframe
    """
    # si llega un dataframe que no tenga las columnas 'state' y 'year' devuelvo un error
    if 'state' not in df.columns or 'year' not in df.columns:
        raise ValueError("The Dataframe must contains the columns 'state' and 'year'")
    # Hago un groupby sobre el dataframe por los campos pedidos usando la operacion sum para agregar todos sus valores
    # Uso la operación reset_index, ya que más adelante me da problemas si no reseteo los índices del dataframe
    return df.groupby(['year', 'state']).sum().reset_index()


# 3.2
def print_biggest_handguns(grouped_df: DataFrame) -> None:
    """
    Print the year and state of the biggest handguns registered. It throws an error if the columns can't be found.
    :param grouped_df:  input dataframe
    """
    # Compruebo que tenga las columnas con las que se va a operar
    if 'state' not in grouped_df.columns or 'year' not in grouped_df.columns or 'handgun' not in grouped_df.columns:
        raise ValueError("The Dataframe must contains the columns 'state', 'year' and 'handgun'")

    # Primero obtengo el índice máximo de la columna handgun para luego, usando ese índice, obtener la row
    # a través de la operación loc. De esta forma puedo sacar luego los valores 'year' y 'state' sin problema.
    max_handguns_row = grouped_df.loc[grouped_df['handgun'].idxmax()]
    print(
        f"El año donde más handguns se han vendido ha sido {max_handguns_row['year']}, y fue en el estado de "
        f"{max_handguns_row['state']}")


# 3.3
def print_biggest_longguns(grouped_df: DataFrame) -> None:
    """
        Print the year and state of the biggest longguns registered. It throws an error if the columns can't be found.
        :param grouped_df:  input dataframe
        """
    # Compruebo que tenga las columnas con las que se va a operar
    if 'state' not in grouped_df.columns or 'year' not in grouped_df.columns or 'longgun' not in grouped_df.columns:
        raise ValueError("The Dataframe must contains the columns 'state', 'year' and 'longgun'")

    # Primero obtengo el índice máximo de la columna handgun para luego, usando ese índice, obtener la row
    # a través de la operación loc. De esta forma puedo sacar luego los valores 'year' y 'state' sin problema.
    max_handguns_row = grouped_df.loc[grouped_df['longgun'].idxmax()]
    print(
        f"El año donde más longguns se han vendido ha sido {max_handguns_row['year']}, y fue en el estado de "
        f"{max_handguns_row['state']}")
