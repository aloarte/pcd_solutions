from . import maps_generator_operations as mgo
from pandas import DataFrame
import os


def prepare_and_create_maps(firearms_df: DataFrame) -> None:
    """
    Prepare the directory and create the maps for the data in the dataframe
    :param firearms_df:     dataframe with firearms data
    """
    print(f"\n6.1")
    state_geo = "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json"
    # Creo el directorio para depositar los mapas generados
    if not os.path.exists("../generated"):
        os.makedirs("../generated")
    # Creo los mapas
    mgo.create_maps(state_geo, firearms_df)
