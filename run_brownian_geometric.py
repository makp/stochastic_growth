import matplotlib.pyplot as plt
from brownian_motion import brownian_geometric

nsteps, npaths = 1000, 8
mu, sigma = 2, 0.5
t, paths = brownian_geometric(nsteps, npaths, mu, sigma)

fig, ax = plt.subplots()
ax.set_xlabel("$t$")
ax.set_ylabel("S(t)")
for path in paths:
    ax.plot(t, path)

plt.show()
