import random

import numpy as np


def make_figure(N, suffix, stddev=False):
    random.seed(5)

    xs = []
    with open('scripts/slide-vaakmeten-stddev-%s.out' % suffix, 'w') as f:
        for i in range(1, N + 1):
            x = random.normalvariate(1, 1)
            xs.append(x)
            if i == N and not stddev:
                f.write(r"\draw (%.3f, 10pt) -- +(0, -20pt) node[below] {$x_{%d}$};" % (x, i))
            else:
                f.write(r"\draw (%.3f, 10pt) -- +(0, -20pt);" % x)
        xs = np.array(xs)
        if stddev:
            f.write(r"\draw[<->,red] (%.3f, -15pt) -- node[below] {$\sigma_x$} (%.3f, -15pt);" % (xs.mean() - xs.std(), xs.mean() + xs.std()))
        else:
            f.write(r"\draw[<->,red] (%.3f, 15pt) -- node[above] {$\delta x$?} (%.3f, 15pt);" % (min(xs), max(xs)))



if __name__ == '__main__':
    make_figure(1, '1')
    make_figure(2, '2')
    make_figure(3, '3')
    make_figure(50, '4')
    make_figure(50, '5', stddev=True)
