from scipy.optimize import curve_fit

#l = array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
l = array([10, 20, 30, 50, 60, 70, 80, 90, 100])
#t = array([15.0, 19.4, 23.1, 27.7, 29.3, 31.8, 34.3, 36.9, 38.6, 40.7])
t = array([15.0, 19.4, 23.1, 29.3, 31.8, 34.3, 36.9, 38.6, 40.7])
yerr = 0.2
N = len(l)

errorbar(l, t, 0.2, fmt=',')

f = lambda l, g, l0: 20 * 2 * pi * sqrt((l + l0) / g)
popt, pcov = curve_fit(f, l, t, p0=[10., 1.])
rchisq = sum(((t - f(l, *popt)) / yerr) ** 2) / (N - len(popt))

x = linspace(0, 110, 100)
plot(x, f(x, *popt))
print popt
print rchisq
