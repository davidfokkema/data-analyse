import numpy as np
from scipy.special import erf

import artist

x = np.linspace(0, 4, 51)
y = erf(x / np.sqrt(2))

plot = artist.Plot()
plot.plot(x, y, mark=None)

plot.set_xlabel(r"grenzen [$\sigma$]")
plot.set_ylabel(r"kans waarde valt binnen grenzen [\%]")
# plot.draw_horizontal_line(.5)
# plot.draw_vertical_line(.674)
plot.set_yticks([0, .50, .68, .954, 1.00])
plot.set_xticks([0, .674, 1., 2., 3., 4.])
plot.set_xlimits(0, 4)
plot.set_ylimits(0, 1)
plot.save_as_pdf('scripts/preview')
plot.save('scripts/slide-errorfunction')
