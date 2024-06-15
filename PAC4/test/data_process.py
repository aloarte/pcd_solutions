import pandas as pd
import PAC4.PAC4.data_process.process_operations as po
import PAC4.PAC4.data_process.file_process as fp
import unittest


class TestDataExpl(unittest.TestCase):
    plain_dataframe = pd.DataFrame({
        'month': ['2020-1', '1920-10'],
        'state': ['Alabama', 'Alaska']
    })
    breakdown_dataframe = pd.DataFrame({
        'month': ['1', '10'],
        'state': ['Alabama', 'Alaska'],
        'year': ['2020', '1920']

    })
    breakdown_dataframe_month_erased = pd.DataFrame({
        'state': ['Alabama', 'Alaska'],
        'year': ['2020', '1920']
    })
    # Como las funciones modifican la entrada no puedo reusar plain_dataframe
    final_dataframe = pd.DataFrame({
        'month': ['2020-1', '1920-10'],
        'state': ['Alabama', 'Alaska']
    })

    def test_breakdown_date(self):
        result_df = po.breakdown_date(self.plain_dataframe)
        # Para poder evaluar que el contenido del dataframe es el mismo tenemos que usar la operación .equals de pandas
        assert result_df.equals(self.breakdown_dataframe)

    def test_clean_csv(self):
        result_df = po.erase_month(self.breakdown_dataframe)
        assert result_df.equals(self.breakdown_dataframe_month_erased)

    def test_process_file(self):
        result_df = fp.process_file(self.final_dataframe)
        assert result_df.equals(self.breakdown_dataframe_month_erased)
