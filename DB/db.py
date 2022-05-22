import numpy as np
import pandas as pd
from pandas import DataFrame


# yes, it's not true DB...

def create_and_insert():
    df = pd.read_csv('./DB/insert_value_to_table.csv', sep=";", encoding_errors='ignore')
    #df.columns = df.columns.str.strip()
    df = df.drop([10])

    return df


def get_simptom(df: DataFrame, index: int):
    _df = df.iloc[:, index+2:index+4]

    return _df


def delete_symptom(df: DataFrame, index: int):
    df = df.drop([f"p{index+1}(x/w)", f"p{index+1}(x/now)"], axis=1)  # p(x/w) and p(x/now)

    return df
