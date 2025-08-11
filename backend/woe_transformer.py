# woe_transformer.py
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class WoETransformer(BaseEstimator, TransformerMixin):
    def __init__(self, target_col, exclude_cols=None):
        self.target_col = target_col
        self.exclude_cols = exclude_cols if exclude_cols else []
        self.woe_tables_ = None
        self.iv_summary_ = None

    def fit(self, X, y):
        df_train = X.copy()
        df_train[self.target_col] = y
        self.woe_tables_, self.iv_summary_ = calculate_woe_iv_all_variables(
            df_train, target_col=self.target_col, exclude_cols=self.exclude_cols
        )
        return self

    def transform(self, X):
        return apply_woe_transformation(
            df=X,
            woe_tables=self.woe_tables_,
            target_col=self.target_col
        )

    def get_iv_summary(self):
        return self.iv_summary_


def calculate_woe_iv_single_variable(df_train, variable, target):
    df_grouped = df_train.groupby(variable)[target].agg(['count', 'sum']).reset_index()
    df_grouped.columns = [variable, 'Total', 'Bad']
    df_grouped['Good'] = df_grouped['Total'] - df_grouped['Bad']

    total_good = df_grouped['Good'].sum()
    total_bad = df_grouped['Bad'].sum()

    df_grouped['Good_Dist_Smooth'] = (df_grouped['Good'] + 0.5) / (total_good + 0.5)
    df_grouped['Bad_Dist_Smooth'] = (df_grouped['Bad'] + 0.5) / (total_bad + 0.5)
    df_grouped['WOE'] = np.log(df_grouped['Good_Dist_Smooth'] / df_grouped['Bad_Dist_Smooth'])
    df_grouped['IV_Category'] = ((df_grouped['Good'] / total_good) -
                                 (df_grouped['Bad'] / total_bad)) * df_grouped['WOE']

    total_iv = df_grouped['IV_Category'].sum()
    return df_grouped, total_iv


def calculate_woe_iv_all_variables(df_train, target_col, exclude_cols=None):
    if exclude_cols is None:
        exclude_cols = []

    categorical_cols = df_train.select_dtypes(include=['object', 'category']).columns
    categorical_cols = [c for c in categorical_cols if c != target_col and c not in exclude_cols]

    woe_tables = {}
    iv_summary = []

    for col in categorical_cols:
        woe_table, iv_value = calculate_woe_iv_single_variable(df_train, col, target_col)
        woe_tables[col] = woe_table
        iv_summary.append({'Variable': col, 'IV': iv_value})

    iv_summary_df = pd.DataFrame(iv_summary).sort_values('IV', ascending=False)
    return woe_tables, iv_summary_df


def apply_woe_transformation(df, woe_tables, target_col):
    df_transformed = df.copy()

    for variable, woe_table in woe_tables.items():
        if variable in df.columns:
            woe_mapping = dict(zip(woe_table[variable], woe_table['WOE']))
            df_transformed[variable] = df[variable].map(woe_mapping).fillna(0)

    return df_transformed
