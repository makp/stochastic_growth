import numpy as np
import matplotlib.pyplot as plt


def run_wiener(nsteps, npaths):
    """Simulate Wiener processes."""
    t = np.linspace(0, 1, nsteps)
    z = np.random.randn(npaths, nsteps)
    dw = z*np.sqrt(t[1])
    return t, np.cumsum(dw, axis=1)


nsteps, npaths = 1000, 20
t, paths = run_wiener(nsteps, npaths)

fig, ax = plt.subplots()

ax.set_xlabel("$t$")
ax.set_ylabel("$W(t)$")
for path in paths:
    ax.plot(t, path)

plt.show()
