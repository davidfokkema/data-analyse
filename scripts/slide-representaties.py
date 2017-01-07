import numpy as np
from scipy.stats import norm

import artist


def plot_histogram(N, suffix, Nbins=10, ymax=None, draw_distribution=False):
    np.random.seed(1)
    x = np.random.normal(0, 1., N)

    with open('scripts/slide-representaties-histogram-%s.out' % suffix, 'w') as f:
        n, bins = np.histogram(x, bins=np.linspace(-4, 4, Nbins + 1))
        for u, v in zip(bins[:-1], n):
            f.write("%f %f\n" % (u, v))

    plot = artist.Plot(width=r'.5\linewidth')
    plot.histogram(n, bins)
    if draw_distribution:
        x = np.linspace(-4, 4, 50)
        y = (8. / Nbins) * N * norm.pdf(x, loc=0, scale=1.)
        plot.plot(x, y, mark=None, linestyle='red,smooth')
    if ymax:
        plot.set_ylimits(0, ymax)
    else:
        plot.set_ylimits(min=0)
    plot.set_xlimits(-4, 4)
    plot.set_ylabel('Aantal')
    plot.set_label('$N=%d$' % N)
    plot.save('scripts/slide-representaties-histogram-%s.tex' % suffix)


if __name__ == '__main__':
    np.random.seed(1)
    x = np.random.normal(0, 1., 49)

    with open('scripts/slide-representaties-numbers.out', 'w') as f:
        f.write('\quad'.join(['%.3f' % u for u in x]))

    with open('scripts/slide-representaties-getallenlijn.out', 'w') as f:
        for u in x:
            f.write("\draw (%.3f, 10pt) -- +(0, -20pt);" % u)

    plot_histogram(49, '1', ymax=20)

    plot_histogram(10, 'N-1', Nbins=20)
    plot_histogram(100, 'N-2', Nbins=20)
    plot_histogram(1000, 'N-3', Nbins=20)
    plot_histogram(10000, 'N-4', Nbins=20)
    plot_histogram(10000, 'N-5', Nbins=20, draw_distribution=True)
