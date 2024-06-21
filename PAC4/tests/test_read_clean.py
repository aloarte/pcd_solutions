import pandas as pd
import PAC4.src.read_clean.management_operations as fmo
import PAC4.src.read_clean.file_management as fm
import unittest


class TestReadFile(unittest.TestCase):
    # Creo un Dataframe a través de los datos que debería leer del fichero .csv de prueba
    plain_dataframe = pd.DataFrame({
        'month': [1, 1],
        'state': ['Alabama', 'Alaska'],
        'permit': [31205, 31206],
        'handgun': [34897, 34898],
        'long_gun': [17850, 17851],
        'other_column': [2020, 2021]
    })
    # Dataframe para comprobar cuando se eliminan las otras columnas no deseadas
    cleaned_dataframe = pd.DataFrame({
        'month': [1, 1],
        'state': ['Alabama', 'Alaska'],
        'permit': [31205, 31206],
        'handgun': [34897, 34898],
        'long_gun': [17850, 17851]
    })
    # Dataframe para comprobar el resultado cuando se renombra la columna longgun
    renamed_dataframe = pd.DataFrame({
        'month': [1, 1],
        'state': ['Alabama', 'Alaska'],
        'permit': [31205, 31206],
        'handgun': [34897, 34898],
        'longgun': [17850, 17851],
        'other_column': [2020, 2021]
    })
    # Dataframe para comprobar cuando se renombra la columna long-gun y esta no existe
    dataframe_without_long_gun_col = pd.DataFrame({
        'month': [1, 1],
        'other_column': [2020, 2021]
    })
    # Dataframe procesado por completo
    full_processed_dataframe = pd.DataFrame({
        'month': [1, 1],
        'state': ['Alabama', 'Alaska'],
        'permit': [31205, 31206],
        'handgun': [34897, 34898],
        'longgun': [17850, 17851]
    })

    def test_read_csv(self):
        result_df = fmo.read_csv("PAC4/tests/data/test_data.csv")
        # Para poder evaluar que el contenido del dataframe es el mismo tenemos que usar la operación .equals de pandas
        assert result_df.equals(self.plain_dataframe)

    def test_clean_csv(self):
        result_df = fmo.clean_csv(self.plain_dataframe)
        assert result_df.equals(self.cleaned_dataframe)

    def test_rename_col(self):
        result_df = fmo.rename_col(self.plain_dataframe)
        assert result_df.equals(self.renamed_dataframe)

    def test_rename_col_avoided(self):
        result_df = fmo.rename_col(self.dataframe_without_long_gun_col)
        assert result_df.equals(self.dataframe_without_long_gun_col)

    def test_read_and_clean_file(self):
        result_df = fm.read_and_clean_file("PAC4/tests/data/test_data.csv")
        assert result_df.equals(self.full_processed_dataframe)
