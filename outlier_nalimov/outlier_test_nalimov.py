import numpy as np
import pandas as pd
from outlier_nalimov import outlier_tables_nalimov as ot


def formula_nalimov(x1, df):
    q = np.abs((x1 - np.average(df)) / np.std(df)) * np.sqrt(len(df) / (len(df) - 1))
    return q


def calc_q_nalimov(df):
    q = []
    for num in df:
        q.append(formula_nalimov(num, df))
    return q


def get_q_crit_nalimov(data, alpha=0.05):
    n_deg_f = len(data) - 2
    if n_deg_f < 1:
        print('not enough degrees of freedom. Make more tests!')
        print('exit program')
        exit()
    table_degree_freedom = ot.nalimov_table()['f'][::-1]
    error_table = ot.nalimov_table()[f'{alpha}'][::-1]

    error_idx = None
    for idx, val in enumerate(table_degree_freedom):
        if n_deg_f >= val:
            error_idx = idx
            break

    if error_idx:
        q_crit = error_table[error_idx]
        return q_crit
    else:
        print('not q_crit found')
        print('Exit programm')
        exit()


def remove_outliers(arr, alpha=0.05, verbose=False):
    if type(arr) == pd.Series:
        arr = arr.to_list()

    q = calc_q_nalimov(arr)
    q_crit = get_q_crit_nalimov(arr, alpha)
    if verbose: print('q_crit', q_crit)
    list_outliers = []
    for i, val in enumerate(q):
        if val < q_crit:
            list_outliers.append(arr[i])
        else:
            list_outliers.append(np.nan)
    return list_outliers


if __name__ == '__main__':
    data = [-4, -5, -6, 45]
    data_corr = remove_outliers(data)
    print(f"original data: {data}")
    print(f"outlier corrected data: {data_corr}")
