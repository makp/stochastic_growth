import matplotlib.pyplot as plt
from brownian_motion import wiener_process


nsteps, npaths = 1000, 20
t, paths = wiener_process(nsteps, npaths)

fig, ax = plt.subplots()

ax.set_xlabel("$t$")
ax.set_ylabel("$W(t)$")
for path in paths:
    ax.plot(t, path)

plt.show()
