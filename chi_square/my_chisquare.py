def chi_square(xes, ys):
    chi2 = 0.0
    for i in range(len(xes)):
        chi2 += (ys[i] - xes[i]) ** 2
    return chi2

def reduced_chi_square(xes, ys):
    y_residual = 0.0
    for i in range(len(xes)):
        y_residual += (ys[i] - (xes[i])) ** 2
    y_mean = sum(ys) / len(ys)
    y_sq_devs_from_mean = 0.0
    for i in range(len(ys)):
        y_sq_devs_from_mean += (ys[i] - y_mean) ** 2
    try:
        r2 = 1.0 - (float(y_residual) / float(y_sq_devs_from_mean))
        return r2
    except ZeroDivisionError:
        return None

if __name__ == '__main__':
    pass