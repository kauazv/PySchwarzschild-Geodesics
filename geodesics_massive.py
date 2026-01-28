import numpy as np
from scipy.integrate import solve_ivp
from schwarzschild import schwarzschild_factor

def geodesic_equations(tau, y, M, E, L):
    t, r, phi, r_dot = y
    f = schwarzschild_factor(r, M)
    dt_dtau = E / f
    dphi_dtau = L / r ** 2
    r_ddot = (
        - M / r ** 2
        + L ** 2 / r ** 3
        - 3 * M * L ** 2 / r ** 4
    )

    return np.array([
        dt_dtau,
        r_dot,
        dphi_dtau,
        r_ddot
    ])

def integrate_geodesic(
        tau_span,
        y0,
        M,
        E,
        L,
        r_stop=2.05,
        max_step=0.1):
    
    def horizon_event(tau,y):
        r = y [1]
        return r - r_stop

    horizon_event.terminal = True
    horizon_event.direction = -1

    solution = solve_ivp(
        fun=lambda tau, y: geodesic_equations(tau, y, M, E, L),
        t_span=tau_span,
        y0=y0,
        method="RK45",
        max_step=max_step,
        events=horizon_event,
        rtol=1e-9,
        atol=1e-9
    )

    return solution