import numpy as np


def wiener_increments(nsteps, npaths):
    """Generate Wiener increments."""
    t = np.linspace(0, 1, nsteps)
    z = np.random.randn(npaths, nsteps)
    return t, z*np.sqrt(t[1])


def wiener_process(nsteps, npaths):
    """Simulate Wiener processes."""
    t, dw = wiener_increments(nsteps, npaths)
    return t, np.cumsum(dw, axis=1)


def brownian_standard(nsteps, npaths, mu, sigma):
    """Simulate Brownian motion with drift mu and scale sigma."""
    t, dw = wiener_increments(nsteps, npaths)
    dx = mu*t[1] + sigma*dw
    return t, np.cumsum(dx, axis=1)


def brownian_geometric(nsteps, npaths, mu, sigma):
    """Simulate geometric Brownian motion with pars mu and sigma."""
    t, dw = wiener_increments(nsteps, npaths)
    s = np.ones((npaths, nsteps))
    for j in range(1, nsteps):
        s[:, j] = s[:, j-1]*(1 + (mu*t[1] + sigma*dw[:, j]))
    return t, s
