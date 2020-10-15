import scipy.stats as stats
import numpy as np
from outlier_nalimov.outlier_test_nalimov import remove_outliers


def pearson_corr(array1, array2):
    pearson_corr, _ = stats.pearsonr(array1, array2)
    return pearson_corr


def spearman_corr(array1, array2):
    spearman_corr, _ = stats.spearmanr(array1, array2)
    return spearman_corr


def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), stats.sem(a)

    h = se * stats.t.ppf((1 + confidence) / 2., n - 1)
    return m, m - h, m + h


def confidence_value(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    se = stats.sem(a)

    h = se * stats.t.ppf((1 + confidence) / 2., n - 1)
    return h


def confidence_interval(data, confidence=0.95):
    return confidence_value(data, confidence)


def remove_outliers_nalimov(arr, alpha=0.05, verbose=False):
    return remove_outliers(arr, alpha, verbose)


def ttest_two_sided(arr1, arr2, alpha=0.05, verbose=False):
    """
    conducts a two-sided t-test and return the p-value and its significance of difference as a boolean.
    :param arr1: array like object of numbers
    :param arr2: array like object of numbers
    :param alpha: level of alpha mistake
    :return: p-value, significance of difference
    """
    res = stats.ttest_ind(arr1, arr2)
    if res[1] <= alpha:
        if verbose: print(
            f'P-value = {round(res[1], 3)}, i.e. at alpha={alpha} the samples are significantly DIFFERENT')
        is_significant = True
    else:
        if verbose: print(f'P-value = {round(res[1], 3)}, i.e. at alpha={alpha} the samples are from the SAME set')
        is_significant = False
    return res[1], is_significant


if __name__ == '__main__':
    pass
