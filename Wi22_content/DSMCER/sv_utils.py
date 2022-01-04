import numpy as np
import matplotlib
from matplotlib import pyplot as plt

def my_special_margin_plot():
    """Create a plot for lecture ... not a very useful function :)
    """
    X1_bound = np.linspace(-1.5,1.5,100)
    X2_bound = -1*(2*X1_bound + 1) / 3
    plt.figure(figsize=(5.5,5))
    plt.plot(X1_bound, X2_bound)
    plt.xlabel("$X_1$")
    plt.ylabel("$X_2$")
    plt.tight_layout()
    plt.fill_between(X1_bound, X2_bound, 1.5, hatch='.', edgecolor='tab:blue', alpha=0.30)
    plt.fill_between(X1_bound, X2_bound, -1.5, hatch='.', edgecolor='tab:red',alpha=0.30)
    plt.text(-0.6, 1.0, r'$1+2X_1+3X_2>0$', fontsize=20)
    plt.text(-1.3, -1.3, r'$1+2X_1+3X_2<0$', fontsize=20)
    plt.show()

def make_meshgrid(x, y, h=.02, delta=1):
    """Create a mesh of points to plot in

    Parameters
    ----------
    x: data to base x-axis meshgrid on
    y: data to base y-axis meshgrid on
    h: stepsize for meshgrid, optional

    Returns
    -------
    xx, yy : ndarray
    """
    x_min, x_max = x.min() - delta, x.max() + delta
    y_min, y_max = y.min() - delta, y.max() + delta
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy

def plot_contours(ax, clf, xx, yy, **params):

    """Plot the decision boundaries for a classifier based on prediction.

    Parameters
    ----------
    ax: matplotlib axes object
    clf: a classifier
    xx: meshgrid ndarray
    yy: meshgrid ndarray
    params: dictionary of params to pass to contourf, optional
    """
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

def plot_decision_contours(ax, clf, xx, yy, **params):
    
    """Plot the decision boundaries for a classifier based on presence of decision function of with prediction.

    Parameters
    ----------
    ax: matplotlib axes object
    clf: a classifier
    xx: meshgrid ndarray
    yy: meshgrid ndarray
    params: dictionary of params to pass to contourf, optional

    Returns the Z matrix as well as the ax.contour

    """

    if hasattr(clf, "decision_function"):
        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    else:
        Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    Zbi = Z > np.median(Z)
    out = ax.contourf(xx, yy, Zbi, **params)
    
    return out, Z



