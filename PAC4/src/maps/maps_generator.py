from ..maps import maps_generator_operations as m


def prepare_and_create_maps(firearms_df):
    state_geo = "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json"
    m.create_maps(firearms_df, state_geo)
