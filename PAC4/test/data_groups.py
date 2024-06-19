import pandas as pd
import PAC4.src.data_group.file_group as fg
import PAC4.src.data_group.group_operations as go
import unittest


class TestDataExpl(unittest.TestCase):
    df = pd.DataFrame({
        'state': ['Alabama', 'Alabama', 'Alaska', 'Alaska', 'Alabama', 'Alaska'],
        'year': [2020, 2020, 2020, 2021, 2021, 2021],
        'handgun': [10, 15, 5, 10, 20, 30],
        'longgun': [10, 15, 5, 10, 20, 30]
    })

    bad_df = pd.DataFrame({
        'state': ['Alabama', 'Alabama', 'Alaska', 'Alaska', 'Alabama', 'Alaska']
    })

    # Ejemplo con el resultado agrupado
    grouped_df = pd.DataFrame({
        'year': [2020, 2020, 2021, 2021],
        'state': ['Alabama', 'Alaska', 'Alabama', 'Alaska'],
        'handgun': [25, 5, 20, 40],
        'longgun': [25, 5, 20, 40]
    })

    def test_groupby_state_and_year(self):
        result_df = go.groupby_state_and_year(self.df)
        # Para poder evaluar que el contenido del dataframe es el mismo tenemos que usar la operación .equals de pandas
        assert result_df.equals(self.grouped_df)

    def test_groupby_state_and_year_error(self):
        with self.assertRaises(ValueError) as context:
            go.groupby_state_and_year(self.bad_df)
        self.assertEqual(str(context.exception), "The Dataframe must contains the columns 'state' and 'year'")

    def test_print_biggest_longguns_error(self):
        with self.assertRaises(ValueError) as context:
            go.print_biggest_longguns(self.bad_df)
        self.assertEqual(
            str(context.exception),
            "The Dataframe must contains the columns 'state', 'year' and 'longgun'")

    def test_print_biggest_handgun_error(self):
        with self.assertRaises(ValueError) as context:
            go.print_biggest_handguns(self.bad_df)
        self.assertEqual(
            str(context.exception),
            "The Dataframe must contains the columns 'state', 'year' and 'handgun'")

    def test_group_file(self):
        result_df = fg.group_file(self.df)
        assert result_df.equals(self.grouped_df)
