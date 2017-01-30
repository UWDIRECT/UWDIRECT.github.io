import pandas as pd

def row_i_to_row_j(row_i, row_j):
    """docstring goes here"""
    return row_i.corr(row_j)

def row_i_to_all_rows(df, index_i, row_i, metric):
    """docstring goes here"""
    for index_j, row_j in df.iterrows():
        # use special features of the matrix
        if index_j < index_i:
            continue
        elif index_i == index_j:
            metric.loc[index_i, index_j] = 1
        else:
            metric.loc[index_i, index_j] = row_i_to_row_j(row_i, row_j)
            metric.loc[index_j, index_i] = metric.loc[index_i, index_j]
    return 

def pairwise_correlation(df):
    """docstring goes here"""
    metric = pd.DataFrame()
    for index_i, row_i in df.iterrows():
        row_i_to_all_rows(df, index_i, row_i, metric)
    return metric
