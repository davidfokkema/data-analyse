import random


def make_figure(N, suffix, show_mean=False):
    random.seed(5)

    xs = []
    with open('scripts/slide-vaakmeten-gemiddelde-%s.out' % suffix, 'w') as f:
        for i in range(1, N + 1):
            x = random.normalvariate(1, 1)
            xs.append(x)
            if i == N:
                f.write(r"\draw (%.3f, 10pt) -- +(0, -20pt) node[below] {$x_{%d}$};" % (x, i))
            else:
                f.write("\draw (%.3f, 10pt) -- +(0, -20pt);" % x)
        mean = sum(xs) / len(xs)
        print mean
        if show_mean:
            f.write(r"\draw[red] (%.3f, 10pt) -- +(0, -20pt) node[below] {$\bar x$};" % mean)
        else:
            f.write(r"\draw[red] (%.3f, 10pt) node[above] {$X$?} -- +(0, -20pt);" % mean)


if __name__ == '__main__':
    make_figure(1, '1')
    make_figure(2, '2')
    make_figure(3, '3')
    make_figure(50, '4')
    make_figure(50, '5', show_mean=True)

    make_figure(1, 'stdmean-1', show_mean=False)
    make_figure(2, 'stdmean-2', show_mean=False)
    make_figure(3, 'stdmean-3', show_mean=False)
    make_figure(48, 'stdmean-4', show_mean=False)
    make_figure(49, 'stdmean-5', show_mean=False)
    make_figure(50, 'stdmean-6', show_mean=False)
