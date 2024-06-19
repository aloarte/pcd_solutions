import pandas as pd
import PAC4.src.states_analysis.states_analysis_operations as sao
import PAC4.src.states_analysis.states_analysis as sa
import unittest


class TestDataExpl(unittest.TestCase):
    year_state_grouped_dataframe = pd.DataFrame({
        'year': [2020, 2019, 2019, 2020, 2019, 2020, 2019],
        'state': ['Alabama', 'Alabama', 'Alaska', 'Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands'],
        'permit': [50, 50, 40, 30, 20, 10, 50],
        'handgun': [100, 50, 150, 100, 100, 100, 100],
        'longgun': [200, 50, 150, 200, 200, 200, 200]
    })

    state_grouped_dataframe = pd.DataFrame({
        'state': ['Alabama', 'Alaska', 'Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands'],
        'permit': [100, 40, 30, 20, 10, 50],
        'handgun': [150, 150, 100, 100, 100, 100],
        'longgun': [250, 150, 200, 200, 200, 200]
    })

    states_cleaned_dataframe = pd.DataFrame({
        'state': ['Alabama', 'Alaska'],
        'permit': [100, 40],
        'handgun': [150, 150],
        'longgun': [250, 150]
    })

    def test_groupby_state(self):
        result_df = sao.groupby_state(self.year_state_grouped_dataframe)
        # Para poder evaluar que el contenido del dataframe es el mismo tenemos que usar la operación .equals de pandas
        assert result_df.equals(self.state_grouped_dataframe)

    def test_clean_states(self):
        result_df = sao.clean_states(self.state_grouped_dataframe)
        assert result_df.equals(self.states_cleaned_dataframe)
