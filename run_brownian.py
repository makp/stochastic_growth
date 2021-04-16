import matplotlib.pyplot as plt
from brownian_motion import brownian_motion


nsteps, npaths = 100, 3
t, paths = brownian_motion(nsteps, npaths, 2, 0.5)

fig, ax = plt.subplots()
ax.set_xlabel("$t$")
ax.set_ylabel("X(t)")
for path in paths:
    ax.plot(t, path)

plt.show()
