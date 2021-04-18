import matplotlib.pyplot as plt
from exponential_growth import grow_poisson


n0, ave = 10, 1.1
npaths, nsteps = 15, 50

fig, ax = plt.subplots()
paths = grow_poisson(n0, ave, npaths, nsteps)
for path in paths:
    ax.plot(path)

plt.show()
