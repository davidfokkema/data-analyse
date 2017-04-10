import numpy as np

import artist


N = 7
A = 1.
B = .4
std = .3


def fit_polynoma(order=1, yerr=.3, suffix=''):
    np.random.seed(1)
    x = np.linspace(.5, 5.5, N)
    y = A + B * x
    y += np.random.normal(loc=0, scale=std, size=len(y))

    x2 = np.linspace(0, 6, 30)
    c = np.polyfit(x, y, order)
    f = np.poly1d(c)

    rchisq = sum(((y - f(x)) / yerr) ** 2) / (N - 2)

    plot = artist.Plot(width=r'.5\linewidth')
    plot.plot(x, y, yerr=[yerr] * len(x), linestyle=None)
    plot.plot(x2, f(x2), mark=None, linestyle='blue,smooth')
    plot.set_xlimits(0, 6)
    plot.set_ylimits(0, 5)
    plot.set_title("Orde: %d" % order)
    plot.set_label(r'$\tilde\chi^2 = %.1f$' % rchisq, location='upper left')
    plot.save('scripts/slide-polynoom-fit-O-%d%s' % (order, suffix))


if __name__ == '__main__':
    fit_polynoma(1)
    fit_polynoma(2)
    fit_polynoma(3)
    fit_polynoma(4)
    fit_polynoma(5)
    fit_polynoma(6)
    fit_polynoma(1, yerr=.5, suffix='-err')
