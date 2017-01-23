import numpy as np

from scipy.optimize import curve_fit


np.random.seed(1)


def fit_data(func, xdata, ydata, yerr):
    figure()
    errorbar(xdata, ydata, yerr, fmt=',')

    popt, pcov = curve_fit(func, xdata, ydata)

    rchisq = sum(((ydata - func(xdata, *popt)) / yerr) ** 2) / (N - len(popt))

    x = linspace(0, 1, 50)
    plot(x, func(x, *popt))

    print "parameters (a, s0, v0):", popt
    print "gereduceerde chi-kwadraat:", rchisq

    return popt


f = lambda t, a, s0, v0: s0 + v0 * t + .5 * a * t ** 2
g = lambda t, a: .5 * a * t ** 2

t = arange(0.1, 1.1, .1)
s = f(t, 9.81 * sin(radians(30)), 0.05, 0)

yerr = .01
N = len(t)
s += normal(0, yerr, N)
s[2] += 4.8 * yerr

popt = fit_data(g, t, s, yerr)
popt = fit_data(f, t, s, yerr)

print s[2], f(.3, *popt), (s[2] - f(.3, *popt)) / yerr

print ' & '.join('%.1f' % u for u in t)
print ' & '.join('%.2f' % u for u in s)

savetxt('data.out', array((t, s, len(t) * [yerr])).T)
