import folium
from pandas import DataFrame


def create_maps(firearms_df: DataFrame, state_geo_url: str) -> None:
    create_map(
        state_geo_url,
        firearms_df,
        ["code", "permit_perc"],
        "Firearms permit percentage",
        "firearms_permit_percentage_map.html")

    create_map(
        state_geo_url,
        firearms_df,
        ["code", "longgun_perc"],
        "Firearms long gun percentage",
        "firearms_longgun_percentage_map.html")

    create_map(
        state_geo_url,
        firearms_df,
        ["code", "handgun_perc"],
        "Firearms hand gun percentage",
        "firearms_handgun_percentage_map.html")


def create_map(state_geo_url: str, firearms_df: DataFrame, columns: list, title: str, map_name: str):
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
    firearm_map.save(map_name)
