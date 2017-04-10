import numpy as np

import artist

np.random.seed(1)

A = 1
B = .4

def make_dataset(std, plot=False, suffix='', N=7):
    f = lambda x: A + B * x

    xdata = np.linspace(.5, 5.5, N)
    ydata = f(xdata) + np.random.normal(loc=0, scale=std, size=N)
    yerr = np.array(N * [std])

    x2 = np.linspace(0, 6, 2)

    rchisq = sum(((ydata - f(xdata)) / yerr) ** 2) / (N - 2)

    if plot:
        plot = artist.Plot()
        plot.plot(xdata, ydata, yerr=yerr, linestyle=None)
        plot.plot(x2, f(x2), mark=None)
        plot.set_xlabel('x')
        plot.set_ylabel('y')
        plot.set_label(r'$\tilde\chi^2 = %.1f$' % rchisq)
        plot.set_xlimits(0, 6)
        plot.set_ylimits(0, 5)
        plot.save('scripts/plot-chisq-%s.tex' % suffix)

    return rchisq


def plot_chisq_histogram(N):
    rchisq = []
    for i in range(10000):
        rchisq.append(make_dataset(.3, N=N))

    plot = artist.Plot(width=r'.5\linewidth')
    n, bins = np.histogram(rchisq, bins=np.linspace(0, 6, 20))
    plot.histogram(n, bins)
    plot.set_xlabel(r'$\tilde\chi^2$')
    plot.set_ylabel('$N$')
    plot.set_xlimits(0, 6)
    plot.set_ylimits(min=0)
    plot.set_label("$N=%d$" % N)
    plot.save('scripts/slide-chisq-histogram-N-%d' % N)


if __name__ == '__main__':
    for i in range(1, 6):
        make_dataset(.3, plot=True, suffix=str(i))

    plot_chisq_histogram(3)
    plot_chisq_histogram(5)
    plot_chisq_histogram(7)
    plot_chisq_histogram(14)
