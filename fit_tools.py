from exponential_regression.exponential_regression import exp_fit


def exponential_regression(arr1, arr2):
    """
    Conduct a non-iterative exponential fit with the fit function a*exp(k*x)+c without initial guess.
    The algorithms originates from Jean Jaquelin's algorithm.
    :param arr1: array-like object of numbers
    :param arr2: array-like object of numbers
    :return: a, k, c of the fit function a*exp(k*x)+c
    """
    return exp_fit(arr1, arr2)


if __name__ == '__main__':
    pass
