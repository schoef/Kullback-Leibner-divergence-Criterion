import numpy as np

from sklearn.datasets import make_gaussian_quantiles

def gauss_easy():
    #Dataset creation
    X1,y1 = make_gaussian_quantiles(mean=(2, 2), cov=1.5, n_samples=1600, n_features=2, n_classes=1, random_state=1)
    X2,y2 = make_gaussian_quantiles(cov=1.2, n_samples=1200, n_features=2, n_classes=1, random_state=1)

    X12 = np.concatenate((X1,X2))
    X = np.concatenate((X12,X12))
    n_samle_size = len(X12)

    # Generating labels
    y1 = np.zeros(n_samle_size)
    y2 = np.ones(n_samle_size)
    y = np.concatenate((y1,y2))

    #Generating weights
    n_alt_hyp_size = len(X1) #BSM
    n_hyp_size = len(X2) #SM
    EPSILON = 0.01

    #in case of y=0, SM
    w_alt_hyp = np.zeros(n_alt_hyp_size)
    w_alt_hyp += (EPSILON / n_alt_hyp_size)
    w_hyp = np.ones(n_hyp_size)
    w_hyp /= n_hyp_size
    w0 = np.concatenate((w_alt_hyp, w_hyp))

    #in case of y=1, BSM
    w_alt_hyp = np.ones(n_alt_hyp_size)
    w_alt_hyp /= n_alt_hyp_size
    w_hyp = np.zeros(n_hyp_size)
    w_hyp += (EPSILON / n_hyp_size)
    w1 = np.concatenate((w_alt_hyp, w_hyp))

    #final weights
    w = np.concatenate((w0,w1))

    w_min = min((2.0 * EPSILON) / n_hyp_size, (2.0 * EPSILON) / n_alt_hyp_size)

    return X, y, w, w_min

def gauss_hard():
    #Dataset creation
    X1,y1 = make_gaussian_quantiles(mean=(2, 2), cov=1.5, n_samples=1600, n_features=2, n_classes=1, random_state=1)
    X2,y2 = make_gaussian_quantiles(cov=1.2, n_samples=1200, n_features=2, n_classes=1, random_state=1)

    X12 = np.concatenate((X1,-X2 + 1))
    X = np.concatenate((X12,X12))
    n_samle_size = len(X12)

    # Generating labels
    y1 = np.zeros(n_samle_size)
    y2 = np.ones(n_samle_size)
    y = np.concatenate((y1,y2))

    #Generating weights
    n_alt_hyp_size = len(X1) #BSM
    n_hyp_size = len(X2) #SM
    EPSILON = 0.01

    #in case of y=0, SM
    w_alt_hyp = np.zeros(n_alt_hyp_size)
    w_alt_hyp += (EPSILON / n_alt_hyp_size)
    w_hyp = np.ones(n_hyp_size)
    w_hyp /= n_hyp_size
    w0 = np.concatenate((w_alt_hyp, w_hyp))

    #in case of y=1, BSM
    w_alt_hyp = np.ones(n_alt_hyp_size)
    w_alt_hyp /= n_alt_hyp_size
    w_hyp = np.zeros(n_hyp_size)
    w_hyp += (EPSILON / n_hyp_size)
    w1 = np.concatenate((w_alt_hyp, w_hyp))

    #final weights
    w = np.concatenate((w0,w1))

    w_min = min((2.0 * EPSILON) / n_hyp_size, (2.0 * EPSILON) / n_alt_hyp_size)

    return X, y, w, w_min
