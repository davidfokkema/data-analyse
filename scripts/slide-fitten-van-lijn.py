import numpy as np

A = 1
B = .4

def make_dataset(suffix, seed=1, std=None, show_residuals=False, show_errors=False, larger_errors=True):
    np.random.seed(seed)
    x = np.linspace(.5, 5.5, 7)
    y = A + B * x
    Y = y.copy()

    if std:
        y += np.random.normal(loc=0, scale=std, size=len(y))

    with open('scripts/slide-fitten-van-lijn-%s.out' % suffix, 'w') as f:
        for u, v, w in zip(x, y, Y):
            print u, v, w
            if show_residuals:
                f.write(r"\draw[blue] (%f, %f) -- (%f, %f);" % (u, v, u, w) + '\n')
            if show_errors:
                if larger_errors:
                    error = .05 + .1 * u
                else:
                    error = .05 + .1 * (6 - u)
                f.write(r"\draw (%f, %f) -- (%f, %f);" % (u, v + error, u, v - error) + '\n')
            f.write(r"\fill (%f, %f) circle (1pt);" % (u, v) + '\n')
    print


if __name__ == '__main__':
    make_dataset('1')
    make_dataset('2', std=.3)
    make_dataset('3', std=.3, show_residuals=True)
    make_dataset('4', seed=4, std=.3, show_errors=True)
    make_dataset('5', seed=4, std=.3, show_errors=True, larger_errors=False)
