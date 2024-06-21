import folium
import io
from pandas import DataFrame
from PIL import Image


def create_maps(state_geo_url: str, firearms_df: DataFrame) -> None:
    """
    Creates maps trough folium library using the data from the firearms dataframe and the state geography
    :param state_geo_url:   url where the states geographic json data is located
    :param firearms_df:     dataframe with the data extracted from exercise 5.5
    :return:
    """
    create_map(
        state_geo_url,
        firearms_df,
        ["code", "permit_perc"],
        "Firearms permit percentage",
        "m1")

    create_map(
        state_geo_url,
        firearms_df,
        ["code", "longgun_perc"],
        "Firearms long gun percentage",
        "m2")

    create_map(
        state_geo_url,
        firearms_df,
        ["code", "handgun_perc"],
        "Firearms hand gun percentage",
        "m3")


def create_map(state_geo_url: str, firearms_df: DataFrame, columns: list, title: str, map_name: str) -> None:
    """
    Creates a map from the dataframe from the given columns
    :param state_geo_url:   Url where the states info json data is located
    :param firearms_df:     dataframe with the data extracted from exercise 5.5
    :param columns:         columns to be drawn in the map
    :param title:           title of the map that will apear in the legend
    :param map_name:        file name of the map
    """
    firearm_map = folium.Map(location=[40, -95], zoom_start=4)
    folium.Choropleth(
        geo_data=state_geo_url,
        name="choropleth",
        data=firearms_df,
        columns=columns,
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=.1,
        legend_name=title,
    ).add_to(firearm_map)
    folium.LayerControl().add_to(firearm_map)
    save_map(firearm_map, title, map_name)


def save_map(firearm_map: folium.Map, title: str, map_name: str) -> None:
    """
    Save the previously created map from the folium library into html and png
    :param firearm_map:     folium map to be saved as files
    :param title:           title of the map that will apear in the legend
    :param map_name:        file name of the map
    :return:
    """
    maps_path = "../generated/"
    firearm_map.save(f"{maps_path}{map_name}.html")
    print(f"\nMapa para '{title}' generado como .html en /generated")
    img_data = firearm_map._to_png(5)
    img = Image.open(io.BytesIO(img_data))
    img.save(f"{maps_path}{map_name}.png")
    print(f"Mapa para '{title}' generado como .png en /generated")
